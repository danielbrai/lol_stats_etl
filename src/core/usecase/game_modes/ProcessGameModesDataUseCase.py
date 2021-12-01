from src.core.usecase.game_modes.RetrieveGameModesInfoUseCase import RetrieveGameModesInfoUseCase
from src.core.usecase.game_modes.SaveGameModesDataInDatabaseUseCase import SaveGameModesDataInDatabaseUseCase


class ProcessGameModesDataUseCase:

    def __init__(self, retrieve_game_mode_info_usecase: RetrieveGameModesInfoUseCase,
                 save_game_mode_info_usecase: SaveGameModesDataInDatabaseUseCase):
        self.retrieve_game_mode_info_usecase = retrieve_game_mode_info_usecase
        self.save_game_mode_info_usecase = save_game_mode_info_usecase

    def execute(self, ):
        test_json = self.retrieve_game_mode_info_usecase.execute()
        self.save_game_mode_info_usecase.execute(test_json)
