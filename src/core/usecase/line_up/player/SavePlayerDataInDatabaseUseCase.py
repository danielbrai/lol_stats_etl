from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.line_up.player.PlayerModel import PlayerModel
from src.core.usecase.line_up.player.RetrievePlayerInfoUseCase import RetrievePlayerInfoUseCase


class SavePlayerDataInDatabaseUseCase:

    def __init__(self, repository: DatabaseRepositoryConstraint,
                 retrieve_player_info_use_case: RetrievePlayerInfoUseCase, ):
        self.retrieve_player_info_use_case = retrieve_player_info_use_case
        self.repository = repository

    def execute(self, player: PlayerModel):
        player.puuid = self.retrieve_player_info_use_case.execute(player.summoner_name)

        if player.puuid:
            player.id = self.repository.save_player(player)

        return player
