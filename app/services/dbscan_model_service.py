from app.services.abs_model_services import AbstractModelServices

from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.cluster import DBSCAN


class DBSCANModel(AbstractModelServices):
    """Class that returns the DBSCAN model from sklearn"""

    def __init__(self, params):
        self.model = DBSCAN(
            eps=params['eps'],
            min_samples=params['min_samples'],
            metric=params['metric'],
            metric_params=params['metric_params'],
            algorithm=params["algorithm"],
            leaf_size=params['leaf_size'],
            p=params['p'],
            n_jobs=params['n_jobs'],
        )
