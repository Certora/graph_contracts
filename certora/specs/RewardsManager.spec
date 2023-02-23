import "Setup.spec"

// https://vaas-stg.certora.com/output/95893/f4133bd8060c4f999bc3dfdaf58243df/?anonymousKey=303ffe12073a9749cee7b15eeab4e32d84095564

// this allocation  lifecycle is, imo, what we should ideally verify as much as possible, e.g.
// the amount of minted rewards should be monotonically increasing as a function of the time between opening and closing
rule takeRewardsMonoIncreasingWithTime() {
    specVsSolidityConsts();

    env e1; env e2;
    require e1.block.number < e2.block.number;
    address allocationID;

    storage initial = lastStorage;

    uint256 rewards1 = takeRewards(e1, allocationID);
    uint256 rewards2 = takeRewards(e2, allocationID) at initial;

    assert rewards1 <= rewards2;
}

// other allocations on the same subgraph trigger calls to onSubgraphAllocationUpdate, so they can change the resulting rate of accrual of rewards for the other allocation, but piece-wise the amount of rewards should follow the issuance rate
rule takeRewardsMonoIncreasingWithIssurancePerBlock() {
    specVsSolidityConsts();
    storage initial = lastStorage;

    env e;
    address allocationID;

    uint256 issuancePerBlock1;
    uint256 issuancePerBlock2;
    require issuancePerBlock1 < issuancePerBlock2;

    setNewIssuancePerBlock(e, issuancePerBlock1);
    uint256 rewards1 = takeRewards(e, allocationID);

    setNewIssuancePerBlock(e, issuancePerBlock2) at initial;
    uint256 rewards2 = takeRewards(e, allocationID);

    assert rewards1 <= rewards2;
    // assert rewards1>=0;
}

rule takeRewardsTwice() {
    specVsSolidityConsts();
    
    env e;
    address allocationID;

    uint256 rewards = takeRewards(e, allocationID);
    uint256 rewards2 = takeRewards(e, allocationID);
    assert rewards2 == 0;
}

// For @Pablo the main thing that should hold is across several function calls rather than just in takeRewards:
// when an allocation is created, its accRewardsPerAllocatedToken field is set through onSubgraphAllocationUpdate
// when the allocation is closed, takeRewards gets a new value of the accumulated rewards per allocated token, and the minted amount of tokens should equal the difference between these two values multiplied by the amount of allocated tokens

rule takeRewardsCalc() {
    specVsSolidityConsts();

    env e;
    address allocationID;
    uint256 tokens; 

    bytes32 subgraphDeploymentID;
    uint256 _accRewardsPerAllocatedToken;
    _, subgraphDeploymentID, tokens, _, _, _, _, _accRewardsPerAllocatedToken = _staking.getAllocation(e, allocationID);
    uint256 _totalSupply = _graphToken.totalSupply(e);

    uint256 rewards = takeRewards(e, allocationID);

    uint256 accRewardsPerAllocatedToken_;
    _, _, _, accRewardsPerAllocatedToken_ = subgraphs(e, subgraphDeploymentID);
    uint256 totalSupply_ = _graphToken.totalSupply(e);

    assert e.msg.sender == _staking;
    if (isDenied(e, subgraphDeploymentID) == true) {
        assert rewards == 0;
    } else {
        assert rewards == tokens * (accRewardsPerAllocatedToken_ - _accRewardsPerAllocatedToken) / FIXED_POINT_SCALING_FACTOR(e);
    }
    assert totalSupply_ - _totalSupply == rewards;
}

rule complexity_check {
    method f; env e; calldataarg args;

    f(e, args);

    assert false, "this assertion should fail";
}

// rule takeRewards_check() {
//     env e;
//     specVsSolidityConsts();

//     address allocationID;

//     uint256 _totalSupply = _graphToken.totalSupply(e);
//     uint256 _curationBalance = _graphToken.balanceOf(e, _curation);

//     address _indexer;
//     bytes32 _subgraphDeploymentID;
//     uint256 _tokens; // Tokens allocated to a SubgraphDeployment
//     uint256 _createdAtEpoch; // Epoch when it was created
//     uint256 _closedAtEpoch; // Epoch when it was closed
//     uint256 _collectedFees; // Collected fees for the allocation
//     uint256 _effectiveAllocation; // Effective allocation when closed
//     uint256 _accRewardsPerAllocatedTokenAlloc; 

//     _indexer, _subgraphDeploymentID, _tokens, _createdAtEpoch, _closedAtEpoch, _collectedFees, _effectiveAllocation, _accRewardsPerAllocatedTokenAlloc = _staking.getAllocation(e, allocationID);

//     uint256 _accRewardsForSubgraph;
//     uint256 _accRewardsForSubgraphSnapshot;
//     uint256 _accRewardsPerSignalSnapshot;
//     uint256 _accRewardsPerAllocatedTokenSubgraph;

//     _accRewardsForSubgraph, _accRewardsForSubgraphSnapshot, _accRewardsPerSignalSnapshot, _accRewardsPerAllocatedTokenSubgraph = subgraphs(e, _subgraphDeploymentID);

//     uint256 _subgraphSignalledTokens = _curation.getCurationPoolTokens(e, _subgraphDeploymentID);

//     uint256 rewards = takeRewards(e, allocationID);

