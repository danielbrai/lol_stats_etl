from src.core.usecase.line_up.ChampionshipModel import ChampionshipModel
from src.core.usecase.line_up.TeamLineUpModel import TeamLineUpModel
from src.core.usecase.line_up.player.PlayerModel import PlayerModel
from src.core.usecase.line_up.teams.TeamModel import TeamModel


class LineUpDtoDecoder:

    def parse_to_object(self, cblol_teams) -> ChampionshipModel:
        championship = ChampionshipModel(season=None, split=None, line_up=[])
        championship.season = cblol_teams['season']
        championship.split = cblol_teams['split']
        for team in cblol_teams['teams']:
            team_model = TeamModel(id=None, name=team['team'])
            players = list(PlayerModel(id=None, name=player, puuid=None) for player in team['lineup'])
            championship.line_up.append(TeamLineUpModel(team=team_model, lineup=players))
        return championship
