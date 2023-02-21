using Controller            as controller
using Curation              as _curation
using EpochManager          as _epochManager
using RewardsManagerHarness as _rewardsManager
using StakingHarness        as _staking
using GraphToken            as _graphToken
using L1GraphTokenGateway   as _graphTokenGateway

methods {
    CURATION()            returns (bytes32) => ghostCuration()
    EPOCH_MANAGER()       returns (bytes32) => ghostEpochManager()
    REWARDS_MANAGER()     returns (bytes32) => ghostRewardsManager() 
    STAKING()             returns (bytes32) => ghostStaking() 
    GRAPH_TOKEN()         returns (bytes32) => ghostGraphToken()
    GRAPH_TOKEN_GATEWAY() returns (bytes32) => ghostGraphTokenGw()
/*
    CURATION()            returns (bytes32) envfree
    EPOCH_MANAGER()       returns (bytes32) envfree
    REWARDS_MANAGER()     returns (bytes32) envfree
    STAKING()             returns (bytes32) envfree
    GRAPH_TOKEN()         returns (bytes32) envfree
    GRAPH_TOKEN_GATEWAY() returns (bytes32) envfree
*/
    // Controller
    getContractProxy(bytes32) returns (address)                                                        => DISPATCHER(true)

    // _curator
    getCurationPoolTokens(bytes32) returns (uint256)                                                   => DISPATCHER(true)

    // _epochManager
    currentEpoch() returns (uint256)                                                                   => DISPATCHER(true)
    epochsSince(uint256) returns (uint256)                                                             => DISPATCHER(true)

    // _graphToken
    balanceOf(address) returns (uint256)                                                               => DISPATCHER(true)
    mint(address,uint256)                                                                              => DISPATCHER(true)

    // _staking
    getSubgraphAllocatedTokens(bytes32) returns (uint256)                                              => DISPATCHER(true)
    isSlasher() returns (bool)                                                                         => DISPATCHER(true)
    getIndexerStake(address) returns ((uint256,uint256,uint256,uint256))                               => DISPATCHER(true)
    closeAllocation(address,bytes32)                                                                   => DISPATCHER(true)    

    // _rewardManager
    takeRewards(address) returns (uint256)                                                             => DISPATCHER(true)
    onSubgraphAllocationUpdate(bytes32) returns (uint256)                                              => DISPATCHER(true)
    getAllocationCreatedAtEpoch(address) returns (uint256) envfree
    getAllocationCreatedAtEpoch(address) returns (uint256)                                             => DISPATCHER(true)
    getAllocationClosedAtEpoch(address) returns (uint256) envfree
    getAllocationClosedAtEpoch(address) returns (uint256)                                              => DISPATCHER(true)
    getAllocation(address) returns ((address,bytes32,uint256,uint256,uint256,uint256,uint256,uint256)) => DISPATCHER(true)
    _addressCache(bytes32) returns (address) envfree
    _addressCache(bytes32) returns (address)                                                           => DISPATCHER(true)
    subgraphs(bytes32) returns (uint256,uint256,uint256,uint256)                                       => DISPATCHER(true)
    accRewardsPerSignalLastBlockUpdated()                                                              => DISPATCHER(true)
    isDenied(bytes32) returns (bool)                                                                   => DISPATCHER(true)
    issuancePerBlock() returns (uint256)                                                               => DISPATCHER(true)
    minimumSubgraphSignal() returns (uint256)                                                          => DISPATCHER(true)
    getAccRewardsPerSignal() returns (uint256)                                                         => DISPATCHER(true)
    getAccRewardsForSubgraph(bytes32) returns (uint256)                                                => DISPATCHER(true)
    getAccRewardsPerAllocatedToken(bytes32) returns (uint256, uint256)                                 => DISPATCHER(true)
    getRewards(address) returns (uint256)                                                              => DISPATCHER(true)
}

ghost ghostCuration() returns bytes32;
ghost ghostEpochManager() returns bytes32;
ghost ghostRewardsManager() returns bytes32;
ghost ghostStaking() returns bytes32;
ghost ghostGraphToken() returns bytes32;
ghost ghostGraphTokenGw() returns bytes32;

function specVsSolidityConsts() {
    require
    _addressCache(ghostCuration())           == _curation                                   &&
    _addressCache(ghostEpochManager())       == _epochManager                               &&
    _addressCache(ghostRewardsManager())     == _rewardsManager                             &&
    _addressCache(ghostStaking())            == _staking                                    &&
    _addressCache(ghostGraphToken())         == _graphToken                                 &&
    _addressCache(ghostGraphTokenGw())       == _graphTokenGateway                          &&
    ghostCuration()       > ghostEpochManager()                                             &&
    ghostEpochManager()   > ghostRewardsManager()                                           &&
    ghostRewardsManager() > ghostStaking()                                                  &&
    ghostStaking()        > ghostGraphToken()                                               &&
    ghostGraphToken()     > ghostGraphTokenGw();
}
/*
function specVsSolidityConsts() {
    require
    CURATION()                           == 0x4375726174696f6e000000000000000000000000000000000000000000000000 &&
    EPOCH_MANAGER()                      == 0x45706f63684d616e616765720000000000000000000000000000000000000000 &&
    REWARDS_MANAGER()                    == 0x526577617264734d616e61676572000000000000000000000000000000000000 &&
    STAKING()                            == 0x5374616b696e6700000000000000000000000000000000000000000000000000 &&
    GRAPH_TOKEN()                        == 0x4772617068546f6b656e00000000000000000000000000000000000000000000 &&
    GRAPH_TOKEN_GATEWAY()                == 0x4772617068546f6b656e47617465776179000000000000000000000000000000
    &&
    _addressCache(CURATION())            == _curation                                                          &&
    _addressCache(EPOCH_MANAGER())       == _epochManager                                                      &&
    _addressCache(REWARDS_MANAGER())     == _rewardsManager                                                    &&
    _addressCache(STAKING())             == _staking                                                           &&
    _addressCache(GRAPH_TOKEN())         == _graphToken                                                        &&
    _addressCache(GRAPH_TOKEN_GATEWAY()) == _graphTokenGateway;
}
*/