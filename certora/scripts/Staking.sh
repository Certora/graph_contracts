!/bin/bash

if [[ "$1" ]]
then
    RULE="--rule $1"
fi
certoraRun \
    certora/harnesses/StakingHarness.sol \
    certora/munged/token/GraphToken.sol \
    certora/munged/curation/Curation.sol \
    certora/munged/governance/Controller.sol \
    certora/harnesses/RewardsManagerHarness.sol \
    certora/munged/epochs/EpochManager.sol \
    certora/munged/gateway/L1GraphTokenGateway.sol \
    --link StakingHarness:controller=Controller \
    --verify StakingHarness:certora/specs/Staking.spec \
    --packages @openzeppelin=node_modules/@openzeppelin \
    --staging \
    --optimistic_loop \
    --loop_iter 3 \
    --solc solc7.6 \
    $RULE \
    --send_only \
    --msg "StakingHarness: $1 $2"

