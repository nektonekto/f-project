from abc import ABC, abstractmethod
from typing import List, Any, Dict
import numpy as np


class AbstractModelServices(ABC):
    @abstractmethod
    def create_model(self, params: Dict): pass

    @abstractmethod
    def learn_model(self, data): pass

    @abstractmethod
    def test_model(self, input_shape: List, file_name: str, provider: List, test_data: np.ndarray): pass

    @abstractmethod
    def convert_model_to_onnx(self, input_shape): pass

