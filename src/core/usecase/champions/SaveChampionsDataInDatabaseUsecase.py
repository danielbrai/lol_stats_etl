from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.champions.ChampionModel import ChampionModel
from src.core.usecase.champions.GetChampionByRiotIdUseCase import GetChampionByRiotIdUseCase


class SaveChampionsDataInDatabaseUsecase:

    def __init__(self, repository: DatabaseRepositoryConstraint, get_champion_by_riot_id_id_use_case: GetChampionByRiotIdUseCase):
        self.repository = repository
        self.get_champion_by_riot_id_id_use_case = get_champion_by_riot_id_id_use_case

    def execute(self, champion_data: ChampionModel):

        saved_champion = self.get_champion_by_riot_id_id_use_case.execute(champion_data.riot_id)

        if saved_champion:
            return saved_champion.id
        else:
            return self.repository.save_champions_in_database(champion_data)
