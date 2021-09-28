import abc


class RiotRestClientConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user_data(self, username):
        return

    @abc.abstractmethod
    def get_last_played_matches(self, puuid, desired_number_of_matches):
        return

    @abc.abstractmethod
    def get_match_details(self, match_id):
        return

    @abc.abstractmethod
    def get_champions_data(self):
        return

    @abc.abstractmethod
    def get_maps_data(self):
        return

    @abc.abstractmethod
    def get_queue_data(self):
        return


