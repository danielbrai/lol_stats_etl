from configparser import SafeConfigParser
from pathlib import Path


class PropertyReader:

    def __init__(self):
        self.parser = SafeConfigParser()
        prop_path = f'{Path(__file__).parent.parent.parent}/resources/application.ini'
        self.parser.read(prop_path)
        print('')

    def get_property_key(self, section, property_name):
        return self.parser.get(section, property_name)

    def get_boolean_property(self, section, property_name):
        return self.parser.getboolean(section, property_name)

    def get_int_property(self, section, property_name):
        return self.parser.getint(section, property_name)
