import json
import os

from src.core.constraints.FileConsumerConstraint import FileConsumerConstraint
from src.dataproviders.filesystem.decoder.LineUpDtoDecoder import LineUpDtoDecoder
from src.dataproviders.filesystem.decoder.PlatformDtoDecoder import PlatformDtoDecoder


class FileSystemConsumer(FileConsumerConstraint):
    def load_platform_data_from_file_system(self):
        prop_path = f'{os.path.abspath(os.curdir)}/resources/platforms.json'
        f = open(prop_path)
        data = json.load(f)
        decoder = PlatformDtoDecoder()
        return decoder.parse_to_object(data)

    def load_lineup_data_from_file_system(self):
        prop_path = f'{os.path.abspath(os.curdir)}/resources/cblol_2021_2.json'
        f = open(prop_path)
        data = json.load(f)
        decoder = LineUpDtoDecoder()
        return decoder.parse_to_object(data)
