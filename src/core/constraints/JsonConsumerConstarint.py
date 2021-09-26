import abc


class JsonConsumerConstraint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_data_from_file_system(self, file_path):
        return
