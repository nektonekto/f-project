from app.services.abs_model_services import AbstractModelServices

from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier


class KNeighborsRegressorModel(AbstractModelServices):
    """Class that returns the KNeighbors Regressor model from sklearn"""

    def __init__(self, params):
        self.model = KNeighborsRegressor(
                n_neighbors=params.n_neighbors,
                weights=params.weights,
                algorithm=params.algorithm,
                leaf_size=params.leaf_size,
                p=params.p,
                metric=params.metric,
                metric_params=params.metric_params,
                n_jobs=params.n_jobs
        )


class KNeighborsClassifierModel(AbstractModelServices):
    """Class that returns the KNeighbors Classifier model from sklearn"""

    def __init__(self, params):
        self.model = KNeighborsClassifier(
                n_neighbors=params.n_neighbors,
                weights=params.weights,
                algorithm=params.algorithm,
                leaf_size=params.leaf_size,
                metric=params.metric,
                p=params.p,
                n_jobs=params.n_jobs
        )