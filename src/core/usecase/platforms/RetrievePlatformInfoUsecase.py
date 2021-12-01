from src.core.constraints.FileConsumerConstraint import FileConsumerConstraint


class RetrievePlatformInfoUsecase:

    def __init__(self, file_consumer: FileConsumerConstraint):
        self.file_consumer = file_consumer

    def execute(self):
        return self.file_consumer.load_platform_data_from_file_system()

