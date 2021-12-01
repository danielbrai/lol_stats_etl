from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.bans.BanModel import BanModel
from src.core.usecase.champions.ChampionModel import ChampionModel
from src.core.usecase.game_modes.GameModeModel import GameModeModel
from src.core.usecase.game_types.GameTypeModel import GameTypeModel
from src.core.usecase.items.ItemModel import ItemModel
from src.core.usecase.line_up.lineup.PlayerTeamModel import PlayerTeamModel
from src.core.usecase.line_up.matches.MatchPlayerDetailsModel import MatchPlayerDetailsModel
from src.core.usecase.line_up.player.PlayerModel import PlayerModel
from src.core.usecase.line_up.teams.TeamModel import TeamModel
from src.core.usecase.maps.MapModel import MapModel
from src.core.usecase.match_team_info.MatchTeamInfoModel import MatchTeamInfoModel
from src.core.usecase.matches_info.MatchInfoModel import MatchInfoModel
from src.core.usecase.objectives.ObjectiveModel import ObjectiveModel
from src.core.usecase.objectives_type.ObjectiveTypeModel import ObjectiveTypeModel
from src.core.usecase.platforms.PlatformModel import PlatformModel
from src.core.usecase.positions.PositionModel import PositionModel
from src.core.usecase.queues.QueueModel import QueueModel
from src.core.usecase.roles.RoleModel import RoleModel
from src.dataproviders.repository.MySqlCursor import MySqlCursor


