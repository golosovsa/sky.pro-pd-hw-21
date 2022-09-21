"""
    Abstract class Task
"""

from abc import ABC, abstractmethod


class Task(ABC):

    @abstractmethod
    def get_performer(self):
        pass

    @abstractmethod
    def get_sender(self):
        pass

    @abstractmethod
    def get_recipient(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

    @abstractmethod
    def get_amount(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_progress(self):
        pass

    @abstractmethod
    def update(self):
        pass
