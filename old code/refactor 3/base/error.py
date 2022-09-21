"""
    Base class implementation Error
"""

import abstract


class Error(abstract.Error):

    def __init__(self, message):
        super().__init__()
        self._message = message

    @property
    def message(self):
        return self.message

    def __str__(self):
        return self.message
