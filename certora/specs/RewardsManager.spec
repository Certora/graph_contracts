//import "Setup.spec"
using Controller as controller
using Curation as _curation
using EpochManager as _epochManager
using RewardsManagerHarness as _rewardsManager
using Staking as _staking
using GraphToken as _graphToken
using L1GraphTokenGateway as _graphTokenGateway

methods {
 //   graphToken() returns (bytes32) envfree => ALWAYS _graphToken // define function that returns _graphToken

 /*   CURATION() returns (bytes32) envfree
    EPOCH_MANAGER() returns (bytes32) envfree
    REWARDS_MANAGER() returns (bytes32) envfree
    STAKING() returns (bytes32) envfree
    GRAPH_TOKEN() returns (bytes32) envfree
    GRAPH_TOKEN_GATEWAY() returns (bytes32) envfree

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

  */ 
}


rule sanity {
    env e;
    method f;
    calldataarg args;

    f(e, args);
    assert false;
}