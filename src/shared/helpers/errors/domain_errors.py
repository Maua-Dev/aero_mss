from src.shared.helpers.errors.base_error import BaseError

class EntityError(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is not valid')

class XcgError(EntityError):
    def __init__(self, xcg: float):
        if xcg is None:
            super().__init__('Field xcg is None')
        elif type(xcg) != float:
            super().__init__('Field xcg is not float')
        elif xcg > 1:
            super().__init__('Field xcg is greater than 1')
        elif xcg < -1:
            super().__init__('Field xcg is less than -1')
        else:
            super().__init__('Field xcg is not valid')

class XacWerror(EntityError):
    def __init__(self, xac_w: float):
        if xac_w is None:
            super().__init__('Field xac_w is None')
        elif type(xac_w) != float:
            super().__init__('Field xac_w is not float')
        elif xac_w <= 0:
            super().__init__('Field xac_w is less than -1')
        else:
            super().__init__('Field xac_w is not valid')

class SwError(EntityError):
    def __init__(self, sw: float):
        if sw is None:
            super().__init__('Field sw is None')
        elif type(sw) != float:
            super().__init__('Field sw is not float')
        elif sw <= 0:
            super().__init__('Field sw is less than or equal to 0')
        else:
            super().__init__('Field sw is not valid')

class StError(EntityError):
    def __init__(self, st: float):
        if st is None:
            super().__init__('Field st is None')
        elif type(st) != float:
            super().__init__('Field st is not float')
        elif st <= 0:
            super().__init__('Field st is less than or equal to 0')
        else:
            super().__init__('Field st is not valid')

class CwError(EntityError):
    def __init__(self, cw: float):
        if cw is None:
            super().__init__('Field cw is None')
        elif type(cw) != float:
            super().__init__('Field cw is not float')
        elif cw <= 0:
            super().__init__('Field cw is less than or equal to 0')
        else:
            super().__init__('Field cw is not valid')

class CtError(EntityError):
    def __init__(self, ct: float):
        if ct is None:
            super().__init__('Field ct is None')
        elif type(ct) != float:
            super().__init__('Field ct is not float')
        elif ct <= 0:
            super().__init__('Field ct is less than or equal to 0')
        else:
            super().__init__('Field ct is not valid')

class IwError(EntityError):
    def __init__(self, iw: float):
        if iw is None:
            super().__init__('Field iw is None')
        elif type(iw) != float:
            super().__init__('Field iw is not float')
        else:
            super().__init__('Field iw is not valid')

class ItError(EntityError):
    def __init__(self, it: float):
        if it is None:
            super().__init__('Field it is None')
        elif type(it) != float:
            super().__init__('Field it is not float')
        else:
            super().__init__('Field it is not valid')

class LtError(EntityError):
    def __init__(self, lt: float):
        if lt is None:
            super().__init__('Field lt is None')
        elif type(lt) != float:
            super().__init__('Field lt is not float')
        elif lt < 0:
            super().__init__('Field lt is less than 0')
        else:
            super().__init__('Field lt is not valid')

class CmAcError(EntityError):
    def __init__(self, cm_ac: float):
        if cm_ac is None:
            super().__init__('Field cm_ac is None')
        elif type(cm_ac) != float:
            super().__init__('Field cm_ac is not float')
        elif cm_ac < -1:
            super().__init__('Field cm_ac is less than -1')
        elif cm_ac > 1:
            super().__init__('Field cm_ac is greater than 1')
        else:
            super().__init__('Field cm_ac is not valid')

class Cl0Error(EntityError):
    def __init__(self, cl_0: float):
        if cl_0 is None:
            super().__init__('Field cl_0 is None')
        elif type(cl_0) != float:
            super().__init__('Field cl_0 is not float')
        elif cl_0 < 0:
            super().__init__('Field cl_0 is less than 0')
        else:
            super().__init__('Field cl_0 is not valid')

class ClAlphaError(EntityError):
    def __init__(self, cl_alpha: float):
        if cl_alpha is None:
            super().__init__('Field cl_alpha is None')
        elif type(cl_alpha) != float:
            super().__init__('Field cl_alpha is not float')
        elif cl_alpha < 0:
            super().__init__('Field cl_alpha is less than 0')
        else:
            super().__init__('Field cl_alpha is not valid')


class EntityParameterTypeError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message

class EntityParameterError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message
