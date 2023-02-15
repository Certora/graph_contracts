pragma solidity ^0.7.6;
pragma abicoder v2;

import "certora/munged/staking/Staking.sol";

contract StakingHarness is Staking {
 /*   function isSlasher() public returns (bool) {
        return slashers[msg.sender];
    }

    function getIndexerStake(address _indexer) public returns (Stakes.Indexer memory) {
        return stakes[_indexer];
    }
    */
}