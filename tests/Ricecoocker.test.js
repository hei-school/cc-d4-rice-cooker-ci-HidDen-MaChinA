import { describe, it } from 'mocha'
import { assert } from 'chai'
import { RiceCookerGenerator } from './utils/index.js'

describe('testing each comportement of rice-cooker pluging fonctionnality', () => {
  it('should be-pluged in', () => {
    assert.equal(RiceCookerGenerator().plugInOrOutThatRiceCooker(), 'oke now it\'s pluged in')
  })
  it('should not work because it\' broken', () => {
    assert.equal(RiceCookerGenerator(true, false, [], false).plugInOrOutThatRiceCooker(), 'my guy...you trown it into a person...it\'s broken')
  })
})
describe('testing each comportement of rice-cooker adding food functionnality', () => {
  it('should add a food named rice', () => {
    assert.equal(RiceCookerGenerator().addInSomeFoodToCoock('rice'), 'added a food : rice')
  })
  it('shouldn\'t be able to add more than 20 food', () => {
    const list = []
    'abcdefghijklmnopqrst'.split('').forEach((str) => { list.push(str) })
    assert.equal(RiceCookerGenerator(false, true, list, true).addInSomeFoodToCoock('rice'), 'oke bro...I don\'t know what you are coocking but i don\'t think it\'s comestible')
  })
  it('should list all the food', () => {
    assert.equal(RiceCookerGenerator(false, false, ['rice', 'floor'], true).listEachFoodInside(), 'each food inside the rice-cooker, even if you shouldn\'t have more than rice in it\nrice\nfloor')
  })
  it('should be no food returned', () => {
    assert.equal(RiceCookerGenerator().listEachFoodInside(), 'no food inside this')
  })
  it('should remove all the things inside of the rice-cooker and remove all the food inside it', () => {
    assert.equal(RiceCookerGenerator().getTheDish('mydish'), 'oke here is your dish: mydish\nanyway I think all you should do with a rice-coocker is...coock rice, if you wanted to coock some steak or something like that inside of it, the only place you belonging is in jail.')
  })
})
describe('should trow it to people', () => {
  it('should throw the rice-cooker to people', () => {
    assert.equal(RiceCookerGenerator().throwAtPeople(), 'oke...you\'re dumb...or you are just...dumb...oke...anyway the rice-coocker is broken')
  })
})
