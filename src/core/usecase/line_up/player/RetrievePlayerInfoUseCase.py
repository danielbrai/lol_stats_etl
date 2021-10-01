from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint


class RetrievePlayerInfoUseCase:

    def __init__(self, rest_client: RiotRestClientConstraint):
        self.rest_client = rest_client

    def execute(self, player_name: str) -> str:
        return self.rest_client.get_user_puuid(player_name)
