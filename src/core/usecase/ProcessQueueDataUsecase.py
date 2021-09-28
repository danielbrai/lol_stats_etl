from src.core.usecase.RetrieveQueueInfoUsecase import RetrieveQueueInfoUsecase
from src.core.usecase.SaveQueueDataInDatabaseUsecase import SaveQueueDataInDatabaseUsecase


class ProcessQueueDataUsecase:

    def __init__(self, retrieve_queue_data_usecase: RetrieveQueueInfoUsecase,
                 save_queue_data_in_database_usecase: SaveQueueDataInDatabaseUsecase):
        self.retrieve_queue_data_usecase = retrieve_queue_data_usecase
        self.save_queue_data_in_database_usecase = save_queue_data_in_database_usecase

    def execute(self):
        champions_data = self.retrieve_queue_data_usecase.execute()
        self.save_queue_data_in_database_usecase.execute(champions_data)
