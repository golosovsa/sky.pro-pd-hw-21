"""
    Abstract class EssenceMixin
"""

from abc import ABC, abstractmethod


class Essence(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @staticmethod
    @abstractmethod
    def calc_distance(essence1, essence2):
        pass
