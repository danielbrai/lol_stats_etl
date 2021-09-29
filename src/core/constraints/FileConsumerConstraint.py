import abc


class FileConsumerConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_platform_data_from_file_system(self):
        pass
