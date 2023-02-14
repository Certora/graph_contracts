
using Controller as controller
using Curation as _curation
using EpochManager as _epochManager
// using RewardsManagerHarness as _rewardsManager
using Staking as _staking
using GraphToken as _graphToken
using L1GraphTokenGateway as _graphTokenGateway

methods {
    CURATION() returns (bytes32) envfree
    EPOCH_MANAGER() returns (bytes32) envfree
    REWARDS_MANAGER() returns (bytes32) envfree
    STAKING() returns (bytes32) envfree
    GRAPH_TOKEN() returns (bytes32) envfree
    GRAPH_TOKEN_GATEWAY() returns (bytes32) envfree

    // _resolveContract(bytes32 _nameHash) returns (address) 
    //     => linkedAddress(_nameHash)
    getAccRewardsPerSignal() returns (uint256) envfree
    getAccRewardsForSubgraph(bytes32) returns (uint256) envfree
    getAccRewardsPerAllocatedToken(bytes32) returns (uint256, uint256) envfree
    getRewards(address) returns (uint256) envfree

    _curation.getCurationPoolTokens(bytes32) returns (uint256) envfree
    _graphToken.balanceOf(address) returns (uint256) envfree
    _graphToken.totalSupply() returns (uint256) envfree
    _graphToken.mint(address,uint256) envfree
    _staking.getAllocation(address) returns ((address,bytes32,uint256,uint256,uint256,uint256,uint256,uint256)) envfree
    _staking.getSubgraphAllocatedTokens(bytes32) returns (uint256) envfree

    getCurationPoolTokens(bytes32) returns (uint256) => DISPATCHER(true)
    balanceOf(address) returns (uint256) => DISPATCHER(true)
    totalSupply() returns (uint256) => DISPATCHER(true)
    mint(address,uint256) => DISPATCHER(true)
    getAllocation(address) returns ((address,bytes32,uint256,uint256,uint256,uint256,uint256,uint256)) => DISPATCHER(true)
    getSubgraphAllocatedTokens(bytes32) returns (uint256) => DISPATCHER(true)
    
    _addressCache(bytes32) returns (address) envfree

    subgraphs(bytes32) returns (uint256,uint256,uint256,uint256) envfree

    accRewardsPerSignalLastBlockUpdated() envfree
    isDenied(bytes32) returns (bool) envfree
    issuancePerBlock() returns (uint256) envfree
    minimumSubgraphSignal() returns (uint256) envfree
}

invariant specVsSolidityConsts()
    CURATION() == 0x4375726174696f6e000000000000000000000000000000000000000000000000 &&
    EPOCH_MANAGER() == 0x45706f63684d616e616765720000000000000000000000000000000000000000 &&
    REWARDS_MANAGER() == 0x526577617264734d616e61676572000000000000000000000000000000000000 &&
    STAKING() == 0x5374616b696e6700000000000000000000000000000000000000000000000000 &&
    GRAPH_TOKEN() == 0x4772617068546f6b656e00000000000000000000000000000000000000000000 &&
    GRAPH_TOKEN_GATEWAY() == 0x4772617068546f6b656e47617465776179000000000000000000000000000000
    &&
    _addressCache(0x4375726174696f6e000000000000000000000000000000000000000000000000) == _curation &&
    _addressCache(0x45706f63684d616e616765720000000000000000000000000000000000000000) == _epochManager &&
    _addressCache(0x526577617264734d616e61676572000000000000000000000000000000000000) == currentContract &&
    _addressCache(0x5374616b696e6700000000000000000000000000000000000000000000000000) == _staking &&
    _addressCache(0x4772617068546f6b656e00000000000000000000000000000000000000000000) == _graphToken &&
    _addressCache(0x4772617068546f6b656e47617465776179000000000000000000000000000000) == _graphTokenGateway


