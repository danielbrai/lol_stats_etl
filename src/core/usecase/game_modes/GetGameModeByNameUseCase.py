from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint


class GetGameModeByNameUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint):
        self.repository = repository

    def execute(self, game_mode: str):
        return self.repository.get_game_mode_type_by_name(game_mode)

