"""
        this is my file for all the RiceCooker components
"""


class RiceCooker:
    """
        main class for the constructor class
        I made this class to make sur that everything about RiceCooker is
        inside this file and all the methode and information we need to
        run the app is set when we create an instance of RiceCooker
    """
    def __init__(self):
        """
            constructor
        """
        self.is_plugged_in = False
        self.is_filled = False
        self.broken = False
        self.content = []

    def plug_in_or_out_that_rice_cooker(self):
        """
            toogle from true to false is_plugged_in variable

            Return:
            str: the message to desplay
        """
        if self.broken:
            return 'My guy...you threw it into a person...it\'s broken'
        self.is_plugged_in = not self.is_plugged_in
        return 'Oke now it\'s plugged in' if self.is_plugged_in else 'Oke now we removed the plug'

    def add_in_some_food_to_cook(self, food):
        """
            to add some food inside the cooker

            Parameteres:
             - food (str): the food you want to add into it

            Return:
            str: the message
        """
        if not self.is_filled:
            self.content.append(food)
            if len(self.content) == 20:
                self.is_filled = True
            return 'Added a food: ' + food
        return 'Oke bro...I don\'t know what you are cooking, but I don\'t think it\'s comestible'

    def list_each_food_inside(self):
        """
            to list all the food inside the cooker

            Return:
            str: the message
        """
        if not self.content:
            return 'No food inside this'
        message = 'Each food inside the rice-cooker, even if you shouldn\'t '
        message += 'have more than rice in it:\n{}'.format('\n'.join(self.content))
        return message

    def get_the_dish(self, dish_name):
        """
            to get the dish and remove all inside the cooker
            it's like your dish is done so you remove all of this, and remove the dish

            Parameters:
             - dish_name (str): the dish name

            Return:
            str:the message
        """
        self.content = []
        message = f'Oke, here is your dish: {dish_name}\nAnyway, I think all you should '
        message += 'do with a rice-cooker is...cook rice. If you wanted to cook some steak '
        message += 'or something like that inside of it, the only place you belong is in jail.'
        return message

    def throw_at_people(self):
        """
            I don't know why would you do that but you can throw your rice
            cooker into people's face, and break it in the same time

            return:
            str: the message(and a rice-cooker on your face)
        """
        self.broken = True
        message = 'Oke...you\'re dumb...or you are just...dumb'
        message += '...Oke...anyway the rice-cooker is broken'
        return message
