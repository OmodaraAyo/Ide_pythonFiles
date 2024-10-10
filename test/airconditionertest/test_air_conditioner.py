import unittest

from airconditioner.air_conditioner import Ac


class AirConditionerTest(unittest.TestCase):

    def setUp(self):
        self.ac = Ac()

    def test_to_turn_on_Ac(self):
        self.ac.turn_on()
        self.assertTrue(self.ac.power_status())

    def test_to_turn_off_Ac(self):
        self.ac.turn_off()
        self.assertFalse(self.ac.power_status())

    def test_to_increase_Ac_temperature_when_ac_is_On(self):
        self.ac.turn_on()
        self.assertTrue(self.ac.power_status())
        self.ac.increase_temperature()
        self.assertEqual(17, self.ac.get_temperature())

    def test_to_increase_Ac_temperature_when_ac_is_not_On(self):
        self.assertEqual("Ac is not On", self.ac.increase_temperature())

    def test_to_decrease_Ac_temperature_when_ac_is_On(self):
        self.ac.turn_on()
        self.assertTrue(self.ac.power_status())
        self.ac.increase_temperature()
        self.assertEqual(17, self.ac.get_temperature())
        self.ac.decrease_temperature()
        self.assertEqual(16, self.ac.get_temperature())

    def test_that_when_ac_is_Off_temperature_sets_back_to_16(self):
        self.ac.turn_on()
        self.assertTrue(self.ac.power_status())
        self.ac.increase_temperature()
        self.assertEqual(17, self.ac.get_temperature())
        self.ac.increase_temperature()
        self.assertEqual(18, self.ac.get_temperature())
        self.ac.turn_off()
        self.assertFalse(self.ac.power_status())
        self.ac.turn_on()
        self.assertTrue(self.ac.power_status())
        self.assertEqual(16, self.ac.get_temperature())