//     uint256 totalSupply_ = _graphToken.totalSupply(e);

//     address indexer_;
//     bytes32 subgraphDeploymentID_;
//     uint256 tokens_; // Tokens allocated to a SubgraphDeployment
//     uint256 createdAtEpoch_; // Epoch when it was created
//     uint256 closedAtEpoch_; // Epoch when it was closed
//     uint256 collectedFees_; // Collected fees for the allocation
//     uint256 effectiveAllocation_; // Effective allocation when closed
//     uint256 accRewardsPerAllocatedTokenAlloc_; 

//     indexer_, subgraphDeploymentID_, tokens_, createdAtEpoch_, closedAtEpoch_, collectedFees_, effectiveAllocation_, accRewardsPerAllocatedTokenAlloc_ = _staking.getAllocation(e, allocationID);

//     assert subgraphDeploymentID_ == _subgraphDeploymentID;

//     uint256 accRewardsForSubgraph_;
//     uint256 accRewardsForSubgraphSnapshot_;
//     uint256 accRewardsPerSignalSnapshot_;
//     uint256 accRewardsPerAllocatedTokenSubgraph_;

//     accRewardsForSubgraph_, accRewardsForSubgraphSnapshot_, accRewardsPerSignalSnapshot_, accRewardsPerAllocatedTokenSubgraph_ = subgraphs(e, _subgraphDeploymentID);

//     assert tokens_ == _tokens;
//     assert isDenied(e, _subgraphDeploymentID) => rewards == 0;
//     assert totalSupply_ - _totalSupply == rewards;
//     // assert rewards > 0 => _curationBalance > 0;
//     assert rewards > 0 => _subgraphSignalledTokens > minimumSubgraphSignal(e);
//     assert rewards > 0 => issuancePerBlock(e) > 0;
//     assert rewards > 0 => e.block.timestamp > accRewardsPerSignalLastBlockUpdated(e);
//     assert rewards > 0 => tokens_ > 0;
//     assert rewards > 0 => accRewardsPerAllocatedTokenSubgraph_ > accRewardsPerAllocatedTokenAlloc_;
//     assert rewards > 0 => accRewardsPerAllocatedTokenSubgraph_ > _accRewardsPerAllocatedTokenSubgraph;
//     assert rewards > 0 => accRewardsPerSignalSnapshot_ > _accRewardsPerSignalSnapshot;

//     // uint256 rewards2 = takeRewards(e, allocationID);
//     // assert rewards2 == 0;
//     // assert false;
// }

// rule takeRewards_check2() {
//     env e;
//     specVsSolidityConsts();
//     address allocationID;

//     address _indexer;
//     bytes32 _subgraphDeploymentID;
//     uint256 _tokens; // Tokens allocated to a SubgraphDeployment
//     uint256 _createdAtEpoch; // Epoch when it was created
//     uint256 _closedAtEpoch; // Epoch when it was closed
//     uint256 _collectedFees; // Collected fees for the allocation
//     uint256 _effectiveAllocation; // Effective allocation when closed
//     uint256 _accRewardsPerAllocatedTokenAlloc; 

//     _indexer, _subgraphDeploymentID, _tokens, _createdAtEpoch, _closedAtEpoch, _collectedFees, _effectiveAllocation, _accRewardsPerAllocatedTokenAlloc = _staking.getAllocation(e, allocationID);

//     uint256 _totalSupply = _graphToken.totalSupply(e);
//     uint256 _accRewardsPerSignal;
//     uint256 _accRewardsForSubgraph1;
//     uint256 _accRewardsPerAllocatedToken;
//     uint256 _accRewardsForSubgraph2;
//     uint256 _calcRewards;
//     _accRewardsPerSignal = getAccRewardsPerSignal(e);
//     _accRewardsForSubgraph1 = getAccRewardsForSubgraph(e, _subgraphDeploymentID);
//     _accRewardsPerAllocatedToken, _accRewardsForSubgraph2 = getAccRewardsPerAllocatedToken(e, _subgraphDeploymentID);
//     _calcRewards = getRewards(e, allocationID);

//     uint256 rewards = takeRewards(e, allocationID);
//     uint256 totalSupply_ = _graphToken.totalSupply(e);

//     uint256 accRewardsPerSignal_;
//     uint256 accRewardsForSubgraph1_;
//     uint256 accRewardsPerAllocatedToken_;
//     uint256 accRewardsForSubgraph2_;
//     uint256 calcRewards_;
//     accRewardsPerSignal_ = getAccRewardsPerSignal(e);
//     accRewardsForSubgraph1_ = getAccRewardsForSubgraph(e, _subgraphDeploymentID);
//     accRewardsPerAllocatedToken_, accRewardsForSubgraph2_ = getAccRewardsPerAllocatedToken(e, _subgraphDeploymentID);
//     calcRewards_ = getRewards(e, allocationID);

//     assert _accRewardsPerSignal >= accRewardsPerSignal_;
//     assert _accRewardsForSubgraph1 >= accRewardsForSubgraph1_;
//     assert _accRewardsPerAllocatedToken >= accRewardsPerAllocatedToken_;
//     assert _accRewardsForSubgraph2 >= accRewardsForSubgraph2_;
//     assert _calcRewards >= calcRewards_;
// }
