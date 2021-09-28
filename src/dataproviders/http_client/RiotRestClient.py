import requests
from src.utils.PropertyReader import PropertyReader
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint


class RiotRestClient(RiotRestClientConstraint):
    def __init__(self, property_reader: PropertyReader):
        self.prop_reader = property_reader
        auth_token = self.prop_reader.get_property_key("API RIOT", "auth_token")
        self.headers = {'X-Riot-Token': auth_token}

    def get_user_data(self, username):
        url_summoner = self.prop_reader.get_property_key("API RIOT", "summoner_endpoint")
        br1_base_url = self.prop_reader.get_property_key("API RIOT", "br1_base_url")
        url = f'{br1_base_url}{url_summoner}/{username}'
        response = requests.get(url=url, headers=self.headers)
        return response

    def get_last_played_matches(self, puuid, number_of_matches):
        matches_id_endpoint = self.prop_reader.get_property_key("API RIOT", "matches_id_endpoint")
        americas_base_url = self.prop_reader.get_property_key("API RIOT", "americas_base_url")
        url = f'{americas_base_url}{matches_id_endpoint.replace("{puuid}", puuid)}'
        response = requests.get(url=url, headers=self.headers, params={'count': number_of_matches})
        return response

    def get_match_details(self, match_id):
        match_details_endpoint = self.prop_reader.get_property_key("API RIOT", "match_details_endpoint")
        americas_base_url = self.prop_reader.get_property_key("API RIOT", "americas_base_url")
        url = f'{americas_base_url}{match_details_endpoint.replace("{matchId}", match_id)}'
        response = requests.get(url=url, headers=self.headers)
        return response

    def get_champions_data(self):
        champions_data_endpoint = self.prop_reader.get_property_key("API RIOT", "champions_data_endpoint")
        response = requests.get(url=champions_data_endpoint, headers=self.headers)
        return response

    def get_items_data(self):
        items_data_endpoint = self.prop_reader.get_property_key("API RIOT", "items_data_endpoint")
        response = requests.get(url=items_data_endpoint, headers=self.headers)
        return response

    def get_maps_data(self):
        maps_data_endpoint = self.prop_reader.get_property_key("API RIOT", "maps_data_endpoint")
        response = requests.get(url=maps_data_endpoint, headers=self.headers)
        return response

    def get_queue_data(self):
        queue_data_endpoint = self.prop_reader.get_property_key("API RIOT", "queue_data_endpoint")
        response = requests.get(url=queue_data_endpoint, headers=self.headers)
        return response

    def get_game_modes_data(self):
        game_modes_data_endpoint = self.prop_reader.get_property_key("API RIOT", "game_modes_endpoint")
        response = requests.get(url=game_modes_data_endpoint, headers=self.headers)
        return response


