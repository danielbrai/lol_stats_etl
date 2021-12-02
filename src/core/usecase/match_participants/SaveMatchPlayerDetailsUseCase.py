from src.core.constraints import DatabaseRepositoryConstraint


class SaveMatchPlayerDetailsUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, match_id: int):
        response = self.repository.save_match_player_details(match_id)
        return response.json()

