import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *

# Filter to require at least one S3m43 particle in the event
singleLQFilter = cms.EDFilter("LHEGenericFilter",
    src = cms.InputTag('externalLHEProducer'),
    NumRequired = cms.int32(0),
    ParticleID = cms.vint32(9000007),
    AcceptLogic = cms.string("GT")
)

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'SLHA:readFrom = 0',
            '9000007:all = S3m43 S3m43* 1 -1 1 300 0.537148 291.94 308.06 3.67360578462547e-13',
            '9000007:oneChannel = 1 1.0 101 5 13',
            '9000007:mayDecay = on',
            '9000007:isResonance = on',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters',
        )
    )
)

# Define production sequence
ProductionFilterSequence = cms.Sequence(singleLQFilter*generator)
