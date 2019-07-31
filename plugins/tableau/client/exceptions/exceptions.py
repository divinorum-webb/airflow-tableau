class BaseError(Exception):
    """Base class for additional exceptions"""
    pass


class InvalidParameter(BaseError):
    """Raised when an invalid set of parameters are passed to an Endpoint or Request class"""
    pass


class InvalidWorkbookType(BaseError):
    """Raised when attempting to call publish_workbook() with an invalid file type (valid types are twbx or twb)"""
    pass
