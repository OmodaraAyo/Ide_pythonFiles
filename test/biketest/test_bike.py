import unittest

from classtask.Bike.bike import Bike


class TestBike(unittest.TestCase):

    def setUp(self):
        self.bike = Bike()

    def test_that_bike_exist(self):
        self.bike

    def test_to_turn_bike_on(self):
        self.assertTrue(self.bike.turn_on())

    def test_to_turn_bike_off(self):
        self.assertFalse(self.bike.turn_off())

    def test_to_accelerate_when_BikeIsOn_and_gear_is_set_to_one_bike_speed_increases_by_one(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.accelerate(1, 19)
        self.assertEqual(20, self.bike.get_speed())

    def test_to_accelerate_when_BikeIsOn_and_gear_is_set_to_two_bike_speed_increases_by_two(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.accelerate(2, 24)
        self.assertEqual(26, self.bike.get_speed())

    def test_to_accelerate_when_BikeIsOn_and_gear_is_set_to_three_bike_speed_increases_by_three(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.accelerate(3, 35)
        self.assertEqual(38, self.bike.get_speed())

    def test_to_accelerate_when_BikeIsOn_and_gear_is_set_to_four_bike_speed_increases_by_three(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.accelerate(4, 44)
        self.assertEqual(48, self.bike.get_speed())

    def test_when_BikeIsOff_and_gear_and_speed_are_set_raise_error_message(self):
        self.assertEqual("Bike is not On", self.bike.accelerate(3, 35))

    def test_to_decelerate_when_BikeIsOn_and_gear_is_set_to_one_bike_speed_decreases_by_one(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.decelerate(1, 15)
        self.assertEqual(14, self.bike.get_speed())

    def test_to_decelerate_when_BikeIsOn_and_gear_is_set_to_two_bike_speed_decreases_by_two(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.decelerate(2, 24)
        self.assertEqual(22, self.bike.get_speed())

    def test_to_decelerate_when_BikeIsOn_and_gear_is_set_to_three_bike_speed_decreases_by_three(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.decelerate(3, 35)
        self.assertEqual(32, self.bike.get_speed())

    def test_to_decelerate_when_BikeIsOn_and_gear_is_set_to_four_bike_speed_decreases_by_four(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.decelerate(4, 44)
        self.assertEqual(40, self.bike.get_speed())

    def test_to_decelerate_when_BikeIsOff_and_gear_and_speed_are_set_raise_error_message(self):
        self.assertEqual("Bike is not On", self.bike.decelerate(3, 35))