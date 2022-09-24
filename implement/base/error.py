"""
    Base implementation class Error
"""


class Error(Exception):
    _module = "Base"

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return f"{self._module}. {self._message}."
