#!/bin/bash

# if test -n "$1"
# then
#     METHOD="--method $1"
# fi

# certoraRun certora/configs/Complexity.conf \
#     $METHOD \
#     --send_only \
#     --msg "ControllerHarness:Complexity.spec $1 -- $2" \

    # certora/helpers/DummyERC20A.sol \

if [[ "$1" ]]
then
    RULE="--rule $1"
fi
certoraRun \
    certora/harnesses/StakingHarness.sol \
    certora/munged/token/GraphToken.sol \
    certora/munged/curation/Curation.sol \
    certora/munged/governance/Controller.sol \
    certora/munged/rewards/RewardsManager.sol \
    certora/munged/epochs/EpochManager.sol \
    --link StakingHarness:controller=Controller \
    --link StakingHarness:_graphToken=GraphToken \
    --link StakingHarness:_curation=Curation \
    --link StakingHarness:_rewardsManager=RewardsManager \
    --link StakingHarness:_epochManager=EpochManager \
    --verify StakingHarness:certora/specs/complexity.spec \
    --packages @openzeppelin=node_modules/@openzeppelin \
    --staging \
    --optimistic_loop \
    --loop_iter 3 \
    --solc solc7.6 \
    $RULE \
    --send_only \
    --msg "StakingHarness: $1 $2"

