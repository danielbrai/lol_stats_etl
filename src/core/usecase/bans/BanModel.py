class BanModel:
    def __init__(self, id: int, champion_id: int, match_info_team_id: int, pick_turn: int):
        self.id = id
        self.champion_id = champion_id
        self.match_info_team_id = match_info_team_id
        self.pick_turn = pick_turn
