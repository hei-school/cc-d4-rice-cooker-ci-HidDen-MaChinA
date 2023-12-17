class RiceCooker:
    def __init__(self):
        self.is_plugged_in = False
        self.is_filled = False
        self.broken = False
        self.content = []

    def set_content(self, value=[]):
        if not isinstance(value, list):
            raise ValueError('Dude, you need an array')
        if len(value) > 20:
            raise ValueError('You can\'t have more than 20 food inside it')
        self.content = value

    def plug_in_or_out_that_rice_cooker(self):
        if self.broken:
            return 'My guy...you threw it into a person...it\'s broken'
        self.is_plugged_in = not self.is_plugged_in
        return 'Oke now it\'s plugged in' if self.is_plugged_in else 'Oke now we removed the plug'

    def add_in_some_food_to_cook(self, food):
        if not self.is_filled:
            self.content.append(food)
            if len(self.content) == 20:
                self.is_filled = True
            return 'Added a food: ' + food
        return 'Oke bro...I don\'t know what you are cooking, but I don\'t think it\'s comestible'

    def list_each_food_inside(self):
        if not self.content:
            return 'No food inside this'
        return 'Each food inside the rice-cooker, even if you shouldn\'t have more than rice in it:\n{}'.format('\n'.join(self.content))

    def get_the_dish(self, dish_name):
        self.content = []
        return 'Oke, here is your dish: {}\nAnyway, I think all you should do with a rice-cooker is...cook rice. If you wanted to cook some steak or something like that inside of it, the only place you belong is in jail.'.format(dish_name)

    def throw_at_people(self):
        self.broken = True
        return 'Oke...you\'re dumb...or you are just...dumb...Oke...anyway the rice-cooker is broken'
