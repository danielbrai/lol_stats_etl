from src.core.usecase.TeamModel import TeamModel
from src.core.usecase.LeagueModel import LeagueModel


class LeagueDtoDecoder:

    def parse_to_object(self, json):
        team_dto = []
        for team in json['teams']:
            team_dto.append(TeamModel(name=team['team'], lineup=team['lineup']))
        return LeagueModel(season=json['season'], split=json['split'], teams=team_dto)
