class NotFoundError(Exception):
    def __init__(self, message: str):
        self.message = message

class UniqueKeyError(Exception):
    def __init__(self, message: str):
        self.message = message

