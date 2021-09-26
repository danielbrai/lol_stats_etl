from src.core.models.Team import Team
from src.core.models.League import League


class LeagueDtoDecoder:

    def parse_to_object(self, json):
        team_dto = []
        for team in json['teams']:
            team_dto.append(Team(name=team['team'], lineup=team['lineup']))
        return League(season=json['season'], split=json['split'], teams=team_dto)
