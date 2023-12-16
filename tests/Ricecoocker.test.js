import { describe, it } from 'mocha'
import { assert } from 'chai'
import { RiceCookerGenerator } from './utils/index.js'

describe('testing each functionnaly of the rice-cooker', () => {
  it('should be-pluged in', () => {
    assert.equal(RiceCookerGenerator().plugInOrOutThatRiceCooker(), 'oke now it\'s pluged in')
  })
})
