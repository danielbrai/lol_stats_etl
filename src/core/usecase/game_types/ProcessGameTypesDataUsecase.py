from src.core.usecase.game_types.RetrieveGameTypesInfoUsecase import RetrieveGameTypesInfoUsecase
from src.core.usecase.game_types.SaveGameTypesDataInDatabaseUsecase import SaveGameTypesDataInDatabaseUsecase


class ProcessGameTypesDataUsecase:

    def __init__(self, retrieve_game_types_data_usecase: RetrieveGameTypesInfoUsecase,
                 save_game_types_data_usecase: SaveGameTypesDataInDatabaseUsecase):
        self.retrieve_game_types_data_usecase = retrieve_game_types_data_usecase
        self.save_game_types_data_usecase = save_game_types_data_usecase

    def execute(self, ):
        game_types_json = self.retrieve_game_types_data_usecase.execute()
        self.save_game_types_data_usecase.execute(game_types_json)
