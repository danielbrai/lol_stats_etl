class MatchPlayerDetailsModel:

    def __init__(self,
                 assists,
                 bount_level,
                 champ_exp,
                 champion_level,
                 champion_id,
                 consumables_purchased,
                 damage_dealt_to_objectives,
                 damage_dealt_to_turrets,
                 damage_self_mitigated,
                 deaths,
                 damage_dealt_to_buildings,
                 detector_wards_placed,
                 double_kills,
                 dragon_kills,
                 first_blood_assist,
                 first_blood_kill,
                 first_tower_assist,
                 first_tower_kill,
                 gold_earned,
                 gold_spent,
                 individual_position_id,
                 inhibitor_kills,
                 inhibitor_lost,
                 inhibitor_takedowns,
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
                 match_info_team_id,
                 neutral_minions_killed,
                 nexus_kills,
                 nexus_lost,
                 nexus_takedowns,
                 objective_stolen,
                 objective_stolen_assistis,
                 penta_kills,
                 physical_damage_dealt,
                 physical_damage_dealt_to_champions,
                 physical_damage_taken,
                 player_id,
                 quadra_kills,
                 role_id,
                 sight_wards_bought_in_game,
                 team_early_surrendered,
                 team_position_id,
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
                 turrets_lost,
                 unreal_kills,
                 vision_score,
                 vision_wards_bought_in_game,
                 wards_killed,
                 wards_placed,
                 id: int = None,
                 ):
        self.assists = assists
        self.bount_level = bount_level
        self.champ_exp = champ_exp
        self.champion_level = champion_level
        self.champion_id = champion_id
        self.consumables_purchased = consumables_purchased
        self.damage_dealt_to_objectives = damage_dealt_to_objectives
        self.damage_dealt_to_turrets = damage_dealt_to_turrets
        self.damage_self_mitigated = damage_self_mitigated
        self.deaths = deaths
        self.damage_dealt_to_buildings = damage_dealt_to_buildings
        self.detector_wards_placed = detector_wards_placed
        self.double_kills = double_kills
        self.dragon_kills = dragon_kills
        self.first_blood_assist = first_blood_assist
        self.first_blood_kill = first_blood_kill
        self.first_tower_assist = first_tower_assist
        self.first_tower_kill = first_tower_kill
        self.gold_earned = gold_earned
        self.gold_spent = gold_spent
        self.id = id
        self.individual_position_id = individual_position_id
        self.inhibitor_kills = inhibitor_kills
        self.inhibitor_lost = inhibitor_lost
        self.inhibitor_takedowns = inhibitor_takedowns
        self.items_purchased = items_purchased
        self.killing_sprees = killing_sprees
        self.kills = kills
        self.lane = lane
        self.largest_critical_strike = largest_critical_strike
        self.largest_killing_spree = largest_killing_spree
        self.largest_multi_kill = largest_multi_kill
        self.longest_time_spent_living = longest_time_spent_living
        self.magic_damage_dealt = magic_damage_dealt
        self.magic_damage_dealt_to_champions = magic_damage_dealt_to_champions
        self.magic_damage_taken = magic_damage_taken
        self.match_info_team_id = match_info_team_id
        self.neutral_minions_killed = neutral_minions_killed
        self.nexus_kills = nexus_kills
        self.nexus_lost = nexus_lost
        self.nexus_takedowns = nexus_takedowns
        self.objective_stolen = objective_stolen
        self.objective_stolen_assistis = objective_stolen_assistis
        self.penta_kills = penta_kills
        self.physical_damage_dealt = physical_damage_dealt
        self.physical_damage_dealt_to_champions = physical_damage_dealt_to_champions
        self.physical_damage_taken = physical_damage_taken
        self.player_id = player_id
        self.quadra_kills = quadra_kills
        self.role_id = role_id
        self.sight_wards_bought_in_game = sight_wards_bought_in_game
        self.team_early_surrendered = team_early_surrendered
        self.team_position_id = team_position_id
        self.time_ccing_others = time_ccing_others
        self.time_played = time_played
        self.total_damage_dealt = total_damage_dealt
        self.total_damage_dealt_to_champions = total_damage_dealt_to_champions
        self.total_damage_shielded_on_teammates = total_damage_shielded_on_teammates
        self.total_damage_taken = total_damage_taken
        self.total_heal = total_heal
        self.total_heal_on_teammates = total_heal_on_teammates
        self.total_minions_killed = total_minions_killed
        self.total_time_cc_dealt = total_time_cc_dealt
        self.total_time_spent_dead = total_time_spent_dead
        self.total_units_healed = total_units_healed
        self.triple_kills = triple_kills
        self.true_damage_dealt = true_damage_dealt
        self.true_damage_dealt_to_champions = true_damage_dealt_to_champions
        self.true_damage_taken = true_damage_taken
        self.turret_kills = turret_kills
        self.turrets_takedowns = turrets_takedowns
        self.turrets_lost = turrets_lost
        self.unreal_kills = unreal_kills
        self.vision_score = vision_score
        self.vision_wards_bought_in_game = vision_wards_bought_in_game
        self.wards_killed = wards_killed
        self.wards_placed = wards_placed
