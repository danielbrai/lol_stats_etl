from src.core.usecase.platforms.RetrievePlatformInfoUsecase import RetrievePlatformInfoUsecase
from src.core.usecase.platforms.SavePlatformDataInDatabaseUsecase import SavePlatformDataInDatabaseUsecase


class ProcessPlatformDataUsecase:

    def __init__(self, retrieve_platform_data_usecase: RetrievePlatformInfoUsecase,
                 save_platform_data_in_database_usecase: SavePlatformDataInDatabaseUsecase):
        self.retrieve_platform_data_usecase = retrieve_platform_data_usecase
        self.save_platform_data_in_database_usecase = save_platform_data_in_database_usecase

    def execute(self):
        platform_data = self.retrieve_platform_data_usecase.execute()
        self.save_platform_data_in_database_usecase.execute(platform_data)
