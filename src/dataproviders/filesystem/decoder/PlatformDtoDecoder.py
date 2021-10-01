from src.core.usecase.platforms.PlatformModel import PlatformModel


class PlatformDtoDecoder:

    def parse_to_object(self, json):
        return list(PlatformModel(id=None, name=platform) for platform in json)
