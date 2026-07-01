from src.shared.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is missing')
class WrongTypeParameter(BaseError):
    def __init__(self, fieldName: str, fieldTypeExpected: str, fieldTypeReceived: str):
        super().__init__(f'Field {fieldName} isn\'t in the right type.\n Received: {fieldTypeReceived}.\n Expected: {fieldTypeExpected}')
    
class EmptyUpdate(BaseError):
    def __init__(self):
        super().__init__(f'Empty update request. Update did not fail, but no data was provided to update, so nothing changed')