// function linkedAddress(bytes32 _nameHash) returns address {   
//     requireInvariant specVsSolidityConsts();
//     if (_nameHash == 0x4375726174696f6e000000000000000000000000000000000000000000000000)
//         return _curation;
//     if (_nameHash == 0x45706f63684d616e616765720000000000000000000000000000000000000000)
//         return _epochManager;
//     if (_nameHash == 0x526577617264734d616e61676572000000000000000000000000000000000000)
//         return currentContract;
//     if (_nameHash == 0x5374616b696e6700000000000000000000000000000000000000000000000000)
//         return _staking;
//     if (_nameHash == 0x4772617068546f6b656e00000000000000000000000000000000000000000000)
//         return _graphToken;
//     if (_nameHash == 0x4772617068546f6b656e47617465776179000000000000000000000000000000)
//         return _graphTokenGateway;
//     return 0;
// }

rule complexity_check(method f) filtered {
    f -> !f.isView
} {
    env e; calldataarg args;

    f(e, args);

    assert false, "this assertion should fail";
}

// function setup(env e) {
//     requireInvariant specVsSolidityConsts();
//     // require CURATION() == 0x4375726174696f6e000000000000000000000000000000000000000000000000 &&
//     // EPOCH_MANAGER() == 0x45706f63684d616e616765720000000000000000000000000000000000000000 &&
//     // REWARDS_MANAGER() == 0x526577617264734d616e61676572000000000000000000000000000000000000 &&
//     // STAKING() == 0x5374616b696e6700000000000000000000000000000000000000000000000000 &&
//     // GRAPH_TOKEN() == 0x4772617068546f6b656e00000000000000000000000000000000000000000000 &&
//     // GRAPH_TOKEN_GATEWAY() == 0x4772617068546f6b656e47617465776179000000000000000000000000000000
//     // &&
//     // _addressCache(0x4375726174696f6e000000000000000000000000000000000000000000000000) == _curation &&
//     // _addressCache(0x45706f63684d616e616765720000000000000000000000000000000000000000) == _epochManager &&
//     // _addressCache(0x526577617264734d616e61676572000000000000000000000000000000000000) == currentContract &&
//     // _addressCache(0x5374616b696e6700000000000000000000000000000000000000000000000000) == _staking &&
//     // _addressCache(0x4772617068546f6b656e00000000000000000000000000000000000000000000) == _graphToken &&
//     // _addressCache(0x4772617068546f6b656e47617465776179000000000000000000000000000000) == _graphTokenGateway;
//     // require e.msg.sender != _curation;
//     // require e.msg.sender != _epochManager;
//     // require e.msg.sender != _rewardsManager;
//     // require e.msg.sender != _staking;
//     // require e.msg.sender != _graphToken;
//     // require e.msg.sender != _graphTokenGateway;
// }

