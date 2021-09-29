from src.core.constraints.FileConsumerConstraint import FileConsumerConstraint


class RetrieveLeagueInfoUsecase:

    def __init__(self, dataprovider: FileConsumerConstraint):
        self.dataprovider = dataprovider

    def execute(self, file_name):
        league_data = self.dataprovider.load_platform_data_from_file_system()
        return league_data
