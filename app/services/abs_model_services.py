from abc import ABC, abstractmethod


class AbstractModelServices(ABC):
    @staticmethod
    @abstractmethod
    def create_model(params): pass

    @staticmethod
    @abstractmethod
    def learn_model(data, model): pass

    def test_model(self): pass
