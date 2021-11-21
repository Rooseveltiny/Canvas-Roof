from abc import ABCMeta


class BaseException(Exception):
    __metaclass__ = ABCMeta
    message = "something went wrong!"

    def __init__(self):
        super().__init__(self.message)


class UpSideIsGreaterThanDownSide(BaseException):
    message = "up side is greater than down side. It should be smaller!"

class UpSideShouldBeMoreThan600mm(BaseException):
    message = "up side should be more than 600 mm!"

class SerializeError(BaseException):
    message = "Error during serializing"

class ItIsNotCoordinate(BaseException):
    message = "Looks like error in finding center of coordintates"
