pragma solidity ^0.7.6;
pragma abicoder v2;

import "certora/munged/rewards/RewardsManager.sol";

contract RewardsManagerHarness is RewardsManager {
    function setNewIssuancePerBlock(uint256 _issuancePerBlock) public {
        issuancePerBlock = _issuancePerBlock;
    }

}