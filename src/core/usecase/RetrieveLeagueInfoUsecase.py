import os
from src.core.constraints.JsonConsumerConstarint import JsonConsumerConstraint


class RetrieveLeagueInfoUsecase:

    def __init__(self, dataprovider: JsonConsumerConstraint):
        self.dataprovider = dataprovider

    def execute(self, file_name):
        prop_path = f'{os.path.abspath(os.curdir)}/resources/{file_name}'
        league_data = self.dataprovider.load_data_from_file_system(prop_path)
        return league_data
