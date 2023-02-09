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
    certora/harnesses/RewardsManagerHarness.sol \
    certora/munged/token/GraphToken.sol \
    certora/munged/curation/Curation.sol \
    certora/munged/governance/Controller.sol \
    certora/munged/rewards/RewardsManager.sol \
    certora/munged/epochs/EpochManager.sol \
    --link RewardsManagerHarness:controller=Controller \
    --link RewardsManagerHarness:_graphToken=GraphToken \
    --link RewardsManagerHarness:_curation=Curation \
    --link RewardsManagerHarness:_rewardsManager=RewardsManager \
    --link RewardsManagerHarness:_epochManager=EpochManager \
    --verify RewardsManagerHarness:certora/specs/complexity.spec \
    --packages @openzeppelin=node_modules/@openzeppelin \
    --staging \
    --optimistic_loop \
    --loop_iter 3 \
    --solc solc7.6 \
    $RULE \
    --send_only \
    --msg "RewardsManagerHarness: $1 $2"

