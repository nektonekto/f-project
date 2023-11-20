from abc import ABC, abstractmethod
from typing import List, Any, Dict
import numpy as np

from skl2onnx import convert_sklearn
from onnxconverter_common import FloatTensorType
import onnxruntime as rt


class AbstractModelServices:
    def __init__(self):
        self.model = None

    def learn_model(self, data: Dict):
        self.model.fit(data)

    @staticmethod
    def test_model(file_name: str, provider: List, test_data: np.ndarray):
        sess = rt.InferenceSession(file_name, providers=provider)
        input_name = sess.get_inputs()[0].name
        output_name = sess.get_outputs()[0].name

        return sess.run([output_name],
                        {input_name: test_data.astype(np.float32)})[0]

    def convert_model_to_onnx(self, input_shape):
        return convert_sklearn(self.model,
                               initial_types=[("input",
                                               FloatTensorType(input_shape))])

    def get_parameters(self):
        return f"{self.model}"
