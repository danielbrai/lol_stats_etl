from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint


class RetrieveUserDataUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self, username):
        return self.dataprovider.get_user_data(username)
