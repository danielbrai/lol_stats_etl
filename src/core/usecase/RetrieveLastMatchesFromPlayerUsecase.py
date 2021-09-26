from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint


class RetrieveLastMatchesFromPlayerUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self, puuid, desired_number_of_matches):
        return self.dataprovider.get_last_played_matches(puuid, desired_number_of_matches)