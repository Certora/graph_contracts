using Controller as controller
using GraphToken as _graphToken
using Curation as _curation
using RewardsManager as _rewardsManager
using EpochManager as _epochManager

methods {
    isSlasher() returns (bool) envfree
    getIndexerStake(address) returns ((uint256,uint256,uint256,uint256)) envfree
}

rule slash_check(){
    address _indexer;
    uint256 _tokens;
    uint256 _reward;
    address _beneficiary;
    
    uint256 _tokensStaked;
    uint256 _tokensAllocated;
    uint256 _tokensLocked; 
    uint256 _tokensLockedUntil; 
    bool _isSlasher = isSlasher();
    _tokensStaked, _tokensAllocated, _tokensLocked, _tokensLockedUntil = getIndexerStake(_indexer);


    slash(_indexer, _tokens, _reward, _beneficiary);

    uint256 tokensStaked_;
    uint256 tokensAllocated_;
    uint256 tokensLocked_; 
    uint256 tokensLockedUntil_; 

    assert _isSlasher;
    assert _tokens > 0;
    assert _tokens >= reward;
    assert _tokensStaked > 0;
    assert _tokens <= _tokensStaked;
    assert _beneficiary != 0;
}

	uint256 tokensCapacity = stake.tokensStaked.add(0);
     uint256 _tokensUsed = stake.tokensUsed();
     if (_tokensUsed > tokensCapacity) {
          tokensAvailable = 0;
        } else
        	tokensAvailable = tokensCapacity.sub(_tokensUsed);	
	if (_tokens > tokensAvailable && indexerStake.tokensLocked > 0) {
            uint256 tokensOverAllocated = _tokens.sub(indexerStake.tokensAvailable());
            uint256 tokensToUnlock = MathUtils.min(tokensOverAllocated, indexerStake.tokensLocked);
            stake.tokensLocked = stake.tokensLocked.sub(_tokens);
       	 if (stake.tokensLocked == 0) {
          	  stake.tokensLockedUntil = 0;
        	}
        }

        // Remove tokens to slash from the stake
        stake.tokensStaked = stake.tokensStaked.sub(_tokens);

        // -- Interactions --

        IGraphToken graphToken = graphToken();

        // Set apart the reward for the beneficiary and burn remaining slashed stake
        if (_tokens.sub(_reward) > 0) {
            _graphToken.burn(_tokens.sub(_reward));
        }
       
        // Give the beneficiary a reward for slashing
        if (_reward > 0) {
            require(_graphToken.transfer(_beneficiary, _reward), "!transfer");
        }
