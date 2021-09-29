from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.constraints.FileConsumerConstraint import FileConsumerConstraint
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint
from src.core.usecase.maps.MapModel import MapModel
from src.core.usecase.queues.QueueModel import QueueModel


class RetrievePlatformInfoUsecase:

    def __init__(self, file_consumer: FileConsumerConstraint):
        self.file_consumer = file_consumer

    def execute(self):
        return self.file_consumer.load_platform_data_from_file_system()

