import datetime
import time
import unittest

from SimpleTimeManagement import Hourglass
from SimpleTimeManagement.hourglass import HourglassError


class HourglassTest(unittest.TestCase):
    """
    Tests of ``SimpleTimeManagement.Hourglass`` class.
    """

    def setUp(self):
        pass

    def test_01_init_no_args(self):
        """if no args ar provided to __init__, it should raise a TypeError"""
        with self.assertRaises(TypeError):
            h = Hourglass()

    def test_02_init_duration_negative(self):
        """if the duration provided is negative, it should raise a ValueError"""
        with self.assertRaises(ValueError):
            h = Hourglass(duration=-1)

        with self.assertRaises(ValueError):
            h = Hourglass(-1)

    def test_03_init_duration_float(self):
        """if the duration provided is a float, it should raise a NotImplementedError"""
        with self.assertRaises(NotImplementedError):
            h = Hourglass(duration=1.2)

        with self.assertRaises(NotImplementedError):
            h = Hourglass(1.2)

    def test_04_multiple_starts(self):
        """Test if the start method raise a HourglassError if called 2 times"""
        h = Hourglass(duration=5)
        h.start()
        with self.assertRaises(HourglassError):
            h.start()

    def test_05_is_running(self):
        """Test the `is_running` attribut"""
        h = Hourglass(duration=5)

        self.assertIsInstance(h.is_running, bool)
        self.assertFalse(h.is_running)

        h.start()
        self.assertTrue(h.is_running)

    def test_06_elapsed_time(self):
        """Test the `elapsed_time` attribut"""
        duration = datetime.timedelta(seconds=2)
        h = Hourglass(duration=duration)

        h.start()
        self.assertIsInstance(h.elapsed_time, datetime.timedelta)
        self.assertGreater(duration, h.elapsed_time)

    def test_07_compute(self):
        """Test the `compute` method"""
        duration = datetime.timedelta(seconds=2)
        h = Hourglass(duration=duration)
        with self.assertRaises(HourglassError):
            h.compute()
        h.start()
        self.assertIsInstance(h.compute(), bool)
        self.assertFalse(h.compute())
        time.sleep(2)
        self.assertTrue(h.compute())

    def test_08_stop(self):
        """Test the `stop` method"""
        h = Hourglass(duration=5)

        h.start()
        self.assertIsInstance(h.is_running, bool)
        self.assertTrue(h.is_running)

        h.stop()
        self.assertFalse(h.is_running)
