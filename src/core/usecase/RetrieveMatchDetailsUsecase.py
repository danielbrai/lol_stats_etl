from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint


class RetrieveMatchDetailsUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self, match_id):
        return self.dataprovider.get_match_details(match_id)
