import os
from src.core.constraints.JsonConsumerConstarint import JsonConsumerConstraint
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint
from src.core.models.Map import Map


class RetrieveMapsInfoUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self):
        response = self.dataprovider.get_maps_data()
        maps_data = response.json()
        items_model = list(Map(id=None, riot_id=map_info['mapId'], name=map_info['mapName'], notes=map_info['notes']) for map_info in maps_data)
        return items_model
