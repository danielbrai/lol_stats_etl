from src.core.constraints import RiotRestClientConstraint
from src.core.usecase.champions.ChampionModel import ChampionModel


class RetrieveChampionsDataUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self):
        response = self.dataprovider.get_champions_data()
        champions_data = response.json()['data']
        champions_model = list(ChampionModel(id=champions_data[champion]['key'], name=champions_data[champion]['name']) for champion in champions_data)
        return champions_model
