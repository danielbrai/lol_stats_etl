from src.core.usecase.bans.BanModel import BanModel
from src.core.usecase.bans.GetBanInfoByChampionIdAndMatchInfoTeamIdFromDatabaseUseCase import \
    GetBanInfoByChampionIdAndMatchInfoTeamIdFromDatabaseUseCase
from src.core.usecase.bans.SaveBanInDatabaseUseCase import SaveBanInDatabaseUseCase
from src.core.usecase.champions.GetChampionByRiotIdUseCase import GetChampionByRiotIdUseCase
from src.core.usecase.champions.ProcessChampionsDataUsecase import ProcessChampionsDataUsecase
from src.core.usecase.champions.RetrieveChampionsDataUsecase import RetrieveChampionsDataUsecase
from src.core.usecase.champions.SaveChampionsDataInDatabaseUsecase import SaveChampionsDataInDatabaseUsecase
from src.core.usecase.game_modes.GetGameModeByNameUseCase import GetGameModeByNameUseCase
from src.core.usecase.game_modes.ProcessGameModesDataUseCase import ProcessGameModesDataUseCase
from src.core.usecase.game_modes.RetrieveGameModesInfoUseCase import RetrieveGameModesInfoUseCase
from src.core.usecase.game_modes.SaveGameModesDataInDatabaseUseCase import SaveGameModesDataInDatabaseUseCase
from src.core.usecase.game_types.GetGameTypeByNameUseCase import GetGameTypeByNameUseCase
from src.core.usecase.game_types.ProcessGameTypesDataUsecase import ProcessGameTypesDataUsecase
from src.core.usecase.game_types.RetrieveGameTypesInfoUsecase import RetrieveGameTypesInfoUsecase
from src.core.usecase.game_types.SaveGameTypesDataInDatabaseUsecase import SaveGameTypesDataInDatabaseUsecase
from src.core.usecase.items.ProcessItemsDataUsecase import ProcessItemsDataUsecase
from src.core.usecase.items.RetrieveItemsDataUsecase import RetrieveItemsDataUsecase
from src.core.usecase.items.SaveItemsDataInDatabaseUsecase import SaveItemsDataInDatabaseUsecase
from src.core.usecase.line_up.ProcessLineUpDataUseCase import ProcessLineUpDataUseCase
from src.core.usecase.line_up.RetrieveChampionshipInfoUseCase import RetrieveChampionshipInfoUseCase
from src.core.usecase.line_up.lineup.SavePlayerTeamInfoInDatabaseUseCase import SavePlayerTeamInfoInDatabaseUseCase
from src.core.usecase.line_up.player.GetPlayerBySummonerNameUseCase import GetPlayerBySummonerNameUseCase
from src.core.usecase.line_up.player.GetPlayersPuuidFromDatabaseUseCase import GetPlayersPuuidFromDatabaseUseCase
from src.core.usecase.line_up.player.RetrievePlayerInfoUseCase import RetrievePlayerInfoUseCase
from src.core.usecase.line_up.player.SavePlayerDataInDatabaseUseCase import SavePlayerDataInDatabaseUseCase
from src.core.usecase.line_up.teams.GetTeamByNameUseCase import GetTeamByNameUseCase
from src.core.usecase.line_up.teams.SaveTeamDataInDatabaseUseCase import SaveTeamDataInDatabaseUseCase
from src.core.usecase.maps.ProcessMapsDataUsecase import ProcessMapsDataUsecase
from src.core.usecase.maps.RetrieveMapsInfoUsecase import RetrieveMapsInfoUsecase
from src.core.usecase.maps.SaveMapsDataInDatabaseUsecase import SaveMapsDataInDatabaseUsecase
from src.core.usecase.match_participants.GetMatchParticipantInfoFromDatabaseUseCase import GetMatchParticipantInfoFromDatabaseUseCase
from src.core.usecase.match_participants.MatchPlayerDetailsModel import MatchPlayerDetailsModel
from src.core.usecase.match_participants.RetrieveMatchDetailsUsecase import RetrieveMatchDetailsUsecase
from src.core.usecase.match_participants.RetrieveMatchIdsFromUserPuuidUseCase import \
    RetrieveMatchIdsFromUserPuuidUseCase