class MySqlDatabaseRepository(DatabaseRepositoryConstraint):

    def get_team_id(self, team_name: str):
        pass

    def __init__(self, cursor: MySqlCursor):
        self.cursor = cursor

    def get_map_by_name(self, map_name: str):
        select_clause = 'SELECT maps.id, maps.name, maps.notes, maps.riot_map_id FROM lol_pro_players_stats.maps WHERE maps.name = %s ORDER BY maps.id DESC LIMIT 1'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(map_name,))
        return MapModel(id=result[0], name=result[1], notes=result[2], riot_map_id=result[3]) if result else None

    def save_champions_in_database(self, champions_data: List[ChampionModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.champions(id, name) VALUES (%(id)s, %(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=champions_data)

    def save_items_in_database(self, items_data: List[ItemModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.items (id, name) VALUES (%(id)s, %(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=items_data)

    def save_maps_in_database(self, map_info_data: List[MapModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.maps (riot_map_id, name, notes) VALUES (%(riot_map_id)s, %(name)s, %(notes)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=map_info_data)

    def save_queue_in_database(self, queue_data: List[QueueModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.queues (id, map_id, description, notes) VALUES (%(id)s, %(map_id)s, %(description)s, %(notes)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=queue_data)

    def save_game_modes_in_database(self, game_modes_data: List[GameModeModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.game_modes (mode) VALUES (%(mode)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=game_modes_data)

    def save_game_types_in_database(self, game_types_data: List[GameTypeModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.game_types (type, description) VALUES (%(type)s, %(description)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=game_types_data)

    def save_platform_in_database(self, platform_data: List[PlatformModel]):
        insert_clause = 'INSERT INTO lol_pro_players_stats.platforms (name) VALUES (%(name)s)'
        self.cursor.bulk_insert(insert_clause=insert_clause, insert_values_list=platform_data)

    def save_team_info_in_database(self, team: TeamModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.teams (name) VALUES (%(name)s)'
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=team)

    def get_team_by_name(self, team_name: str):
        select_clause = 'SELECT teams.id, teams.name FROM lol_pro_players_stats.teams WHERE teams.name = %s ORDER BY teams.id DESC LIMIT 1'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(team_name,))
        return TeamModel(id=result[0], name=result[1]) if result else None

    def save_player(self, player: PlayerModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.players (summoner_name, puuid) VALUES (%(summoner_name)s, %(puuid)s)'
        a = self.cursor.single_insert(insert_clause=insert_clause, insert_value=player)
        return a

    def save_team_player_info_in_database(self, player_team: PlayerTeamModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.lineup (player_id, team_id, season, split) VALUES (%(player_id)s, %(team_id)s, %(season)s, %(split)s)'
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=player_team)

    def get_players_puuid(self):
        select_clause = 'SELECT puuid FROM lol_pro_players_stats.players'
        return self.cursor.get_list(select_clause)

    def save_match_player_details(self, match_participants: MatchPlayerDetailsModel):
        insert_clause = '''
        INSERT INTO `lol_pro_players_stats`.`match_participants`
        (`id`,
        `champion_id`,
        `team_position_id`,
        `individual_position_id`,
        `role_id`,
        `team_id`,
        `player_id`,
        `assists`,
        `bount_level`,
        `champ_exp`,
        `consumables_purchased`,
        `demage_dealt_to_buildings`,
        `damage_dealt_to_objectives`,
        `damage_dealt_to_turrets`,
        `damage_self_mitigated`,
        `deaths`,
        `detector_wards_placed`,
        `double_kills`,
        `dragon_kills`,
        `first_blood_assist`,
        `first_blood_kill`,
        `first_tower_kill`,
        `gold_earned`,
        `gold_spent`,
        `inhibitor_kills`,
        `inhibitor_takedowns`,
        `inhibitor_lost`,
        `items_purchased`,
        `killing_sprees`,
        `kills`,
        `lane`,
        `largest_critical_strike`,
        `largest_killing_spree`,
        `largest_multi_kill`,
        `longest_time_spent_living`,
        `magic_damage_dealt`,
        `magic_damage_dealt_to_champions`,
        `magic_damage_taken`,
        `neutral_minions_killed`,
        `nexus_kills`,
        `nexus_takedowns`,
        `nexus_lost`,
        `objective_stolen`,
        `objective_stolen_assistis`,
        `penta_kills`,
        `physical_damage_dealt`,
        `physical_damage_dealt_to_champions`,
        `physical_damage_taken`,
        `quadra_kills`,
        `sight_wards_bought_in_game`,
        `team_early_surrendered`,
        `time_ccing_others`,
        `time_played`,
        `total_damage_dealt`,
        `total_damage_dealt_to_champions`,
        `total_damage_shielded_on_teammates`,
        `total_damage_taken`,
        `total_heal`,
        `total_heal_on_teammates`,
        `total_minions_killed`,
        `total_time_cc_dealt`,
        `total_time_spent_dead`,
        `total_units_healed`,
        `triple_kills`,
        `true_damage_dealt`,
        `true_damage_dealt_to_champions`,
        `true_damage_taken`,
        `turret_kills`,
        `turrets_takedowns`,
        `unreal_kills`,
        `vision_score`,
        `vision_wards_bought_in_game`,
        `wards_killed`,
        `wards_placed`)
        VALUES
        (
        %(id)s,
        %(champion_id)s,
        %(team_position_id)s,
        %(individual_position_id)s,
        %(role_id)s,
        %(team_id)s,
        %(player_id)s,
        %(assists)s,
        %(bount_level)s,
        %(champ_exp)s,
        %(consumables_purchased)s,
        %(demage_dealt_to_buildings)s,
        %(damage_dealt_to_objectives)s,
        %(damage_dealt_to_turrets)s,
        %(damage_self_mitigated)s,
        %(deaths)s,
        %(detector_wards_placed)s,
        %(double_kills)s,
        %(dragon_kills)s,
        %(first_blood_assist)s,
        %(first_blood_kill)s,
        %(first_tower_kill)s,
        %(gold_earned)s,
        %(gold_spent)s,
        %(inhibitor_kills)s,
        %(inhibitor_takedowns)s,
        %(inhibitor_lost)s,
        %(items_purchased)s,
        %(killing_sprees)s,
        %(kills)s,
        %(lane)s,
        %(largest_critical_strike)s,
        %(largest_killing_spree)s,
        %(largest_multi_kill)s,
        %(longest_time_spent_living)s,
        %(magic_damage_dealt)s,
        %(magic_damage_dealt_to_champions)s,
        %(magic_damage_taken)s,
        %(neutral_minions_killed)s,
        %(nexus_kills)s,
        %(nexus_takedowns)s,
        %(nexus_lost)s,
        %(objective_stolen)s,
        %(objective_stolen_assistis)s,
        %(penta_kills)s,
        %(physical_damage_dealt)s,
        %(physical_damage_dealt_to_champions)s,
        %(physical_damage_taken)s,
        %(quadra_kills)s,
        %(sight_wards_bought_in_game)s,
        %(team_early_surrendered)s,
        %(time_ccing_others)s,
        %(time_played)s,
        %(total_damage_dealt)s,
        %(total_damage_dealt_to_champions)s,
        %(total_damage_shielded_on_teammates)s,
        %(total_damage_taken)s,
        %(total_heal)s,
        %(total_heal_on_teammates)s,
        %(total_minions_killed)s,
        %(total_time_cc_dealt)s,
        %(total_time_spent_dead)s,
        %(total_units_healed)s,
        %(triple_kills)s,
        %(true_damage_dealt)s,
        %(true_damage_dealt_to_champions)s,
        %(true_damage_taken)s,
        %(turret_kills)s,
        %(turrets_takedowns)s,
        %(unreal_kills)s,
        %(vision_score)s,
        %(vision_wards_bought_in_game)s,
        %(wards_killed)s,
        %(wards_placed)s);
        '''
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=match_participants)

    def get_position_by_name(self, position_name: str):
        select_clause = 'SELECT positions.id, positions.position FROM lol_pro_players_stats.positions WHERE UPPER(lol_pro_players_stats.positions.position) = %s;'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(position_name,))
        return PositionModel(id=result[0], position=result[1]) if result else None

    def save_position_in_database(self, position_model: PositionModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.positions (position) VALUES (%(position)s)'
        a = self.cursor.single_insert(insert_clause=insert_clause, insert_value=position_model)
        return a

    def get_role_by_name(self, role: str):
        select_clause = 'SELECT roles.id, roles.role FROM lol_pro_players_stats.roles WHERE UPPER(lol_pro_players_stats.roles.role) = %s;'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(role,))
        return PositionModel(id=result[0], position=result[1]) if result else None

    def save_role_in_database(self, role_model: RoleModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.roles (role)  VALUES (%(role)s)'
        a = self.cursor.single_insert(insert_clause=insert_clause, insert_value=role_model)
        return a

    def get_objective_type_by_name(self, objective_name: str):
        select_clause = 'SELECT * FROM lol_pro_players_stats.objective_type WHERE UPPER(lol_pro_players_stats.objective_type.name) = %s;'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(objective_name,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def save_objective_type_in_database(self, objective_model: ObjectiveTypeModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.objective_type (name) VALUES (%(name)s)'
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=objective_model)

    def get_game_mode_type_by_name(self, game_mode):
        select_clause = 'SELECT * FROM lol_pro_players_stats.game_modes WHERE UPPER(lol_pro_players_stats.game_modes.mode) = %s;'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(game_mode,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def get_game_platform_by_name(self, platform_name: str):
        select_clause = 'SELECT * FROM lol_pro_players_stats.platforms WHERE UPPER(lol_pro_players_stats.platforms.name) = %s;'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(platform_name,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def get_game_type_by_name(self, game_type: str):
        select_clause = 'SELECT * FROM lol_pro_players_stats.game_types WHERE UPPER(lol_pro_players_stats.game_types.type) = %s;'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(game_type,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def get_queue_by_name(self, game_type: str):
        select_clause = 'SELECT * FROM lol_pro_players_stats.game_types WHERE UPPER(lol_pro_players_stats.game_types.type) = %s;'
        result = self.cursor.get_record(select_clause=select_clause, query_params=(game_type,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def save_match_info_in_database(self, match_info: MatchInfoModel):
        insert_clause = """
            INSERT INTO lol_pro_players_stats.matches_info
                (mode_id, type_id, creation, duration, start, game_patch, platform_id, queue_id)
            VALUES 
                (%(mode_id)s, %(type_id)s, %(creation)s, %(duration)s, %(start)s, %(game_patch)s, %(platform_id)s, %(queue_id)s)
            """
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=match_info)

    def save_match_team_info_in_database(self, match_team_info: MatchTeamInfoModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.matches_info_teams (match_info_id, team_id) VALUES (%(match_info_id)s, %(team_id)s)'
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=match_team_info)

    def save_objective_in_database(self, objective: ObjectiveModel):
        insert_clause = '''
            INSERT INTO 
                lol_pro_players_stats.objectives (first, kills, objective_type_id, match_info_team_id) 
            VALUES
                (%(first)s, %(kills)s, %(objective_type_id)s, %(match_info_team_id)s)
        '''
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=objective)

    def get_match_team_info_by_match_info_id_and_team_id(self, match_info_id: int, team_id: int):
        select_clause = '''
            SELECT matches_info_teams.id,
                matches_info_teams.match_info_id,
                matches_info_teams.team_id
            FROM lol_pro_players_stats.matches_info_teams
            WHERE
                matches_info_teams.match_info_id = %s
                AND
                matches_info_teams.team_id = %s;
        '''
        result = self.cursor.get_record(select_clause=select_clause, query_params=(match_info_id, team_id,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def save_ban_in_database(self, ban: BanModel):
        insert_clause = '''
           INSERT INTO 
                lol_pro_players_stats.team_bans (champion_id, match_info_team_id, pick_turn)
            VALUES
                (%(champion_id)s, %(match_info_team_id)s, %(pick_turn)s)
        '''
        return self.cursor.single_insert(insert_clause=insert_clause, insert_value=ban)

    def get_ban_info_by_champion_id_and_match_info_team_id(self, champion_id: int, match_info_team_id: int):
        select_clause = '''
            SELECT 
                team_bans.id,
                team_bans.champion_id,
                team_bans.match_info_team_id,
                team_bans.pick_turn
            FROM lol_pro_players_stats.team_bans
            WHERE
                team_bans.champion_id = %s
                AND
                team_bans.match_info_team_id = %s;
        '''
        result = self.cursor.get_record(select_clause=select_clause, query_params=(champion_id, match_info_team_id,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None
