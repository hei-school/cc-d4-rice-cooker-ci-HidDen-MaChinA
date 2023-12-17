class RiceCooker:
    def __init__(self):
        self.is_plugged_in = False
        self.is_filled = False
        self.broken = False
        self.content = []

    def set_content(self, value):
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
        message = 'Each food inside the rice-cooker, even if you shouldn\'t '
        message += 'have more than rice in it:\n{}'.format('\n'.join(self.content))
        return message

    def get_the_dish(self, dish_name):
        self.content = []
        message = f'Oke, here is your dish: {dish_name}\nAnyway, I think all you should '
        message += 'do with a rice-cooker is...cook rice. If you wanted to cook some steak '
        message += 'or something like that inside of it, the only place you belong is in jail.'
        return message

    def throw_at_people(self):
        self.broken = True
        message = 'Oke...you\'re dumb...or you are just...dumb'
        message += '...Oke...anyway the rice-cooker is broken'
        return message
