class RiceCooker {
  constructor () {
    this.isPlugedIn = false
    this.isFiled = false
    this.broken = false
    this.content = []
    this.plugInOrOutThatRiceCooker = () => {
      if (this.broken) {
        return "my guy...you trown it into a person...it's broken"
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
    this.getTheDish = (dishName) => {
      return 'oke here is your dish: " + dishName + "\nanyway I think all you should do with a rice-coocker is...coock rice, if you wanted to coock some steak or something like that inside of it, the only place you belonging is in jail.'
    }
    this.throwAtIt = () => {
      this.broken = true
      return 'oke...you\'re dumb...or you are just...dumb...oke...anyway the rice-coocker is broken'
    }
  }
}

export default RiceCooker
