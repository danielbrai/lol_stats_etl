from src.core.usecase.game_modes.RetrieveGameModesInfoUsecase import RetrieveGameModesInfoUsecase
from src.core.usecase.game_modes.SaveGameModesDataInDatabaseUsecase import SaveGameModesDataInDatabaseUsecase


class ProcessGameModesDataUsecase:

    def __init__(self, retrieve_game_mode_info_usecase: RetrieveGameModesInfoUsecase,
                 save_game_mode_info_usecase: SaveGameModesDataInDatabaseUsecase):
        self.retrieve_game_mode_info_usecase = retrieve_game_mode_info_usecase
        self.save_game_mode_info_usecase = save_game_mode_info_usecase

    def execute(self, ):
        test_json = self.retrieve_game_mode_info_usecase.execute()
        self.save_game_mode_info_usecase.execute(test_json)
