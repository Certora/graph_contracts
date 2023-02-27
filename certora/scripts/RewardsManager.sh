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
    certora/harnesses/RewardsManagerHarness.sol \
    certora/munged/epochs/EpochManager.sol \
    certora/munged/gateway/L1GraphTokenGateway.sol \
    --link RewardsManagerHarness:controller=Controller \
    --verify RewardsManagerHarness:certora/specs/RewardsManager.spec \
    --packages @openzeppelin=node_modules/@openzeppelin \
    --staging \
    --optimistic_loop \
    --loop_iter 3 \
    --solc solc7.6 \
    $RULE \
    --send_only \
    --rule_sanity=basic \
    --settings -depth=120 \
    --settings -mediumTimeout=600 \
    --settings -t=2400 \
    --msg "RewardsManagerHarness: $1 $2"

    
    # --link RewardsManagerHarness:_graphToken=GraphToken \
    # --link RewardsManagerHarness:_curation=Curation \
    # --link RewardsManagerHarness:_rewardsManager=RewardsManagerHarness \
    # --link RewardsManagerHarness:_epochManager=EpochManager \
