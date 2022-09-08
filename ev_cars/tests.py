from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import EV_Car


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='pass')
        test_user.save()

        test_thing = EV_Car.objects.create(owner=test_user, car_name="model 3", color="red", range="300", year="2020", manufacturer="tesla")
        test_thing.save()

    def test_things_model(self):
        thing = EV_Car.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_car_name = str(thing.car_name)
        actual_color = str(thing.color)
        actual_range = str(thing.range)
        self.assertEqual(actual_owner, "test_user")
        self.assertEqual(actual_color, "red")
        self.assertEqual(actual_car_name, "model 3")
        self.assertEqual(actual_range, "300")