from app.services.abs_model_services import AbstractModelServices
from sklearn import svm


# TODO: Для SVC/SVR
#       1) Добавить типизацию
#       2) Переделать возвращаемую модель


class SVCModelService(AbstractModelServices):
    @staticmethod
    def create_model(params):
        return svm.SVC(
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

    # TODO: Доделать
    @staticmethod
    def learn_model(data, model):
        model.fit(data)


class SVRModelService(AbstractModelServices):
    @staticmethod
    def create_model(params):
        return svm.SVR(
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

    # TODO: Доделать
    @staticmethod
    def learn_model(model, data):
        model.fit(data)