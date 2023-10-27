from app.services.abs_model_services import AbstractModelServices

from onnxconverter_common import FloatTensorType
import onnxruntime as rt

from skl2onnx import convert_sklearn
from sklearn import svm

from typing import List, Dict
import numpy as np


# TODO: Доработать


# class SVModelService(AbstractModelServices):
#

class SVCModel(AbstractModelServices):
    """Class that returns the SVM Classifier model from sklearn"""

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


class SVRModel(AbstractModelServices):
    """Class that returns the SVM Regressor model from sklearn"""

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
