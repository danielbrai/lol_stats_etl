import abc


class RiotRestClientConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user_puuid(self, username) -> str:
        pass

    @abc.abstractmethod
    def get_last_played_matches(self, puuid, desired_number_of_matches):
        pass

    @abc.abstractmethod
    def get_match_details(self, match_id):
        pass

    @abc.abstractmethod
    def get_champions_data(self):
        pass

    @abc.abstractmethod
    def get_maps_data(self):
        pass

    @abc.abstractmethod
    def get_queue_data(self):
        pass

    @abc.abstractmethod
    def get_game_modes_data(self):
        pass

    @abc.abstractmethod
    def get_game_types_data(self):
        pass

    def get_matches_from_player(self, quantity_of_matches: int):
        pass
