from app.src.domain.repositories import DetectMutantRepository
from app.src.exceptions import MutantException, NotMutantException

from ._request import DetectMutantRequest
from ._response import DetectMutantResponse


class DetectMutantUseCase:
    def __init__(self, detect_mutant_repository: DetectMutantRepository) -> None:
        self.detect_mutant_repository = detect_mutant_repository

    async def __call__(self, request: DetectMutantRequest) -> DetectMutantResponse:
        try:
            is_mutant = self._is_mutant(request.dna)
            await self.detect_mutant_repository.save_sequence(request.dna, is_mutant)

            if not is_mutant:
                raise NotMutantException(status_code=403, detail="DNA is not mutant")

            return DetectMutantResponse(is_mutant=is_mutant)

        except MutantException as exception:
            raise MutantException(f"An error occurred while detecting mutant: {str(exception)}")

    def _is_mutant(self, dna: list[str]) -> bool:
        all_letter_combinations = self._get_all_letter_combinations(dna)
        valid_combinations = self._get_valid_letter_combinations(all_letter_combinations)
        sequences_to_check = list(
            filter(
                lambda combination: self._has_more_than_four_repeated_letters(combination),
                valid_combinations,
            )
        )
        is_mutant = len(sequences_to_check) > 1
        return is_mutant

    def _generate_dna_matrix(self, dna: list[str]) -> list:
        return [list(sequence) for sequence in dna]

    def _generate_vertical_combinations(self, matrix: list) -> list:
        return ["".join(row[i] for row in matrix) for i in range(len(matrix))]

    def _generate_dna_reverse_matrix(self, dna: list[str]) -> list:
        return [sequence[::-1] for sequence in dna]

    def _get_main_diagonal_combination(self, matrix: list) -> str:
        diagonal = ""
        for i in range(len(matrix)):
            diagonal += matrix[i][i]
        return diagonal

    def _get_secondary_diagonals_combinations(
        self, matrix: list, generate_superior_diagonal: bool = True
    ) -> list:
        diagonals = []
        matrix_size = len(matrix)
        for start in range(matrix_size - 1):
            diagonal = ""
            for j in range(start + 1, matrix_size):
                if generate_superior_diagonal:
                    diagonal += matrix[j - start - 1][j]
                else:
                    diagonal += matrix[j][j - start - 1]
            diagonals.append(diagonal)
        return diagonals

    def _get_valid_letter_combinations(self, combinations: list[str]) -> list:
        return list(filter(lambda combination: len(combination) >= 4, combinations))

    def _get_all_letter_combinations(self, dna: list[str]) -> list:
        matrix = self._generate_dna_matrix(dna)
        reverse_matrix = self._generate_dna_reverse_matrix(dna)

        vertical_combinations = self._generate_vertical_combinations(matrix)

        main_diagonal_combination = self._get_main_diagonal_combination(matrix)
        secondary_diagonal_combinations = self._get_secondary_diagonals_combinations(matrix)
        secondary_lower_diagonal_combinations = self._get_secondary_diagonals_combinations(
            matrix, False
        )

        main_reverse_diagonal_combination = self._get_main_diagonal_combination(reverse_matrix)
        secondary_reverse_diagonal_combinations = self._get_secondary_diagonals_combinations(
            reverse_matrix
        )
        secondary_reverse_lower_diagonal_combinations = self._get_secondary_diagonals_combinations(
            reverse_matrix, False
        )

        return [
            *dna,
            *vertical_combinations,
            main_diagonal_combination,
            *secondary_diagonal_combinations,
            *secondary_lower_diagonal_combinations,
            main_reverse_diagonal_combination,
            *secondary_reverse_diagonal_combinations,
            *secondary_reverse_lower_diagonal_combinations,
        ]

    def _has_more_than_four_repeated_letters(self, combination: str) -> bool:
        letters = 1
        for i in range(1, len(combination)):
            if combination[i] == combination[i - 1]:
                letters += 1
                if letters == 4:
                    return True
            else:
                letters = 1
        return False
