import "Setup.spec"

rule complexity(method f) filtered {
    f -> !f.isView
} {
    env e; calldataarg args;

    f(e, args);

    assert false, "this assertion should fail";
}

rule closeAllocation() {
    specVsSolidityConsts();
    env e1; env e2; 
    address _allocationID;
    bytes32 _poi;
    require e1.block.timestamp <= e2.block.timestamp;
    require e1.block.number <= e2.block.number;

    closeAllocation(e1, _allocationID, _poi);
    closeAllocation@withrevert(e2, _allocationID, _poi);
    bool success = !lastReverted;

    assert !success;
}


// https://vaas-stg.certora.com/output/95893/961519952853404db67a71ac1989cb56/?anonymousKey=dbcab2adddfaed031d21ae269045e06d945dd078


// rule closeAllocationTwice() {
//     specVsSolidityConsts();
//     env e1; env e2; env e3;
//     method f; calldataarg args; 
//     address _allocationID;
//     bytes32 _poi;
//     require e1.block.timestamp <= e2.block.timestamp;
//     require e2.block.timestamp <= e3.block.timestamp;
//     require e1.block.number <= e2.block.number;
//     require e2.block.number <= e3.block.number;

//     closeAllocation(e1, _allocationID, _poi);
//     f(e2, args);
//     closeAllocation@withrevert(e3, _allocationID, _poi);
//     bool success = !lastReverted;

//     assert !success;
// }


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
