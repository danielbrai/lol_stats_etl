from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.usecase.bans.BanModel import BanModel
from src.core.usecase.champions.ChampionModel import ChampionModel
from src.core.usecase.game_modes.GameModeModel import GameModeModel
from src.core.usecase.game_types.GameTypeModel import GameTypeModel
from src.core.usecase.items.ItemModel import ItemModel
from src.core.usecase.line_up.lineup.PlayerTeamModel import PlayerTeamModel
from src.core.usecase.line_up.player.PlayerModel import PlayerModel
from src.core.usecase.line_up.teams.TeamModel import TeamModel
from src.core.usecase.maps.MapModel import MapModel
from src.core.usecase.match_participants.MatchPlayerDetailsModel import MatchPlayerDetailsModel
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

    def save_champions_in_database(self, champions_data: ChampionModel):
        insert_clause = 'INSERT INTO lol_pro_players_stats.champions(name, riot_id) VALUES (%(name)s, %(riot_id)s)'
        self.cursor.single_insert(insert_clause=insert_clause, insert_value=champions_data)

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
        INSERT INTO lol_pro_players_stats.match_participants
        (
            champion_id,
            team_position_id,
            individual_position_id,
            role_id,
            match_info_team_id,
            player_id,
            assists,
            bount_level,
            champ_exp,
            consumables_purchased,
            damage_dealt_to_buildings,
            damage_dealt_to_objectives,
            damage_dealt_to_turrets,
            damage_self_mitigated,
            deaths,
            detector_wards_placed,
            double_kills,
            dragon_kills,
            first_blood_assist,
            first_blood_kill,
            first_tower_kill,
            gold_earned,
            gold_spent,
            inhibitor_kills,
            inhibitor_takedowns,
            inhibitor_lost,
            items_purchased,
            killing_sprees,
            kills,
            lane,
            largest_critical_strike,
            largest_killing_spree,
            largest_multi_kill,
            longest_time_spent_living,
            magic_damage_dealt,
            magic_damage_dealt_to_champions,
            magic_damage_taken,
            neutral_minions_killed,
            nexus_kills,
            nexus_takedowns,
            nexus_lost,
            objective_stolen,
            objective_stolen_assistis,
            penta_kills,
            physical_damage_dealt,
            physical_damage_dealt_to_champions,
            physical_damage_taken,
            quadra_kills,
            sight_wards_bought_in_game,
            team_early_surrendered,
            time_ccing_others,
            time_played,
            total_damage_dealt,
            total_damage_dealt_to_champions,
            total_damage_shielded_on_teammates,
            total_damage_taken,
            total_heal,
            total_heal_on_teammates,
            total_minions_killed,
            total_time_cc_dealt,
            total_time_spent_dead,
            total_units_healed,
            triple_kills,
            true_damage_dealt,
            true_damage_dealt_to_champions,
            true_damage_taken,
            turret_kills,
            turrets_takedowns,
            unreal_kills,
            vision_score,
            vision_wards_bought_in_game,
            wards_killed,
            wards_placed,
            champion_level,
            first_tower_assist,
            turrets_lost)
            VALUES
            (
            %(champion_id)s,
            %(team_position_id)s,
            %(individual_position_id)s,
            %(role_id)s,
            %(match_info_team_id)s,
            %(player_id)s,
            %(assists)s,
            %(bount_level)s,
            %(champ_exp)s,
            %(consumables_purchased)s,
            %(damage_dealt_to_buildings)s,
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
            %(wards_placed)s,
            %(champion_level)s,
            %(first_tower_assist)s,
            %(turrets_lost)s
        );
        '''
        a = self.cursor.single_insert(insert_clause=insert_clause, insert_value=match_participants)
        return a

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

    def get_player_by_summoner_name(self, summoner_name: str):
        select_clause = '''
            SELECT players.id,
                players.summoner_name,
                players.puuid
            FROM lol_pro_players_stats.players 
            WHERE
                players.summoner_name = %s;
        '''
        result = self.cursor.get_record(select_clause=select_clause, query_params=(summoner_name,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def get_objective_by_objective_type_id_and_match_info_team_id(self, objective_type: int, match_info_team_id: int):
        select_clause = '''
        SELECT 
            objectives.id,
            objectives.first,
            objectives.kills,
            objectives.objective_type_id,
            objectives.match_info_team_id
        FROM 
            lol_pro_players_stats.objectives
        WHERE 
            lol_pro_players_stats.objectives.objective_type_id = %s
            AND
            lol_pro_players_stats.objectives.match_info_team_id = %s
        '''
        result = self.cursor.get_record(select_clause=select_clause, query_params=(objective_type, match_info_team_id,))
        return ObjectiveTypeModel(id=result[0], name=result[1]) if result else None

    def get_match_participant_by_relations_ids(self, champion_id: int, team_position_id: int, individual_position_id: int, role_id: int, match_info_team_id: int, player_id: int):
        select_clause = '''
        SELECT match_participants.id,
            match_participants.champion_id,
            match_participants.team_position_id,
            match_participants.individual_position_id,
            match_participants.role_id,
            match_participants.match_info_team_id,
            match_participants.player_id,
            match_participants.assists,
            match_participants.bount_level,
            match_participants.champ_exp,
            match_participants.consumables_purchased,
            match_participants.damage_dealt_to_buildings,
            match_participants.damage_dealt_to_objectives,
            match_participants.damage_dealt_to_turrets,
            match_participants.damage_self_mitigated,
            match_participants.deaths,
            match_participants.detector_wards_placed,
            match_participants.double_kills,
            match_participants.dragon_kills,
            match_participants.first_blood_assist,
            match_participants.first_blood_kill,
            match_participants.first_tower_kill,
            match_participants.gold_earned,
            match_participants.gold_spent,
            match_participants.inhibitor_kills,
            match_participants.inhibitor_takedowns,
            match_participants.inhibitor_lost,
            match_participants.items_purchased,
            match_participants.killing_sprees,
            match_participants.kills,
            match_participants.lane,
            match_participants.largest_critical_strike,
            match_participants.largest_killing_spree,
            match_participants.largest_multi_kill,
            match_participants.longest_time_spent_living,
            match_participants.magic_damage_dealt,
            match_participants.magic_damage_dealt_to_champions,
            match_participants.magic_damage_taken,
            match_participants.neutral_minions_killed,
            match_participants.nexus_kills,
            match_participants.nexus_takedowns,
            match_participants.nexus_lost,
            match_participants.objective_stolen,
            match_participants.objective_stolen_assistis,
            match_participants.penta_kills,
            match_participants.physical_damage_dealt,
            match_participants.physical_damage_dealt_to_champions,
            match_participants.physical_damage_taken,
            match_participants.quadra_kills,
            match_participants.sight_wards_bought_in_game,
            match_participants.team_early_surrendered,
            match_participants.time_ccing_others,
            match_participants.time_played,
            match_participants.total_damage_dealt,
            match_participants.total_damage_dealt_to_champions,
            match_participants.total_damage_shielded_on_teammates,
            match_participants.total_damage_taken,
            match_participants.total_heal,
            match_participants.total_heal_on_teammates,
            match_participants.total_minions_killed,
            match_participants.total_time_cc_dealt,
            match_participants.total_time_spent_dead,
            match_participants.total_units_healed,
            match_participants.triple_kills,
            match_participants.true_damage_dealt,
            match_participants.true_damage_dealt_to_champions,
            match_participants.true_damage_taken,
            match_participants.turret_kills,
            match_participants.turrets_takedowns,
            match_participants.unreal_kills,
            match_participants.vision_score,
            match_participants.vision_wards_bought_in_game,
            match_participants.wards_killed,
            match_participants.wards_placed,
            match_participants.champion_level,
            match_participants.first_tower_assist,
            match_participants.turrets_lost
        FROM 
            lol_pro_players_stats.match_participants 
        WHERE 
            match_participants.champion_id = %s
        AND
            match_participants.team_position_id = %s
        AND
            match_participants.individual_position_id = %s
        AND
            match_participants.role_id = %s
        AND
            match_participants.match_info_team_id = %s
        AND
            match_participants.player_id = %s
        '''
        result = self.cursor.get_record(select_clause=select_clause, query_params=(champion_id, team_position_id, individual_position_id, role_id, match_info_team_id, player_id,))
        print('')
        return MatchPlayerDetailsModel(
            id=result[0],
            champion_id=result[1],
            team_position_id=result[2],
            individual_position_id=result[3],
            role_id=result[4],
            match_info_team_id=result[5],
            player_id=result[6],
            assists=result[7],
            bount_level=result[8],
            champ_exp=result[9],
            consumables_purchased=result[10],
            damage_dealt_to_buildings=result[11],
            damage_dealt_to_objectives=result[12],
            damage_dealt_to_turrets=result[13],
            damage_self_mitigated=result[14],
            deaths=result[15],
            detector_wards_placed=result[16],
            double_kills=result[17],
            dragon_kills=result[18],
            first_blood_assist=result[19],
            first_blood_kill=result[20],
            first_tower_kill=result[21],
            gold_earned=result[22],
            gold_spent=result[23],
            inhibitor_kills=result[24],
            inhibitor_takedowns=result[25],
            inhibitor_lost=result[26],
            items_purchased=result[27],
            killing_sprees=result[28],
            kills=result[29],
            lane=result[30],
            largest_critical_strike=result[31],
            largest_killing_spree=result[32],
            largest_multi_kill=result[33],
            longest_time_spent_living=result[34],
            magic_damage_dealt=result[35],
            magic_damage_dealt_to_champions=result[36],
            magic_damage_taken=result[37],
            neutral_minions_killed=result[38],
            nexus_kills=result[39],
            nexus_takedowns=result[40],
            nexus_lost=result[41],
            objective_stolen=result[42],
            objective_stolen_assistis=result[43],
            penta_kills=result[44],
            physical_damage_dealt=result[45],
            physical_damage_dealt_to_champions=result[46],
            physical_damage_taken=result[47],
            quadra_kills=result[48],
            sight_wards_bought_in_game=result[49],
            team_early_surrendered=result[50],
            time_ccing_others=result[51],
            time_played=result[52],
            total_damage_dealt=result[53],
            total_damage_dealt_to_champions=result[54],
            total_damage_shielded_on_teammates=result[55],
            total_damage_taken=result[56],
            total_heal=result[57],
            total_heal_on_teammates=result[58],
            total_minions_killed=result[59],
            total_time_cc_dealt=result[60],
            total_time_spent_dead=result[61],
            total_units_healed=result[62],
            triple_kills=result[63],
            true_damage_dealt=result[64],
            true_damage_dealt_to_champions=result[65],
            true_damage_taken=result[66],
            turret_kills=result[67],
            turrets_takedowns=result[68],
            unreal_kills=result[69],
            vision_score=result[70],
            vision_wards_bought_in_game=result[71],
            wards_killed=result[72],
            wards_placed=result[73],
            champion_level=result[74],
            first_tower_assist=result[75],
            turrets_lost=result[76]
        ) if result else None

    def get_champion_by_riot_id(self, riot_id: str):
        select_clause = '''
            SELECT champions.id,
                champions.name,
                champions.riot_id
            FROM lol_pro_players_stats.champions
            WHERE 
                lol_pro_players_stats.champions.riot_id = %s
                
        '''
        result = self.cursor.get_record(select_clause=select_clause, query_params=(riot_id,))
        return ChampionModel(id=result[0], name=result[1], riot_id=result[2]) if result else None
