from app.dependencies_factory.use_cases.mutant import detect_mutant_use_case
from app.src.cases.detect_mutant._detect_mutant_use_case import DetectMutantUseCase


class TestDetectMutantUseCaseFactory:
    def test_create_detect_mutant_use_case(self):
        use_case = detect_mutant_use_case()

        assert isinstance(use_case, DetectMutantUseCase)
