import h5py
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.externals import joblib
import pickle 
import argparse

DATA_DIR = '/bigdata/shared/analysis/'
SCALER = 'scaler.pkl'

# Convert to regular numpy arrays
def to_regular_array(struct_array):
    return struct_array.view((np.float32, len(struct_array.dtype.names)))

def clean_dataset(arr):
    print "Before cleaning: {}".format(arr.shape)
    df = pd.DataFrame(data=arr)
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    cleaned = pd.DataFrame.as_matrix(df[indices_to_keep].astype(np.float32))
    print "After cleaning: {}".format(cleaned.shape)
    return cleaned

def multiply_data(data, multiplicity):
    print "Dataset size before multiplicity: {}".format(data.shape[0])
    for i in range(multiplicity):
        if i==0: sum_data = np.copy(data)
        else: sum_data = np.hstack((sum_data, data))
    # Reduce the weight of the sum:
    # sum_data['weight'] /= multiplicity
    print "Dataset size after multiplicity: {}".format(sum_data.shape[0])
    return sum_data

def create_dataset():
    BACKGROUND = ['DYJets','Other','QCD','SingleTop','TTJets','WJets','ZInv']
    SIGNAL = ['T2qq_900_850']
    print "Creating dataset..."
    for i,bkg in enumerate(BACKGROUND):
        _file = h5py.File(DATA_DIR+'/'+bkg+'.h5','r')
        if i == 0: Background = np.copy(_file['Data'])
        else: Background = np.hstack((Background, _file['Data']))
    Signal = h5py.File(DATA_DIR+SIGNAL[0]+'.h5','r')['Data'][:]

    print "Background size: {}".format(Background.shape[0]) 
    print "Signal size: {}".format(Signal.shape[0])

    # Get shuffled unified dataset for training
    Dataset = np.hstack((Background, Signal))
    np.random.shuffle(Dataset)

    # 60% training, 20% validation, 20% testing
    data_size = Dataset.shape[0]
    training_index = int(0.6*data_size)
    val_index = training_index + int(0.2*data_size)

    Dataset = to_regular_array(Dataset)
    Dataset = clean_dataset(Dataset)
    
    unique, counts = np.unique(Dataset[:,0], return_counts=True)
    occur = dict(zip(unique, counts)) # this hopefully returns {0: bkg, 1: sn}
    print "Original label counts: {}".format(occur)


    # Save to files
    combine = h5py.File(DATA_DIR+"/CombinedDataset.h5","w")
    combine['Training'] = Dataset[:training_index]
    combine['Validation'] = Dataset[training_index:val_index]
    combine['Test'] = Dataset[val_index:]
    print "Save divided datasets to {}/CombinedDataset.h5".format(DATA_DIR)
    combine.close()

def load_dataset(location, load_type = 0):
    loadfile = h5py.File(location,"r")

    def decode(load_type):
        if load_type == 0: return "Training"
        elif load_type == 1: return "Validation"
        else: return "Test"

    dat = loadfile[decode(load_type)]
    _x = dat[:,2:]
    _y = dat[:,0].astype(int)
    _weight = dat[:,1]
    return _x, _y, _weight

def get_class_weight(label):
    unique, counts = np.unique(label, return_counts=True)
    occur = dict(zip(unique, counts)) # this hopefully returns {0: bkg, 1: sn}
    print "occur: {}".format(occur)
    class_weight = {occur.keys()[0]: 1, occur.keys()[1]: occur[occur.keys()[0]]/occur[occur.keys()[1]]}
    print "class_weight: {}".format(class_weight)
    return class_weight

def scale_fit(x_train):
    scaler = preprocessing.StandardScaler().fit(x_train)
    joblib.dump(scaler, SCALER)
    print "Saving scaler information to {}".format(SCALER)

def scale_dataset(x_train):
    scaler = joblib.load(SCALER)
    x_train = scaler.transform(x_train)
    return x_train

def create_model():
    from keras.models import Model
    from keras.layers import Input, Dense
    
    # Training with a simple FFNN
    i = Input(shape=(14,))
    layer = Dense(100, activation = 'relu')(i)
    layer = Dense(100, activation = 'relu')(layer)
    layer = Dense(100, activation = 'relu')(layer)
    layer = Dense(100, activation = 'relu')(layer)
    layer = Dense(10, activation = 'relu')(layer)
    o = Dense(1, activation = 'sigmoid')(layer)

    model = Model(i,o)
    model.summary()
    return model

def training():
    print "Loading data..."
    x_train, y_train, weight_train = load_dataset(DATA_DIR+"/CombinedDataset.h5",0)
    x_val, y_val, weight_val = load_dataset(DATA_DIR+"/CombinedDataset.h5",1)

    print "Scaling features..."
    scale_fit(x_train)
    scale_dataset(x_train)
    scale_dataset(x_val)
    
    class_weight = get_class_weight(y_train)

    model = create_model()
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', weighted_metrics=['accuracy'], metrics=['accuracy'])
    
    from keras.callbacks import ModelCheckpoint
    hist = model.fit(x_train, y_train,
            validation_data = (x_val, y_val, weight_val),
            nb_epoch = 10,
            batch_size = 128,
            class_weight = class_weight,
            sample_weight = weight_train,
            callbacks = [ModelCheckpoint(filepath='CheckPoint.h5', verbose = 1)],
            )

    histfile = 'history.sav'
    pickle.dump(hist.history, open(histfile,'wb'))

def testing():
    print "Loading the model checkpoint..."
    from keras.models import load_model
    model = load_model('CheckPoint.h5')
    x_test, y_test, weight_test = load_dataset(DATA_DIR+"/CombinedDataset.h5",2)
    x_bkg = x_test[np.where(y < 1)]
    x_sn = x_test[np.where(y>0)]

    bkg_pred = model.predict(x_bkg)
    sn_pred = model.predict(x_sn)

    test_result = h5py.File("TestResult.h5")
    test_result['Signal'] = sn_pred
    test_result['Background'] = bkg_pred
    test_result.close()

create_dataset()
training()

