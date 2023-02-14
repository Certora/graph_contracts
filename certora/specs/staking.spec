import "Setup.spec"

rule complexity_check(method f) filtered {
    f -> !f.isView
} {
    env e; calldataarg args;

    f(e, args);

    assert false, "this assertion should fail";
}

rule closeAllocation_check() {
    specVsSolidityConsts();
    env e;
    address _allocationID;
    bytes32 _poi;

    closeAllocation(e, _allocationID, _poi);
    closeAllocation@withrevert(e, _allocationID, _poi);
    bool success = !lastReverted;

    assert !success;
}

// rule slash_check(){
//     address _indexer;
//     uint256 _tokens;
//     uint256 _reward;
//     address _beneficiary;
    
//     uint256 _tokensStaked;
//     uint256 _tokensAllocated;
//     uint256 _tokensLocked; 
//     uint256 _tokensLockedUntil; 
//     bool _isSlasher = isSlasher();
//     _tokensStaked, _tokensAllocated, _tokensLocked, _tokensLockedUntil = getIndexerStake(_indexer);


//     slash(_indexer, _tokens, _reward, _beneficiary);

//     uint256 tokensStaked_;
//     uint256 tokensAllocated_;
//     uint256 tokensLocked_; 
//     uint256 tokensLockedUntil_; 

//     assert _isSlasher;
//     assert _tokens > 0;
//     assert _tokens >= _reward;
//     assert _tokensStaked > 0;
//     assert _tokens <= _tokensStaked;
//     assert _beneficiary != 0;
// }
