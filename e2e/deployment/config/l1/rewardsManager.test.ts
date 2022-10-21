import { expect } from 'chai'
import hre from 'hardhat'
import GraphChain from '../../../../gre/helpers/network'

describe('[L1] RewardsManager configuration', () => {
  const graph = hre.graph()
  const { RewardsManager } = graph.contracts

  before(async function () {
    if (GraphChain.isL2(graph.chainId)) this.skip()
  })

  it('issuancePerBlock should match "issuancePerBlock" in the config file', async function () {
    const value = await RewardsManager.issuancePerBlock()
    expect(value).eq('114155251141552511415') // hardcoded as it's set with a function call rather than init parameter
  })
})