from src.core.usecase.match_participants.SaveMatchPlayerDetailsUseCase import SaveMatchPlayerDetailsUseCase
from src.core.usecase.match_team_info.GetMatchInfoTeamInfoByMatchInfoIdAndTeamIdFromDatabaseUseCase import \
    GetMatchInfoTeamInfoByMatchInfoIdAndTeamIdFromDatabaseUseCase
from src.core.usecase.match_team_info.MatchTeamInfoModel import MatchTeamInfoModel
from src.core.usecase.match_team_info.SaveMatchTeamInfoInDatabaseUseCase import SaveMatchTeamInfoInDatabaseUseCase
from src.core.usecase.matches_info.MatchInfoModel import MatchInfoModel
from src.core.usecase.matches_info.SaveMatchesInfoInDatabaseUseCase import SaveMatchesInfoInDatabaseUseCase
from src.core.usecase.objectives.GetObjectivesInfoByObjectiveTypeIdAndMatchInfoTeamIdFromDatabaseUseCase import \
    GetObjectivesInfoByObjectiveTypeIdAndMatchInfoTeamIdFromDatabaseUseCase
from src.core.usecase.objectives.ObjectiveModel import ObjectiveModel
from src.core.usecase.objectives.SaveObjectiveInfoInDatabaseUseCase import SaveObjectiveInfoInDatabaseUseCase
from src.core.usecase.objectives_type.GetObjectiveTypeInfoFromDatabaseUseCase import \
    GetObjectiveTypeInfoFromDatabaseUseCase
from src.core.usecase.objectives_type.SaveObjectiveTypeInfoInDatabaseUseCase import \
    SaveObjectiveTypeInfoInDatabaseUseCase
from src.core.usecase.platforms.GetPlatformByNameUseCase import GetPlatformByNameUseCase
from src.core.usecase.platforms.ProcessPlatformDataUsecase import ProcessPlatformDataUsecase
from src.core.usecase.platforms.RetrievePlatformInfoUsecase import RetrievePlatformInfoUsecase
from src.core.usecase.platforms.SavePlatformDataInDatabaseUsecase import SavePlatformDataInDatabaseUsecase
from src.core.usecase.positions.GetPositionInfoFromDatabaseUseCase import GetPositionInfoFromDatabaseUseCase
from src.core.usecase.positions.SavePositionInfoInDatabaseUseCase import SavePositionInfoInDatabaseUseCase
from src.core.usecase.queues.ProcessQueueDataUsecase import ProcessQueueDataUsecase
from src.core.usecase.queues.RetrieveQueueInfoUsecase import RetrieveQueueInfoUsecase
from src.core.usecase.queues.SaveQueueDataInDatabaseUsecase import SaveQueueDataInDatabaseUsecase
from src.core.usecase.roles.GetRoleInfoFromDatabaseUseCase import GetRoleInfoFromDatabaseUseCase
from src.core.usecase.roles.SaveRoleInfoInDatabaseUseCase import SaveRoleInfoInDatabaseUseCase
from src.dataproviders.filesystem.FileSystemConsumer import FileSystemConsumer
from src.dataproviders.http_client.RiotRestClient import RiotRestClient
from src.dataproviders.repository.MySqlCursor import MySqlCursor
from src.dataproviders.repository.MySqlDatabaseRepository import MySqlDatabaseRepository
from src.utils.PropertyReader import PropertyReader

###-------------------------------------------------------------------------------------
# Initial setup
###-------------------------------------------------------------------------------------

property_reader = PropertyReader()
bool_take_champion_data = property_reader.get_boolean_property("CONSUMER CONFIG", "champions")
bool_take_items_data = property_reader.get_boolean_property("CONSUMER CONFIG", "items")
bool_take_maps_data = property_reader.get_boolean_property("CONSUMER CONFIG", "maps")
bool_take_queue_data = property_reader.get_boolean_property("CONSUMER CONFIG", "queue")
bool_take_game_modes_data = property_reader.get_boolean_property("CONSUMER CONFIG", "game_modes")
bool_take_game_types_data = property_reader.get_boolean_property("CONSUMER CONFIG", "game_types")
bool_take_platform_data = property_reader.get_boolean_property("CONSUMER CONFIG", "platforms")
bool_take_championship_data = property_reader.get_boolean_property("CONSUMER CONFIG", "championship")
bool_matches_data = property_reader.get_boolean_property("CONSUMER CONFIG", "matches")
number_of_matches_per_player = property_reader.get_int_property("CONSUMER CONFIG", "number_of_matches_per_player")

