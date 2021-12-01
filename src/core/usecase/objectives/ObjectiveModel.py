class ObjectiveModel:

    def __init__(self, id: int, first: int, kills: int, objective_type_id: int, match_info_team_id: int):
        self.id = id
        self.first = first
        self.kills = kills
        self.objective_type_id = objective_type_id
        self.match_info_team_id = match_info_team_id
