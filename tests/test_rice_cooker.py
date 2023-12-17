import unittest
from rice_cooker.rice_cooker_main import RiceCooker

class TestRiceCooker(unittest.TestCase):
    def setUp(self):
        self.toTest = RiceCooker()
    def test_plug_in_that_rice_cooker(self):
        print(self.toTest.is_plugged_in)
        self.assertEqual(self.toTest.plug_in_or_out_that_rice_cooker(),"Oke now it's plugged in")
    def test_plug_out_that_rice_cooker(self):
        self.toTest.plug_in_or_out_that_rice_cooker()
        self.assertEqual(self.toTest.plug_in_or_out_that_rice_cooker(),"Oke now we removed the plug")
    def test_add_in_some_food_to_cook(self):
        self.assertEqual(self.toTest.add_in_some_food_to_cook("foo"),"Added a food: foo")
    def test_add_in_some_food_fail(self):
        for i in range(20):
            self.toTest.add_in_some_food_to_cook(f"food: {i}")
        self.assertEqual(self.toTest.add_in_some_food_to_cook("last food"),"Oke bro...I don\'t know what you are cooking, but I don\'t think it\'s comestible")
    def test_list_each_food_inside(self):
        for i in range(3):
            self.toTest.add_in_some_food_to_cook(f"food: {i}")
        self.assertEqual(self.toTest.list_each_food_inside(),"Each food inside the rice-cooker, even if you shouldn\'t have more than rice in it:\nfood: 0\nfood: 1\nfood: 2")
    def test_list_each_food_if_ther_is_no_food(self):
        self.assertEqual(self.toTest.throw_at_people(),"Oke...you\'re dumb...or you are just...dumb...Oke...anyway the rice-cooker is broken")
        self.assertEqual(self.toTest.broken,True)
    def test_get_the_dish(self):
        self.assertEqual(self.toTest.get_the_dish("my dish"), "Oke, here is your dish: my dish\nAnyway, I think all you should do with a rice-cooker is...cook rice. If you wanted to cook some steak or something like that inside of it, the only place you belong is in jail.")
    
if __name__ == "__main__":
    unittest.main()