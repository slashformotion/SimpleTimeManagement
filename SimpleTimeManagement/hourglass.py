import datetime
from typing import Union


class HourglassError(Exception):
    """A custom exception used to report errors in use of Hourglass class."""


class Hourglass:
    def __init__(self, duration: Union[int, datetime.timedelta], name: str = ""):
        """Hourglass initializer

        :param duration: it's explicit)
        :type duration: datetime.timedelta or a positive integer (in seconds)
        :param name: An optional name if you need it, defaults to ''
        :type name: str, optional
        """
        self.__start_time = None
        self.__name = name
        if isinstance(duration, datetime.timedelta):
            self.__duration = duration
        elif isinstance(duration, float):
            raise NotImplementedError(
                "SimpleTimeManagement only support integers (as seconds) or datetime.timedelta for the 'duration' arg for the moment."
            )
        elif duration <= 0:
            raise ValueError("Duration can't be negative or null.")
        else:
            self.__duration = datetime.timedelta(seconds=duration)

    def start(self) -> None:
        """Start the timer"""
        if self.__start_time is not None:
            raise HourglassError(
                f"Hourglass is already running. Use the .stop() method to stop it."
            )
        self.__start_time = datetime.datetime.now()

    def compute(self, debug: bool = False) -> bool:
        """Compute and report the elapsed time

        :param debug: if True print the elapsed time to stdout, defaults to False
        :type debug: bool, optional
        :raises HourglassError: A custom exception used to report errors in use of Hourglass class.
        :return: True if the time is up
        :rtype: bool
        """
        if self.__start_time is None:
            raise HourglassError(
                f"Hourglass is not running. Use the .start() method to start it."
            )

        if debug:
            print(f"Elapsed time: {self.elapsed_time}. (name: {self._name})")
        return self.elapsed_time > self.__duration

    def stop(self):
        """Stop the Hourglass."""
        self.__start_time = None

    def reset(self):
        self.stop()
        self.start()

    @property
    def elapsed_time(self):
        if self.__start_time is None:
            raise HourglassError(
                f"Hourglass is not running. Use the .start() method to start it."
            )

        elapsed_time = datetime.datetime.now() - self.__start_time
        return elapsed_time

    @property
    def is_running(self):
        """Says if the hourglass has run out

        :return: [description]
        :rtype: [type]
        """
        return not self.__start_time == None
