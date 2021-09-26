import json

from src.core.constraints.JsonConsumerConstarint import JsonConsumerConstraint
from src.dataproviders.filesystem.decoder.LeagueDtoDecoder import LeagueDtoDecoder


class TeamLineupJsonConsumer(JsonConsumerConstraint):

    def load_data_from_file_system(self, file_path):
        f = open(file_path)
        data = json.load(f)
        decoder = LeagueDtoDecoder()
        return decoder.parse_to_object(data)
