from fastapi import HTTPException


class MutantException(Exception):
    """
    Exception raised for operations involved with Mutant.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class NotMutantException(HTTPException):
    """
    Exception raised for operations involved with Mutant.
    """

    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.status_code, detail=self.detail)


class CreateDnaSequenceException(Exception):
    """
    Exception raised for operations involved with DNA Sequence.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class GetAllDnaSequencesException(Exception):
    """
    Exception raised for operations involved with DNA Sequence.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class GetDNAVerificationStatisticsException(Exception):
    """
    Exception raised for operations involved with DNA Sequence statistics.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
