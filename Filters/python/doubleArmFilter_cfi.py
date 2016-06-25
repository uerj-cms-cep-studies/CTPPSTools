import FWCore.ParameterSet.Config as cms

doubleArmFilter = cms.EDFilter( 'DoubleArmFilter'
                               , vertices = cms.InputTag('offlineSlimmedPrimaryVertices')
                               , ppsLabel = cms.string('PPSReco')
                               , tofRes = cms.uint32(50) # picoseconds
                              )
