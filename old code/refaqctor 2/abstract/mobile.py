"""
    Abstract class Mobile
"""

from abc import ABC, abstractmethod


class Mobile(ABC):

    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def calc_time(self, distance):
        pass

    @abstractmethod
    def calc_position(self, essence1, essence2, time):
        pass
