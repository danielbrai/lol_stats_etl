class MatchInfoModel:

    def __init__(self, id: int, mode_id: int, type_id: int, creation: int,
                 duration: int, start: int, game_patch: str, platform_id: int,
                 queue_id: int):
        self.id = id
        self.mode_id = mode_id
        self.type_id = type_id
        self.creation = creation
        self.duration = duration
        self.start = start
        self.game_patch = game_patch
        self.platform_id = platform_id
        self.queue_id = queue_id
