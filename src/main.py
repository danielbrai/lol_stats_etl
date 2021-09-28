from src.core.usecase.champions.ProcessChampionsDataUsecase import ProcessChampionsDataUsecase
from src.core.usecase.game_modes.ProcessGameModesDataUsecase import ProcessGameModesDataUsecase
from src.core.usecase.items.ProcessItemsDataUsecase import ProcessItemsDataUsecase
from src.core.usecase.maps.ProcessMapsDataUsecase import ProcessMapsDataUsecase
from src.core.usecase.queues.ProcessQueueDataUsecase import ProcessQueueDataUsecase
from src.core.usecase.champions.RetrieveChampionsDataUsecase import RetrieveChampionsDataUsecase
from src.core.usecase.game_modes.RetrieveGameModesInfoUsecase import RetrieveGameModesInfoUsecase
from src.core.usecase.items.RetrieveItemsDataUsecase import RetrieveItemsDataUsecase
from src.core.usecase.maps.RetrieveMapsInfoUsecase import RetrieveMapsInfoUsecase
from src.core.usecase.queues.RetrieveQueueInfoUsecase import RetrieveQueueInfoUsecase
from src.core.usecase.champions.SaveChampionsDataInDatabaseUsecase import SaveChampionsDataInDatabaseUsecase
from src.core.usecase.game_modes.SaveGameModesDataInDatabaseUsecase import SaveGameModesDataInDatabaseUsecase
from src.core.usecase.items.SaveItemsDataInDatabaseUsecase import SaveItemsDataInDatabaseUsecase
from src.core.usecase.maps.SaveMapsDataInDatabaseUsecase import SaveMapsDataInDatabaseUsecase
from src.core.usecase.queues.SaveQueueDataInDatabaseUsecase import SaveQueueDataInDatabaseUsecase
from src.dataproviders.http_client.RiotRestClient import RiotRestClient
from src.dataproviders.repository.MySqlCursor import MySqlCursor
from src.dataproviders.repository.MySqlDatabaseRepository import MySqlDatabaseRepository
from src.utils.PropertyReader import PropertyReader

###-------------------------------------------------------------------------------------
# Initial setup
###-------------------------------------------------------------------------------------

property_reader = PropertyReader()
bool_take_champion_data = property_reader.get_boolean_property("CONSUMER CONFIG", "champions")
bool_take_items_data = property_reader.get_boolean_property("CONSUMER CONFIG", "items")
bool_take_maps_data = property_reader.get_boolean_property("CONSUMER CONFIG", "maps")
bool_take_queue_data = property_reader.get_boolean_property("CONSUMER CONFIG", "queue")
bool_take_game_modes_data = property_reader.get_boolean_property("CONSUMER CONFIG", "game_modes")

###-------------------------------------------------------------------------------------
# Boundaries setup
###-------------------------------------------------------------------------------------
dataprovider = RiotRestClient(property_reader)
sql_cursor = MySqlCursor()
repository = MySqlDatabaseRepository(cursor=sql_cursor)

###-------------------------------------------------------------------------------------
# Get champions data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_champion_data:
    retrieve_champions_data_usecase = RetrieveChampionsDataUsecase(dataprovider)
    save_champions_data_in_database_usecase = SaveChampionsDataInDatabaseUsecase(repository)
    process_champions_usecase = ProcessChampionsDataUsecase(retrieve_champions_data_usecase, save_champions_data_in_database_usecase)
    process_champions_usecase.execute()

###-------------------------------------------------------------------------------------
# Get items data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_items_data:
    retrieve_items_data_usecase = RetrieveItemsDataUsecase(dataprovider)
    save_items_data_usecase = SaveItemsDataInDatabaseUsecase(repository)
    process_items_usecase = ProcessItemsDataUsecase(retrieve_items_data_usecase, save_items_data_usecase)
    process_items_usecase.execute()

###-------------------------------------------------------------------------------------
# Get maps data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_maps_data:
    retrieve_maps_data_usecase = RetrieveMapsInfoUsecase(dataprovider)
    save_maps_data_usecase = SaveMapsDataInDatabaseUsecase(repository)
    process_maps_usecase = ProcessMapsDataUsecase(retrieve_maps_data_usecase, save_maps_data_usecase)
    process_maps_usecase.execute()

###-------------------------------------------------------------------------------------
# Get queue data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_queue_data:
    retrieve_queue_data_usecase = RetrieveQueueInfoUsecase(dataprovider, repository)
    save_queue_data_usecase = SaveQueueDataInDatabaseUsecase(repository)
    process_maps_usecase = ProcessQueueDataUsecase(retrieve_queue_data_usecase, save_queue_data_usecase)
    process_maps_usecase.execute()

###-------------------------------------------------------------------------------------
# Get game modes data from Riot API
###-------------------------------------------------------------------------------------
if bool_take_game_modes_data:
    retrieve_game_modes_data_usecase = RetrieveGameModesInfoUsecase(dataprovider, repository)
    save_game_modes_data_usecase = SaveGameModesDataInDatabaseUsecase(repository)
    process_maps_usecase = ProcessGameModesDataUsecase(retrieve_game_modes_data_usecase, save_game_modes_data_usecase)
    process_maps_usecase.execute()