###-------------------------------------------------------------------------------------
# Boundaries setup
###-------------------------------------------------------------------------------------
dataprovider = RiotRestClient(property_reader)
sql_cursor = MySqlCursor()
repository = MySqlDatabaseRepository(cursor=sql_cursor)
file_consumer = FileSystemConsumer()

###-------------------------------------------------------------------------------------
# Get champions data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_champion_data:
    retrieve_champions_data_usecase = RetrieveChampionsDataUsecase(dataprovider)
    get_champion_by_riot_id_id_use_case = GetChampionByRiotIdUseCase(repository)
    save_champions_data_in_database_usecase = SaveChampionsDataInDatabaseUsecase(repository, get_champion_by_riot_id_id_use_case)
    process_champions_usecase = ProcessChampionsDataUsecase(retrieve_champions_data_usecase,
                                                            save_champions_data_in_database_usecase)
    process_champions_usecase.execute()

###-------------------------------------------------------------------------------------
# Get items data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_items_data:
    retrieve_items_data_usecase = RetrieveItemsDataUsecase(dataprovider)
    save_items_data_usecase = SaveItemsDataInDatabaseUsecase(repository)
    process_items_usecase = ProcessItemsDataUsecase(retrieve_items_data_usecase, save_items_data_usecase)
    process_items_usecase.execute()

###-------------------------------------------------------------------------------------
# Get maps data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_maps_data:
    retrieve_maps_data_usecase = RetrieveMapsInfoUsecase(dataprovider)
    save_maps_data_usecase = SaveMapsDataInDatabaseUsecase(repository)
    process_maps_usecase = ProcessMapsDataUsecase(retrieve_maps_data_usecase, save_maps_data_usecase)
    process_maps_usecase.execute()

###-------------------------------------------------------------------------------------
# Get queue data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_queue_data:
    retrieve_queue_data_usecase = RetrieveQueueInfoUsecase(dataprovider, repository)
    save_queue_data_usecase = SaveQueueDataInDatabaseUsecase(repository)
    process_maps_usecase = ProcessQueueDataUsecase(retrieve_queue_data_usecase, save_queue_data_usecase)
    process_maps_usecase.execute()

###-------------------------------------------------------------------------------------
# Get game modes data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_game_modes_data:
    retrieve_game_modes_data_usecase = RetrieveGameModesInfoUseCase(dataprovider, repository)
    save_game_modes_data_usecase = SaveGameModesDataInDatabaseUseCase(repository)
    process_game_modes_usecase = ProcessGameModesDataUseCase(retrieve_game_modes_data_usecase,
                                                             save_game_modes_data_usecase)
    process_game_modes_usecase.execute()

###-------------------------------------------------------------------------------------
# Get game types data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_game_types_data:
    retrieve_game_types_data_usecase = RetrieveGameTypesInfoUsecase(dataprovider, repository)
    save_game_types_data_usecase = SaveGameTypesDataInDatabaseUsecase(repository)
    process_games_types_usecase = ProcessGameTypesDataUsecase(retrieve_game_types_data_usecase,
                                                              save_game_types_data_usecase)
    process_games_types_usecase.execute()

###-------------------------------------------------------------------------------------
# Get platform data from file system (resource dir)
###-------------------------------------------------------------------------------------
if bool_take_platform_data:
    retrieve_platform_data_usecase = RetrievePlatformInfoUsecase(file_consumer=file_consumer)
    save_platform_data_in_database_usecase = SavePlatformDataInDatabaseUsecase(repository=repository)
    process_platform_data_usecase = ProcessPlatformDataUsecase(retrieve_platform_data_usecase,
                                                               save_platform_data_in_database_usecase)
    process_platform_data_usecase.execute()

