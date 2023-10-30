from app.services.abs_model_services import AbstractModelServices

from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.cluster import KMeans


class KMeansModel(AbstractModelServices):
    """Class that returns the KMeans model from sklearn"""

    def __init__(self, params):
        self.model = KMeans(
            n_clusters=params['n_clusters'],
            init=params['init'],
            max_iter=params['max_iter'],
            tol=params['tol'],
            verbose=params['verbose'],
            random_state=['random_state'],
            copy_x=params['copy_x'],
            algorithm=params['algorithm'],
        )
