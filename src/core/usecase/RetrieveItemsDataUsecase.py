from src.core.constraints import RiotRestClientConstraint
from src.core.models.Item import Item


class RetrieveItemsDataUsecase:

    def __init__(self, dataprovider: RiotRestClientConstraint):
        self.dataprovider = dataprovider

    def execute(self):
        response = self.dataprovider.get_items_data()
        items_data = response.json()['data']
        items_model = list(Item(id=item[0], name=item[1]['name']) for item in items_data.items())
        return items_model
