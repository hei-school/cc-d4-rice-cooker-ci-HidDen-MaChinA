class RiceCooker {
  constructor () {
    this.isPlugedIn = false
    this.isFiled = false
    this.broken = false
    this.setContent = (value = []) => {
      if (typeof value !== typeof []) {
        throw new Error('dude...you need an array')
      }
      if (value.length > 20) {
        throw new Error('you can\'t have more than 20 food inside it')
      }
      this.content = value
    }
    this.plugInOrOutThatRiceCooker = () => {
      if (this.broken) {
        return 'my guy...you trown it into a person...it\'s broken'
      }
      this.isPlugedIn = !this.isPlugedIn
      return 'oke now it\'s pluged in'
    }
    this.addInSomeFoodToCoock = (food) => {
      if (!this.isFiled) {
        this.content.push(food)
        if (this.content.length === 20) {
          this.isFiled = true
        }
        return 'added a food : ' + food
      }
      return 'oke bro...I don\'t know what you are coocking but i don\'t think it\'s comestible'
    }
    this.listEachFoodInside = () => {
      if (this.content.length === 0) {
        return 'no food inside this'
      }
      let toReturn = 'each food inside the rice-cooker, even if you shouldn\'t have more than rice in it'
      this.content.forEach((value) => {
        toReturn += '\n' + value
      })
      return toReturn
    }
    this.getTheDish = (dishName) => {
      this.content = []
      return 'oke here is your dish: ' + dishName + '\nanyway I think all you should do with a rice-coocker is...coock rice, if you wanted to coock some steak or something like that inside of it, the only place you belonging is in jail.'
    }
    this.throwAtPeople = () => {
      this.broken = true
      return 'oke...you\'re dumb...or you are just...dumb...oke...anyway the rice-coocker is broken'
    }
  }
}

export default RiceCooker
