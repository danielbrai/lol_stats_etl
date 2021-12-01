from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint


class RetrieveMatchIdsFromUserPuuidUseCase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self, puuid: str, desired_number_of_matches: int):
        response = self.dataprovider.get_last_played_matches(puuid, desired_number_of_matches)
        return response.json()
