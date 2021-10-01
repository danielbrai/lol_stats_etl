from src.core.constraints.FileConsumerConstraint import FileConsumerConstraint
from src.core.usecase.line_up.ChampionshipModel import ChampionshipModel


class RetrieveChampionshipInfoUseCase:

    def __init__(self, consumer: FileConsumerConstraint):
        self.consumer = consumer

    def execute(self) -> ChampionshipModel:
        return self.consumer.load_lineup_data_from_file_system()
