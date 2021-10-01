import abc


class FileConsumerConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_platform_data_from_file_system(self):
        pass

    @abc.abstractmethod
    def load_lineup_data_from_file_system(self):
        pass

