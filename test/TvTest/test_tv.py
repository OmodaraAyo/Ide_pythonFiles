import unittest

from classtask.Tv.tv import Tv


class TestTv(unittest.TestCase):

    def setUp(self):
        self.tv = Tv()

    def test_Tv_Exist(self):
        self.tv

    def test_That_Tv_isOn(self):
        self.assertTrue(self.tv.turn_On())

    def test_That_Tv_isOff(self):
        self.assertFalse(self.tv.turn_0ff())

    def test_That_Tv_default_channel_is_at_Zero(self):
        self.tv.turn_On()
        self.assertEqual(1, self.tv.get_channel())

    def test_that_tv_can_get_tv_channels(self):
        self.tv.turn_On()
        self.assertEqual(1, self.tv.get_channel())

    def test_That_Tv_default_volume_is_at_zero(self):
        self.tv.turn_On()
        self.assertEqual(0, self.tv.get_volume())

    def test_That_Tv_can_increase_volume(self):
        self.tv.turn_On()
        self.tv.set_volume(1)
        self.assertEqual(1, self.tv.get_volume())

    def test_to_increases_tv_channel_by_one_if_channel_up(self):
        self.tv.turn_On()
        self.tv.set_channel(4)
        self.assertEqual(4, self.tv.get_channel())
        self.tv.channel_up()
        self.assertEqual(5, self.tv.get_channel())

    def test_to_decreases_tv_channel_by_one_if_channel_up(self):
        self.tv.turn_On()
        self.tv.set_channel(3)
        self.assertEqual(3, self.tv.get_channel())
        self.tv.channel_down()
        self.assertEqual(2, self.tv.get_channel())

    def test_to_increases_tv_volume_by_one_if_volume_up(self):
        self.tv.turn_On()
        self.tv.set_volume(5)
        self.assertEqual(5, self.tv.get_volume())
        self.tv.volume_up()
        self.assertEqual(6, self.tv.get_volume())

    def test_to_decreases_tv_volume_by_one_if_volume_up(self):
        self.tv.turn_On()
        self.tv.set_volume(3)
        self.assertEqual(3, self.tv.get_volume())
        self.tv.volume_down()
        self.assertEqual(2, self.tv.get_volume())

    def test_to_set_tv_channel_above_100(self):
        self.tv.turn_On()
        expected = f"Channel cannot go above 100"
        self.assertEqual(expected, self.tv.set_channel(101))

    def test_to_set_tv_channel_below_0(self):
        self.tv.turn_On()
        expected = f"Channel cannot go below 0"
        self.assertEqual(expected, self.tv.set_channel(-1))

    def test_to_set_tv_volume_above_100(self):
        self.tv.turn_On()
        expected = f"Volume cannot go above 100"
        self.assertEqual(expected, self.tv.set_volume(105))