###-------------------------------------------------------------------------------------
# Process team info from file system (resource dir)
###-------------------------------------------------------------------------------------
if bool_take_championship_data:
    retrieve_championship_data_use_case = RetrieveChampionshipInfoUseCase(file_consumer)
    retrieve_player_info_use_case = RetrievePlayerInfoUseCase(dataprovider)
    save_team_in_database_use_case = SaveTeamDataInDatabaseUseCase(repository)
    get_team_by_name_use_case = GetTeamByNameUseCase(repository)
    save_player_use_case = SavePlayerDataInDatabaseUseCase(repository, retrieve_player_info_use_case)
    save_player_team_info_in_database_use_case = SavePlayerTeamInfoInDatabaseUseCase(repository)
    process_lineup_data = ProcessLineUpDataUseCase(retrieve_championship_data_use_case,
                                                   save_team_in_database_use_case, get_team_by_name_use_case,
                                                   save_player_use_case, save_player_team_info_in_database_use_case)
    a = process_lineup_data.execute()

###-------------------------------------------------------------------------------------
# Get platform data from file system (resource dir)
###-------------------------------------------------------------------------------------
if bool_matches_data:
    get_players_puuid_from_db_usecase = GetPlayersPuuidFromDatabaseUseCase(repository)
    a = get_players_puuid_from_db_usecase.execute()
    retrieve_matches_id_usecase = RetrieveMatchIdsFromUserPuuidUseCase(dataprovider)
    retrieve_match_details_use_case = RetrieveMatchDetailsUsecase(dataprovider)
    get_position_info_from_database_use_case = GetPositionInfoFromDatabaseUseCase(repository)
    save_position_info_in_database_use_case = SavePositionInfoInDatabaseUseCase(repository, get_position_info_from_database_use_case)
    get_role_info_from_database_use_case = GetRoleInfoFromDatabaseUseCase(repository)
    save_role_info_in_database_use_case = SaveRoleInfoInDatabaseUseCase(repository, get_role_info_from_database_use_case)
    get_objective_info_from_database_use_case = GetObjectiveTypeInfoFromDatabaseUseCase(repository)
    save_objective_type_info_in_database_use_case = SaveObjectiveTypeInfoInDatabaseUseCase(repository, get_objective_info_from_database_use_case)
    get_game_mode_by_name_use_case = GetGameModeByNameUseCase(repository)
    get_platform_by_name_use_case = GetPlatformByNameUseCase(repository)
    get_game_type_by_name_use_case = GetGameTypeByNameUseCase(repository)
    save_match_info_in_database_use_case = SaveMatchesInfoInDatabaseUseCase(repository)
    get_match_team_info_by_match_info_id_and_team_id_from_database_use_case = GetMatchInfoTeamInfoByMatchInfoIdAndTeamIdFromDatabaseUseCase(repository)
    save_match_team_info_in_database_use_case = SaveMatchTeamInfoInDatabaseUseCase(repository, get_match_team_info_by_match_info_id_and_team_id_from_database_use_case)
    get_objective_by_objective_type_id_and_match_info_team_id_from_database_use_case = GetObjectivesInfoByObjectiveTypeIdAndMatchInfoTeamIdFromDatabaseUseCase(repository)
    save_objective_info_in_database_use_case = SaveObjectiveInfoInDatabaseUseCase(repository, get_objective_by_objective_type_id_and_match_info_team_id_from_database_use_case)
    get_ban_info_by_champion_id_and_match_info_team_id_from_database_use_case = GetBanInfoByChampionIdAndMatchInfoTeamIdFromDatabaseUseCase(repository)
    save_ban_in_database_use_case = SaveBanInDatabaseUseCase(repository, get_ban_info_by_champion_id_and_match_info_team_id_from_database_use_case)
    get_player_by_summoner_name_use_case = GetPlayerBySummonerNameUseCase(repository)
    get_match_participant_info_from_database_use_case = GetMatchParticipantInfoFromDatabaseUseCase(repository)
    save_match_player_details_use_case = SaveMatchPlayerDetailsUseCase(repository, get_match_participant_info_from_database_use_case)
    get_champion_by_riot_id_id_use_case = GetChampionByRiotIdUseCase(repository)
    b = []

    for puuid in a:
        b.append(retrieve_matches_id_usecase.execute(puuid[0], number_of_matches_per_player))

    matches_details = []

    for match_id_by_player in b:
        for match_id in match_id_by_player:
            match_participant = retrieve_match_details_use_case.execute(match_id)

            mode_id = get_game_mode_by_name_use_case.execute(match_participant['info']['gameMode']).id
            game_type_id = get_game_type_by_name_use_case.execute(match_participant['info']['gameType']).id
            platform_id = get_platform_by_name_use_case.execute(match_participant['info']['platformId']).id
            queue_id = match_participant['info']['queueId']

            match_info = MatchInfoModel(id=None,
                                        mode_id=mode_id,
                                        type_id=game_type_id,
                                        creation=match_participant['info']['gameCreation'],
                                        duration=match_participant['info']['gameEndTimestamp'] - match_participant['info']['gameStartTimestamp'],
                                        start=match_participant['info']['gameStartTimestamp'],
                                        game_patch=match_participant['info']['gameVersion'],
                                        platform_id=platform_id,
                                        queue_id=queue_id)

            match_info_saved = save_match_info_in_database_use_case.execute(match_info)

            for info_participant in match_participant['info']['participants']:
                for key, value in info_participant.items():

                    individual_position_saved = save_position_info_in_database_use_case.execute(
                        position_name=info_participant['individualPosition'])

                    team_position_saved = save_position_info_in_database_use_case.execute(
                        position_name=info_participant['teamPosition'])

                    role_saved = save_role_info_in_database_use_case.execute(role=info_participant['role'])

                    player_saved = get_player_by_summoner_name_use_case.execute(info_participant['summonerName'])

                    for team_info in match_participant['info']['teams']:
                        match_team_info = MatchTeamInfoModel(id=None, match_info_id=match_info_saved,
                                                             team_id=team_info['teamId'])

                        match_team_info_saved = save_match_team_info_in_database_use_case.execute(match_team_info)

                        for ban in team_info['bans']:
                            saved_champion = get_champion_by_riot_id_id_use_case.execute(ban['championId'])

                            if saved_champion:
                                ban_to_save = BanModel(id=None, champion_id=saved_champion.id, match_info_team_id=match_team_info_saved, pick_turn=ban['pickTurn'])
                                save_ban_in_database_use_case.execute(ban_to_save)

                        for objective_name, objective_data in team_info['objectives'].items():
                            objective_type_saved = save_objective_type_info_in_database_use_case.execute(objective_name)

                            first = 1 if objective_data['first'] else 0

                            objective = ObjectiveModel(id=None, objective_type_id=objective_type_saved,
                                                       match_info_team_id=match_team_info_saved, first=first,
                                                       kills=objective_data['kills'])

                            save_objective_info_in_database_use_case.execute(objective)

                    saved_champion = get_champion_by_riot_id_id_use_case.execute(info_participant['championId'])

                    if player_saved and saved_champion:
                        match_player_details = MatchPlayerDetailsModel(
                            assists=info_participant['assists'],
                            bount_level=info_participant['bountyLevel'],
                            champ_exp=info_participant['champExperience'],
                            champion_level=info_participant['champLevel'],
                            champion_id=saved_champion.id,
                            consumables_purchased=info_participant['consumablesPurchased'],
                            damage_dealt_to_objectives=info_participant['damageDealtToObjectives'],
                            damage_dealt_to_turrets=info_participant['damageDealtToTurrets'],
                            damage_self_mitigated=info_participant['damageSelfMitigated'],
                            deaths=info_participant['deaths'],
                            damage_dealt_to_buildings=info_participant['damageDealtToBuildings'],
                            detector_wards_placed=info_participant['detectorWardsPlaced'],
                            double_kills=info_participant['doubleKills'],
                            dragon_kills=info_participant['dragonKills'],
                            first_blood_assist=1 if info_participant['firstBloodAssist'] else 0,
                            first_blood_kill=1 if info_participant['firstBloodKill'] else 0,
                            first_tower_assist=1 if info_participant['firstTowerAssist'] else 0,
                            first_tower_kill=1 if info_participant['firstTowerKill'] else 0,
                            gold_earned=info_participant['goldEarned'],
                            gold_spent=info_participant['goldSpent'],
                            individual_position_id=individual_position_saved,
                            inhibitor_kills=info_participant['inhibitorKills'],
                            inhibitor_lost=info_participant['inhibitorsLost'],
                            inhibitor_takedowns=info_participant['inhibitorTakedowns'],
                            items_purchased=info_participant['itemsPurchased'],
                            killing_sprees=info_participant['killingSprees'],
                            kills=info_participant['kills'],
                            lane=info_participant['lane'],
                            largest_critical_strike=info_participant['largestCriticalStrike'],
                            largest_killing_spree=info_participant['largestKillingSpree'],
                            largest_multi_kill=info_participant['largestMultiKill'],
                            longest_time_spent_living=info_participant['longestTimeSpentLiving'],
                            magic_damage_dealt=info_participant['magicDamageDealt'],
                            magic_damage_dealt_to_champions=info_participant['magicDamageDealtToChampions'],
                            magic_damage_taken=info_participant['magicDamageTaken'],
                            match_info_team_id=match_info_saved,
                            neutral_minions_killed=info_participant['neutralMinionsKilled'],
                            nexus_kills=info_participant['nexusKills'],
                            nexus_lost=info_participant['nexusLost'],
                            nexus_takedowns=info_participant['nexusTakedowns'],
                            objective_stolen=info_participant['objectivesStolen'],
                            objective_stolen_assistis=info_participant['objectivesStolenAssists'],
                            penta_kills=info_participant['pentaKills'],
                            physical_damage_dealt=info_participant['physicalDamageDealt'],
                            physical_damage_dealt_to_champions=info_participant['physicalDamageDealtToChampions'],
                            physical_damage_taken=info_participant['physicalDamageTaken'],
                            player_id=player_saved.id,
                            quadra_kills=info_participant['quadraKills'],
                            role_id=role_saved,
                            sight_wards_bought_in_game=info_participant['sightWardsBoughtInGame'],
                            team_early_surrendered=1 if info_participant['teamEarlySurrendered'] else 0,
                            team_position_id=team_position_saved,
                            time_ccing_others=info_participant['timeCCingOthers'],
                            time_played=info_participant['timePlayed'],
                            total_damage_dealt=info_participant['totalDamageDealt'],
                            total_damage_dealt_to_champions=info_participant['totalDamageDealtToChampions'],
                            total_damage_shielded_on_teammates=info_participant['totalDamageShieldedOnTeammates'],
                            total_damage_taken=info_participant['totalDamageTaken'],
                            total_heal=info_participant['totalHeal'],
                            total_heal_on_teammates=info_participant['totalHealsOnTeammates'],
                            total_minions_killed=info_participant['totalMinionsKilled'],
                            total_time_cc_dealt=info_participant['totalTimeCCDealt'],
                            total_time_spent_dead=info_participant['totalTimeSpentDead'],
                            total_units_healed=info_participant['totalUnitsHealed'],
                            triple_kills=info_participant['tripleKills'],
                            true_damage_dealt=info_participant['trueDamageDealt'],
                            true_damage_dealt_to_champions=info_participant['trueDamageDealtToChampions'],
                            true_damage_taken=info_participant['trueDamageTaken'],
                            turret_kills=info_participant['turretKills'],
                            turrets_takedowns=info_participant['turretTakedowns'],
                            turrets_lost=info_participant['turretsLost'],
                            unreal_kills=info_participant['unrealKills'],
                            vision_score=info_participant['visionScore'],
                            vision_wards_bought_in_game=info_participant['visionWardsBoughtInGame'],
                            wards_killed=info_participant['wardsKilled'],
                            wards_placed=info_participant['wardsPlaced'],
                        )

                        saved_match_player_details = save_match_player_details_use_case.execute(match_player_details)
                        print(f"\nPlayer adicionado")
