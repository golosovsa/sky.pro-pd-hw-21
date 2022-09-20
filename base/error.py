"""
    Base class implementation Error
"""

import abstract


class Error(abstract.error):

    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self.message

    def __str__(self):
        return self.message
