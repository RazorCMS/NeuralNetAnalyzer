import copy

VERSION = "V3p15_13Oct2017_Inclusive"

TREETYPES = { '1L':'OneLeptonFull',
              '1LInv':'OneLeptonAddToMET',
              '2L':'DileptonFull',
              '2LInv':'DileptonAddToMET',
              'VetoL':'VetoLepton',
              'VetoTau':'VetoTau',
              'Photon':'PhotonAddToMET',
              'Signal':'',
              'SignalFastsim':'',
              }
ANALYZERS = { '1L':'InclusiveControlRegion',
              '1LInv':'InclusiveControlRegion',
              '2L':'InclusiveControlRegion',
              '2LInv':'InclusiveControlRegion',
              'VetoL':'InclusiveControlRegion',
              'VetoTau':'InclusiveControlRegion',
              'Photon':'InclusiveControlRegion',
              'Signal':'InclusiveSignalRegion',
              'SignalFastsim':'InclusiveSignalRegion',
              }
#adapt to Si's file naming system
TREETYPEEXT = TREETYPES.copy()
TREETYPEEXT['1LInv'] = (TREETYPEEXT['1LInv'].replace('MET','Met'))+'Full'
TREETYPEEXT['2LInv'] = (TREETYPEEXT['2LInv'].replace('MET','Met'))+'Full'
TREETYPEEXT['VetoL'] += 'Full'
TREETYPEEXT['VetoTau'] += 'Full_RazorSkim'
TREETYPEEXT['Photon'] = 'PhotonFull'
SKIMS = { '1L':'SingleLeptonSkim',
          '1LInv':'SingleLeptonSkim',
          '2L':'DileptonSkim',
          '2LInv':'DileptonSkim',
          'VetoL':'',
          'VetoTau':'',
          'Photon':'',
          'Signal':'',
          'SignalFastsim':'',
          }

DIR = '/eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoInclusiveControlRegion/2016/'+VERSION
DIRS = { tag:DIR+'/'+TREETYPES[tag] for tag in TREETYPES }
DIRS['Signal'] = '/eos/cms/store/group/phys_susy/razor/Run2Analysis/InclusiveSignalRegion/2016/'+VERSION+'/Signal'
DIRS['SignalFastsim'] = '/eos/cms/store/group/phys_susy/razor/Run2Analysis/InclusiveSignalRegion/2016/'+VERSION+'/SignalFastsim'

OPTIONS = { '1L':1101,
            '1LInv':2102,
            '2L':1203,
            '2LInv':3204,
            'VetoL':1007,
            'VetoTau':1009,
            'Photon':5505,
            'Signal':10,
            'SignalFastsim':1,
          }

SUFFIXES = { '1L':'',
             '1LInv':'_NoW',
             '2L':'',
             '2LInv':'_NoZ',
             'VetoL':'',
             'VetoTau':'',
             'Photon':'_NoPho',
             'Signal':'',
             'SignalFastsim':'',
             }

