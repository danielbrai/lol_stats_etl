from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint


class RetrieveMatchesFromPlayerUseCase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self, quantity_of_matches: int):
        return self.dataprovider.get_matches_from_player(quantity_of_matches)

