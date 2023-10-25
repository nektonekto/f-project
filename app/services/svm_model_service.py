import numpy as np

from app.services.abs_model_services import AbstractModelServices
from sklearn import svm
from onnxconverter_common import FloatTensorType
from skl2onnx import convert_sklearn
import onnxruntime as rt
from typing import List, Dict
import numpy as np


# TODO: Доработать


class SVModelService(AbstractModelServices):
    # def create_model(self, params: Dict):
    def learn_model(self, data):
        self.model.fit(data)

    def convert_model_to_onnx(self, input_shape):
        return convert_sklearn(self.model, initial_types=[("input", FloatTensorType(input_shape))])

    def test_model(self, input_shape: List, file_name: str, provider: List, test_data: np.ndarray):
        sess = rt.InferenceSession(file_name, providers=provider)
        input_name = sess.get_inputs()[0].name
        output_name = sess.get_outputs()[0].name

        return sess.run([output_name], {input_name: test_data.astype(np.float32)})[0]


class SVCModel(SVModelService):
    def __init__(self, params):
        self.model = svm.SVC(
                C=params['C'],
                kernel=params['kernel'],
                degree=params['degree'],
                gamma=params['gamma'],
                coef0=params['coef0'],
                shrinking=params['shrinking'],
                probability=params['probability'],
                tol=params['tol'],
                cache_size=params['cache_size'],
                class_weight=params['class_weight'],
                verbose=params['verbose'],
                max_iter=params['max_iter'],
                decision_function_shape=params['decision_function_shape'],
                break_ties=params['break_ties'],
                random_state=params['random_state']
            )


class SVRModel(SVModelService):
    def __init__(self, params):
        self.model = svm.SVR(
                kernel=params['kernel'],
                degree=params['degree'],
                gamma=params['gamma'],
                coef0=params['coef0'],
                tol=params['tol'],
                C=params['C'],
                epsilon=params['epsilon'],
                shrinking=params['shrinking'],
                cache_size=params['cache_size'],
                verbose=params['verbose'],
                max_iter=params['max_iter']
            )
