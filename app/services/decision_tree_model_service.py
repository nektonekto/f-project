from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from app.services.abs_model_services import AbstractModelServices


class DecisionTreeClassifierModel(AbstractModelServices):
    """Class that returns the DecisionTreeClassifier model from sklearn"""

    def __init__(self, params):
        self.model = DecisionTreeClassifier(
            criterion=params['criterion'],
            splitter=params['splitter'],
            max_depth=params['max_depth'],
            min_samples_split=params['min_samples_split'],
            min_samples_leaf=params['min_samples_leaf'],
            min_weight_fraction_leaf=params['min_weight_fraction_leaf'],
            max_features=params['max_features'],
            random_state=params['random_state'],
            max_leaf_nodes=params['max_leaf_nodes'],
            min_impurity_decrease=params['min_impurity_decrease'],
            class_weight=params['class_weight'],
            ccp_alpha=params['ccp_alpha']
        )


class DecisionTreeRegressorModel(AbstractModelServices):
    """Class that returns the DecisionTreeRegressor model from sklearn"""

    def __init__(self, params):
        self.model = DecisionTreeRegressor(
            criterion=params['criterion'],
            splitter=params['splitter'],
            max_depth=params['max_depth'],
            min_samples_split=params['min_samples_split'],
            min_samples_leaf=params['min_samples_leaf'],
            min_weight_fraction_leaf=params['min_weight_fraction_leaf'],
            max_features=params['max_features'],
            random_state=params['random_state'],
            max_leaf_nodes=params['max_leaf_nodes'],
            min_impurity_decrease=params['min_impurity_decrease'],
            ccp_alpha=params['ccp_alpha']
        )
