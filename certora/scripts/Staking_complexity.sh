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
    --verify StakingHarness:certora/specs/complexity.spec \
    --packages @openzeppelin=node_modules/@openzeppelin \
    --staging \
    --optimistic_loop \
    --loop_iter 3 \
    --solc solc7.6 \
    $RULE \
    --send_only \
    --msg "StakingHarness complexity: $1 $2"

