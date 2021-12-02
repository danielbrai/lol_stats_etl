from src.core.usecase.champions.RetrieveChampionsDataUsecase import RetrieveChampionsDataUsecase
from src.core.usecase.champions.SaveChampionsDataInDatabaseUsecase import SaveChampionsDataInDatabaseUsecase


class ProcessChampionsDataUsecase:

    def __init__(self, retrieve_champions_data_usecase: RetrieveChampionsDataUsecase,
                 save_champions_data_in_database_usecase: SaveChampionsDataInDatabaseUsecase,):
        self.retrieve_champions_data_usecase = retrieve_champions_data_usecase
        self.save_champions_data_in_database_usecase = save_champions_data_in_database_usecase

    def execute(self):
        champions_data_list = self.retrieve_champions_data_usecase.execute()

        for champion_data in champions_data_list:
            self.save_champions_data_in_database_usecase.execute(champion_data)
