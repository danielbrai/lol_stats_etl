from src.core.usecase.items.RetrieveItemsDataUsecase import RetrieveItemsDataUsecase
from src.core.usecase.items.SaveItemsDataInDatabaseUsecase import SaveItemsDataInDatabaseUsecase


class ProcessItemsDataUsecase:

    def __init__(self, retrieve_items_data_usecase: RetrieveItemsDataUsecase,
                 save_items_data_in_database_usecase: SaveItemsDataInDatabaseUsecase):
        self.retrieve_items_data_usecase = retrieve_items_data_usecase
        self.save_items_data_in_database_usecase = save_items_data_in_database_usecase

    def execute(self):
        champions_data = self.retrieve_items_data_usecase.execute()
        self.save_items_data_in_database_usecase.execute(champions_data)
