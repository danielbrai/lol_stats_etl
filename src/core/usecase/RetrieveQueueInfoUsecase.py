import os
from typing import List

from src.core.constraints.DatabaseRepositoryConstraint import DatabaseRepositoryConstraint
from src.core.constraints.JsonConsumerConstarint import JsonConsumerConstraint
from src.core.constraints.RiotRestClientConstraint import RiotRestClientConstraint
from src.core.models.Map import Map
from src.core.models.Queue import Queue


class RetrieveQueueInfoUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint, repository: DatabaseRepositoryConstraint):
        self.dataprovider = dataprovider
        self.repository = repository

    def execute(self):
        response = self.dataprovider.get_queue_data()
        queues_data = response.json()
        queues_entities = []
        for queue in queues_data:
            map_info: Map = self.repository.get_map_by_name(queue['map'])
            if map_info:
                queue_model = Queue(id=queue['queueId'], map_id=map_info.id, notes=queue[ 'notes'], description=queue['description'])
                queues_entities.append(queue_model)

        return queues_entities