rule takeRewards_check() {
    env e;
    requireInvariant specVsSolidityConsts();

    address allocationID;

    uint256 _totalSupply = _graphToken.totalSupply();
    // uint256 _curationBalance = _graphToken.balanceOf(_curation);

    // address _indexer;
    // bytes32 _subgraphDeploymentID;
    // uint256 _tokens; // Tokens allocated to a SubgraphDeployment
    // uint256 _createdAtEpoch; // Epoch when it was created
    // uint256 _closedAtEpoch; // Epoch when it was closed
    // uint256 _collectedFees; // Collected fees for the allocation
    // uint256 _effectiveAllocation; // Effective allocation when closed
    // uint256 _accRewardsPerAllocatedTokenAlloc; 

    // _indexer, _subgraphDeploymentID, _tokens, _createdAtEpoch, _closedAtEpoch, _collectedFees, _effectiveAllocation, _accRewardsPerAllocatedTokenAlloc = _staking.getAllocation(allocationID);

    // uint256 _accRewardsForSubgraph;
    // uint256 _accRewardsForSubgraphSnapshot;
    // uint256 _accRewardsPerSignalSnapshot;
    // uint256 _accRewardsPerAllocatedTokenSubgraph;

    // _accRewardsForSubgraph, _accRewardsForSubgraphSnapshot, _accRewardsPerSignalSnapshot, _accRewardsPerAllocatedTokenSubgraph = subgraphs(_subgraphDeploymentID);

    // uint256 _subgraphSignalledTokens = _curation.getCurationPoolTokens(_subgraphDeploymentID);

    uint256 rewards = takeRewards(e, allocationID);

    uint256 totalSupply_ = _graphToken.totalSupply();

    // address indexer_;
    // bytes32 subgraphDeploymentID_;
    // uint256 tokens_; // Tokens allocated to a SubgraphDeployment
    // uint256 createdAtEpoch_; // Epoch when it was created
    // uint256 closedAtEpoch_; // Epoch when it was closed
    // uint256 collectedFees_; // Collected fees for the allocation
    // uint256 effectiveAllocation_; // Effective allocation when closed
    // uint256 accRewardsPerAllocatedTokenAlloc_; 

    // indexer_, subgraphDeploymentID_, tokens_, createdAtEpoch_, closedAtEpoch_, collectedFees_, effectiveAllocation_, accRewardsPerAllocatedTokenAlloc_ = _staking.getAllocation(allocationID);

    // assert subgraphDeploymentID_ == _subgraphDeploymentID;

    // uint256 accRewardsForSubgraph_;
    // uint256 accRewardsForSubgraphSnapshot_;
    // uint256 accRewardsPerSignalSnapshot_;
    // uint256 accRewardsPerAllocatedTokenSubgraph_;

    // accRewardsForSubgraph_, accRewardsForSubgraphSnapshot_, accRewardsPerSignalSnapshot_, accRewardsPerAllocatedTokenSubgraph_ = subgraphs(_subgraphDeploymentID);

    // assert tokens_ == _tokens;
    // assert isDenied(_subgraphDeploymentID) => rewards == 0;
    // assert totalSupply_ - _totalSupply == rewards;
    // assert rewards > 0 => _curationBalance > 0;
    // assert rewards > 0 => _subgraphSignalledTokens > minimumSubgraphSignal();
    // assert rewards > 0 => issuancePerBlock() > 0;
    // assert rewards > 0 => e.block.timestamp > accRewardsPerSignalLastBlockUpdated();
    // assert rewards > 0 => tokens_ > 0;
    // assert rewards > 0 => accRewardsPerAllocatedTokenSubgraph_ > accRewardsPerAllocatedTokenAlloc_;
    // assert rewards > 0 => accRewardsPerAllocatedTokenSubgraph_ > _accRewardsPerAllocatedTokenSubgraph;
    // assert rewards > 0 => accRewardsPerSignalSnapshot_ > _accRewardsPerSignalSnapshot;

    uint256 rewards2 = takeRewards(e, allocationID);
    assert rewards2 == 0;
    // assert false;
}


// rule takeRewards_check2() {
//     env e;
//     requireInvariant specVsSolidityConsts();

//     address allocationID;

//     uint256 _totalSupply = _graphToken.totalSupply(e);

//     uint256 _accRewardsPerSignal;
//     uint256 _accRewardsForSubgraph1;
//     uint256 _accRewardsPerAllocatedToken;
//     uint256 _accRewardsForSubgraph2;
//     uint256 _calcRewards;
//     _accRewardsPerSignal = getAccRewardsPerSignal();
//     _accRewardsForSubgraph1 = getAccRewardsForSubgraph(allocationID);
//     _accRewardsPerAllocatedToken, _accRewardsForSubgraph2 = getAccRewardsPerAllocatedToken(allocationID);
//     _calcRewards = getRewards(allocationID);

//     uint256 rewards = takeRewards(e, allocationID);

//     uint256 totalSupply_ = _graphToken.totalSupply(e);

//     uint256 accRewardsPerSignal_;
//     uint256 accRewardsForSubgraph1_;
//     uint256 accRewardsPerAllocatedToken_;
//     uint256 accRewardsForSubgraph2_;
//     uint256 calcRewards_;
//     accRewardsPerSignal_ = getAccRewardsPerSignal();
//     accRewardsForSubgraph1_ = getAccRewardsForSubgraph(allocationID);
//     accRewardsPerAllocatedToken_, accRewardsForSubgraph2_ = getAccRewardsPerAllocatedToken(allocationID);
//     calcRewards_ = getRewards(allocationID);
// }
