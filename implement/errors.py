"""
    implementation of classes ...Error
"""


from .base import Error


class CreateEssenceError(Error):
    _module = "Create essence error"


class CreateRequestError(Error):
    _module = "Create request error"