SAMPLES = {}
SAMPLES['1L'] = {
        "DYJets":[
             #'DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             ],
        "QCD":[
             #'QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             ],
        "SingleTop":[
             'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1',
             'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1',
             'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1',
             'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',
             'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',
             ],
        "TTJets":[
             'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
             #'TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8',
             #'TTJets_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8',
             #'TTJets_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8',
            ],
        "TTJetsHTBinned":[
                'TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', # needs additional skim HT < 600
                'TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
            ],
        "Other":[
                'WWTo2L2Nu_13TeV-powheg',
                'WWTo4Q_13TeV-powheg',
                'WWToLNuQQ_13TeV-powheg',
                'WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8',
                'WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8',
                'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
                'WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
                'ZZTo2L2Nu_13TeV_powheg_pythia8',
                'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
                'ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8',
                'ZZTo4L_13TeV_powheg_pythia8',
                'ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8',
                'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
                'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
                'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
                'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
                'WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
                'WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
                'WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
                'ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
            ],
        "WJets":[
                'WJetsToLNu_Wpt-0To50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
                'WJetsToLNu_Wpt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
                'WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
                'WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
                'WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
                'WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
            ],
        "ZInv":[
                'ZJetsToNuNu_HT-100To200_13TeV-madgraph',
                'ZJetsToNuNu_HT-200To400_13TeV-madgraph',
                'ZJetsToNuNu_HT-400To600_13TeV-madgraph',
                'ZJetsToNuNu_HT-600To800_13TeV-madgraph',
                'ZJetsToNuNu_HT-800To1200_13TeV-madgraph',            
                'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph',
                'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph',
            ],
        }
SAMPLES['1LInv'] = SAMPLES['1L'].copy()
SAMPLES['1LInv']['WJets'] = [
        'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        ]
SAMPLES['2L'] = SAMPLES['1L'].copy()
SAMPLES['2LInv'] = SAMPLES['1L'].copy()
SAMPLES['VetoL'] = SAMPLES['1L'].copy()
SAMPLES['VetoTau'] = SAMPLES['1L'].copy()
SAMPLES['Photon'] = {
        "GJetsDR0p4":[
                'GJets_DR-0p4_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
            ],
        "GJets":[
                'GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',             
            ],
        "QCD":[
                'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
            ],
        "Other":[
                'TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8',
                'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
                'WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
            ],
        }
SAMPLES['Signal'] = SAMPLES['1L'].copy()
SAMPLES['Signal']['TTJets1L'] = [
                'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                #'TTJets_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8',
                #'TTJets_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8',
            ]
SAMPLES['Signal']['TTJets2L'] = [
                'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
                #'TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8',
            ]
del SAMPLES['Signal']['TTJets']

FASTSIM_SUFFIX = '_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'
FASTSIM_SAMPLES = [
#        'SMS-T1bbbb',
#        'SMS-T1ttbb',
#        'SMS-T1tttt',
#        'SMS-T1qqqq',
#        'SMS-T2bb',
#        'SMS-T2bt',
#        'SMS-T2tt_dM-10to80_genHT-160_genMET-80',
#        'SMS-T2tt_mStop-150to250',
#        'SMS-T2tt_mStop-250to350',
#        'SMS-T2tt_mStop-350to400',
#        'SMS-T2tt_mStop-400to1200',
        'SMS-T2qq',
        #'SMS-T1tbs_RPV_mGluino1000to1200',
        #'SMS-T1tbs_RPV_mGluino1300to1400',
        #'SMS-T1tbs_RPV_mGluino1500',
        #'SMS-T1tbs_RPV_mGluino750',
        #'SMS-T2bW',
        #'SMS-T2cc_genHT-160_genMET-80',
        #'SMS-T5qqqqVV',
        #'SMS-T5qqqqVV_dM20',
        #'SMS-T5ttcc',
        ]
SAMPLES['SignalFastsim'] = { sample:[sample+FASTSIM_SUFFIX] for sample in FASTSIM_SAMPLES }

DATA = {}
DATA['1L'] = {
        "SingleMuon":[
                'SingleMuon_2016B_03Feb2017',
                'SingleMuon_2016C_03Feb2017',
                'SingleMuon_2016D_03Feb2017',
                'SingleMuon_2016E_03Feb2017',
                'SingleMuon_2016F_03Feb2017',
                'SingleMuon_2016G_03Feb2017',
                'SingleMuon_2016H_03Feb2017v2',
                'SingleMuon_2016H_03Feb2017v3',
            ],
        "SingleElectron":[
                'SingleElectron_2016B_03Feb2017',
                'SingleElectron_2016C_03Feb2017',
                'SingleElectron_2016D_03Feb2017',
                'SingleElectron_2016E_03Feb2017',
                'SingleElectron_2016F_03Feb2017',
                'SingleElectron_2016G_03Feb2017',
                'SingleElectron_2016H_03Feb2017v2',
                'SingleElectron_2016H_03Feb2017v3',
            ]
        }
DATA['1LInv'] = DATA['1L'].copy()
DATA['2L'] = DATA['1L'].copy()
DATA['2LInv'] = DATA['1L'].copy()
DATA['VetoL'] = { 'HTMHT':[
                'HTMHT_2016B_03Feb2017',
                'HTMHT_2016C_03Feb2017',
                'HTMHT_2016D_03Feb2017',
                'HTMHT_2016E_03Feb2017',
                'HTMHT_2016F_03Feb2017',
                'HTMHT_2016G_03Feb2017',
                'HTMHT_2016H_03Feb2017v2',
                'HTMHT_2016H_03Feb2017v3',
                ] }
DATA['VetoTau'] = { 'HTMHT':copy.copy(DATA['VetoL']['HTMHT']) }
DATA['Photon'] = {
        "SinglePhoton":[
                'SinglePhoton_2016B_03Feb2017',
                'SinglePhoton_2016C_03Feb2017',
                'SinglePhoton_2016D_03Feb2017',
                'SinglePhoton_2016E_03Feb2017',
                'SinglePhoton_2016F_03Feb2017',
                'SinglePhoton_2016G_03Feb2017',
                'SinglePhoton_2016H_03Feb2017v2',
                'SinglePhoton_2016H_03Feb2017v3',
                ]
        }
DATA['Signal'] = DATA['1L'].copy()
DATA['Signal']["HTMHT"] = copy.copy(DATA['VetoL']['HTMHT'])

EXTRASKIMS = {
        'TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':'genHT < 600',
        }
