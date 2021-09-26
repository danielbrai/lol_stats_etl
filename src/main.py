from src.core.usecase.ProcessChampionsDataUsecase import ProcessChampionsDataUsecase
from src.core.usecase.ProcessItemsDataUsecase import ProcessItemsDataUsecase
from src.core.usecase.RetrieveChampionsDataUsecase import RetrieveChampionsDataUsecase
from src.core.usecase.RetrieveItemsDataUsecase import RetrieveItemsDataUsecase
from src.core.usecase.SaveChampionsDataInDatabaseUsecase import SaveChampionsDataInDatabaseUsecase
from src.core.usecase.SaveItemsDataInDatabaseUsecase import SaveItemsDataInDatabaseUsecase
from src.dataproviders.http_client.RiotRestClient import RiotRestClient
from src.dataproviders.repository.MySqlDatabaseRepository import MySqlDatabaseRepository

###-------------------------------------------------------------------------------------
# Boundaries setup
###-------------------------------------------------------------------------------------
dataprovider = RiotRestClient()
repository = MySqlDatabaseRepository()

###-------------------------------------------------------------------------------------
# Get champions data from Riot API
###-------------------------------------------------------------------------------------
bool_take_champion_data = True
if bool_take_champion_data:
    retrieve_champions_data_usecase = RetrieveChampionsDataUsecase(dataprovider)
    save_champions_data_in_database_usecase = SaveChampionsDataInDatabaseUsecase(repository)
    process_champions_usecase = ProcessChampionsDataUsecase(retrieve_champions_data_usecase, save_champions_data_in_database_usecase)
    process_champions_usecase.execute()

###-------------------------------------------------------------------------------------
# Get items data from Riot API
###-------------------------------------------------------------------------------------
bool_take_items_data = True
if bool_take_items_data:
    retrieve_items_data_usecase = RetrieveItemsDataUsecase(dataprovider)
    retrieve_items_data_usecase.execute()
    save_items_data_usecase = SaveItemsDataInDatabaseUsecase(repository)
    process_items_usecase = ProcessItemsDataUsecase(retrieve_items_data_usecase, save_items_data_usecase)
    process_items_usecase.execute()
