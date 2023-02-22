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
    bytes32 _poi1;
    bytes32 _poi2;

    closeAllocation(e1, _allocationID, _poi1);
    closeAllocation@withrevert(e2, _allocationID, _poi2);
    bool success = !lastReverted;

    assert !success;
}

rule claimManyIntegrity() {
    specVsSolidityConsts();
    env e;
    address _allocationID1; address _allocationID2;
    address[] _allocationArr; 
    bool restake;
    bool claim1Revert; bool claim2Revert; bool claimManyRevert;

    require _allocationArr.length == 2;
    require _allocationArr[0] == _allocationID1;
    require _allocationArr[1] == _allocationID2;
   
    storage initial = lastStorage;

    claim@withrevert(e, _allocationID1, restake);
    claim1Revert = lastReverted;
    claim@withrevert(e, _allocationID2, restake);
    claim2Revert = lastReverted;

    claimMany@withrevert(e, _allocationArr, restake) at initial;
    claimManyRevert = lastReverted;

    assert (claim1Revert || claim2Revert) <=> claimManyRevert;
}

//temporary rule, because array of 2 timed out
rule claimManyIntegrityTest() {
    specVsSolidityConsts();
    env e;
    address _allocationID1; address _allocationID2;
    address[] _allocationArr; 
    bool restake;
    bool claim1Revert; bool claim2Revert; bool claimManyRevert;

    require _allocationArr.length == 1;
    require _allocationArr[0] == _allocationID1;
    //require _allocationArr[1] == _allocationID2;
   
    storage initial = lastStorage;

    claim@withrevert(e, _allocationID1, restake);
    claim1Revert = lastReverted;
    //claim@withrevert(e, _allocationID2, restake);
    //claim2Revert = lastReverted;

    claimMany@withrevert(e, _allocationArr, restake) at initial;
    claimManyRevert = lastReverted;

    assert (claim1Revert) <=> claimManyRevert;
}
invariant closedAtEpochIntegrity(address _allocationID)
    getAllocationClosedAtEpoch(_allocationID) != 0 =>
        getAllocationClosedAtEpoch(_allocationID) >= getAllocationCreatedAtEpoch(_allocationID)
    filtered {
        m -> m.selector != claimMany(address[],bool).selector
        // && m.selector != multicall(bytes[]).selector 
    }
/*
invariant epochAndStateCorrelation(address _allocationID)
    getAllocationClosedAtEpoch(_allocationID) != 0 => 
           (getAllocationState(_allocationID) == AllocationState.Active)
            //AllocationState.Active)
       // require(allocState == AllocationState.Active, "!active");
 */
/*
    /**
     * @dev Possible states an allocation can be
     * States:
     * - Null = indexer == address(0)
     * - Active = not Null && tokens > 0
     * - Closed = Active && closedAtEpoch != 0
     * - Finalized = Closed && closedAtEpoch + channelDisputeEpochs > now()
     * - Claimed = not Null && tokens == 0
     */
  /*  enum AllocationState {
        Null,
        Active,
        Closed,
        Finalized,
        Claimed
    }

_getAllocationState(_allocationID) != AllocationState.Null;
*/

//ideas for invariant:
/*
state active -> epochTime == 0
if epochTimeCreated(allocationId) != 0 => active(allocationId)
if epochTimeClosed(allocationId) !=0  => !active(allocationId) CLAIMED?
invariant epochTimeClosedIntegrity (address allocationId)
{
}
*/

// https://vaas-stg.certora.com/output/95893/961519952853404db67a71ac1989cb56/?anonymousKey=dbcab2adddfaed031d21ae269045e06d945dd078


// rule closeAllocationTwice() {
//     specVsSolidityConsts();
//     env e1; env e2; env e3;
//     method f; calldataarg args; 
//     address _allocationID;
//     bytes32 _poi1;
//     bytes32 _poi3;

//     closeAllocation(e1, _allocationID, _poi1);
//     f(e2, args);
//     closeAllocation@withrevert(e3, _allocationID, _poi3);
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
