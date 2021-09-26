from src.core.usecase.RetrieveMapsInfoUsecase import RetrieveMapsInfoUsecase
from src.core.usecase.SaveMapsDataInDatabaseUsecase import SaveMapsDataInDatabaseUsecase


class ProcessMapsDataUsecase:

    def __init__(self, retrieve_maps_data_usecase: RetrieveMapsInfoUsecase,
                 save_maps_data_in_database_usecase: SaveMapsDataInDatabaseUsecase):
        self.retrieve_maps_data_usecase = retrieve_maps_data_usecase
        self.save_maps_data_in_database_usecase = save_maps_data_in_database_usecase

    def execute(self):
        champions_data = self.retrieve_maps_data_usecase.execute()
        self.save_maps_data_in_database_usecase.execute(champions_data)
