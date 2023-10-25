from app.services.abs_model_services import AbstractModelServices

from onnxconverter_common import FloatTensorType
import onnxruntime as rt

from skl2onnx import convert_sklearn
from sklearn import svm

from typing import List, Dict
import numpy as np

from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
