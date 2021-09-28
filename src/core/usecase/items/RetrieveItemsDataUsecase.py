from src.core.constraints import RiotRestClientConstraint
from src.core.usecase.items.ItemModel import ItemModel


class RetrieveItemsDataUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self):
        response = self.dataprovider.get_items_data()
        items_data = response.json()['data']
        items_model = list(ItemModel(id=item[0], name=item[1]['name']) for item in items_data.items())
        return items_model
