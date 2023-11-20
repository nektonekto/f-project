from sqlalchemy import (Boolean, Column, String, ForeignKey, Integer, DateTime,
                        ARRAY, Text, Float)
from sqlalchemy.ext.mutable import MutableList

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    users_id = Column(primary_key=True, nullable=True)
    users_name = Column(String(18), nullable=True)
    users_last_name = Column(String(18), nullable=True)
    users_email = Column(String(50), nullable=True)
    users_password = Column(String(18), nullable=True)


class BayesGraph(Base):
    __tablename__ = 'bayes_graph'

    baygr_id = Column(Integer, primary_key=True, nullable=True)
    prjct_id = Column(Integer, ForeignKey('projects.prjct_id', ondelete='CASCADE'), nullable=True)
    datst_id = Column(Integer, ForeignKey('dataset.datst_id'))
    fildt_id = Column(Integer, ForeignKey('filedata.fildt_id', ondelete='CASCADE'))

    def __init__(self, prjct_id, datst_id, fildt_id):
        self.prjct_id = prjct_id
        self.datst_id = datst_id
        self.fildt_id = fildt_id


class DataSelectionByTypeMethod(Base):
    __tablename__ = 'data_selection_type_method_training'

    dstmt_id = Column(Integer, primary_key=True, nullable=True)
    tpmtr_id = Column(Integer, ForeignKey('type_method_training.tpmtr_id'), nullable=True)
    dfsel_id = Column(Integer, ForeignKey('data_for_selection.dfsel_id'), nullable=True)


class DataForSelection(Base):
    __tablename__ = 'data_for_selection'

    dfsel_id = Column(Integer, primary_key=True, nullable=True)
    dfsel_table_name = Column(String(18), nullable=True)
    dfsel_table_label = Column(String(18), nullable=True)


class Dataset(Base):
    __tablename__ = 'dataset'

    datst_id = Column(Integer, primary_key=True, nullable=True)
    tpmtr_id = Column(Integer, ForeignKey('type_method_training.tpmtr_id'), nullable=True)
    users_id = Column(Integer, ForeignKey('users.users_id'), nullable=True)
    fildt_id = Column(Integer, ForeignKey('filedata.fildt_id', ondelete='CASCADE'), nullable=True)
    datst_name = Column(String(18), nullable=True)
    datst_date_create = Column(DateTime, nullable=True)
    datst_date_edit = Column(DateTime)
    datst_is_normalize = Column(Boolean)
    datst_count_none = Column(Integer)

    def __init__(self, tpmtr_id, users_id, fildt_id, datst_name, datst_date_create, datst_date_edit, datst_is_normalize,
                 datst_count_none):
        self.tpmtr_id = tpmtr_id
        self.users_id = users_id
        self.fildt_id = fildt_id
        self.datst_name = datst_name
        self.datst_date_create = datst_date_create
        self.datst_date_edit = datst_date_edit
        self.datst_is_normalize = datst_is_normalize
        self.datst_count_none = datst_count_none


class Filedata(Base):
    __tablename__ = 'filedata'

    fildt_id = Column(Integer, primary_key=True, nullable=True)
    fildt_name = Column(String(50), nullable=True)
    fildt_uuid = Column(String(36), nullable=True)
    fildt_size = Column(Integer, nullable=True)
    fildt_sum = Column(String(32), nullable=True)
    fildt_total_count = Column(Integer)

    def __init__(self, fildt_name, fildt_uuid, fildt_size, fildt_sum, fildt_total_count):
        self.fildt_name = fildt_name
        self.fildt_uuid = fildt_uuid
        self.fildt_size = fildt_size
        self.fildt_sum = fildt_sum
        self.fildt_total_count = fildt_total_count


class MethodTraining(Base):
    __tablename__ = 'method_training'

    mettr_id = Column(Integer, primary_key=True, nullable=True)
    tpslt_id = Column(Integer, ForeignKey('typical_solution.tpslt_id'), nullable=True)
    mettr_name = Column(String(50), nullable=True)


class Model(Base):
    __tablename__ = 'model'

    model_id = Column(Integer, primary_key=True, nullable=True)
    prjct_id = Column(Integer, ForeignKey('projects.prjct_id', ondelete='CASCADE'), nullable=True)
    mettr_id = Column(Integer, ForeignKey('method_training.mettr_id'), nullable=True)
    fildt_id = Column(Integer, ForeignKey('filedata.fildt_id', ondelete='CASCADE'), nullable=True)
    model_params = Column(MutableList.as_mutable(ARRAY(Text)))
    model_name = Column(String(50))
    model_status = Column(Boolean)

    def __init__(self, prjct_id: int, mettr_id: int, fildt_id: int or None, model_params: List[str], model_name: str,
                 model_status: bool):
        self.prjct_id = prjct_id
        self.mettr_id = mettr_id
        self.fildt_id = fildt_id
        self.model_params = model_params
        self.model_name = model_name
        self.model_status = model_status


class TypeResultModel(Base):
    __tablename__ = 'type_result_model'

    tprmd_id = Column(Integer, primary_key=True, nullable=True)
    tpmtr_id = Column(Integer, ForeignKey('type_method_training.tpmtr_id'), nullable=True)
    tprmd_name = Column(String(50), nullable=True)


class ModelResults(Base):
    __tablename__ = 'model_results'

    mdres_id = Column(Integer, primary_key=True, nullable=True)
    model_id = Column(Integer, ForeignKey('type_method_training.tpmtr_id', ondelete='CASCADE'), nullable=True)
    tprmd_id = Column(String(50), nullable=True)
    mdres_value = Column(MutableList.as_mutable(ARRAY(Float)))

    def __init__(self, model_id: int, tprmd_id: int, mdres_value=None):
        if mdres_value is None:
            mdres_value = []
        self.model_id = model_id
        self.tprmd_id = tprmd_id
        self.mdres_value = mdres_value


class ParamTypeMethod(Base):
    __tablename__ = 'params_of_type_methods'

    prtmt_id = Column(Integer, primary_key=True, nullable=True)
    typed_id = Column(Integer, ForeignKey('bp_pbp.bppbp_id'), nullable=True)
    prtmt_name = Column(String(25), nullable=True)
    prtmt_default_value = Column(String(50))
    prtmt_possible_values = Column(MutableList.as_mutable(ARRAY(Text)))
    prtmt_description_input_data = Column(String)
    prtmt_description_param = Column(String)
    prtmt_value_min = Column(String(10))
    prtmt_value_max = Column(String(10))


class TypeLinkMethod(Base):
    __tablename__ = 'type_link_method_learn'
    tlkml_id = Column(Integer, primary_key=True, nullable=True)
    tpmtr_id = Column(Integer, ForeignKey('type_method_training.tpmtr_id'), nullable=True)
    mettr_id = Column(Integer, ForeignKey('method_training.mettr_id'), nullable=True)


class TypeMethodParams(Base):
    __tablename__ = 'type_method_params'

    tpmpr_id = Column(Integer, primary_key=True, nullable=True)
    tlkml_id = Column(Integer, ForeignKey('type_link_method_learn.tlkml_id'), nullable=True)
    prtmt_id = Column(Integer, ForeignKey('params_of_type_methods.prtmt_id'), nullable=True)
    tpmpr_number = Column(Integer)


class TypeData(Base):
    __tablename__ = 'type_data'

    typed_id = Column(Integer, primary_key=True, nullable=True)
    typed_name = Column(String(18), nullable=True)
    typed_description = Column(String(255))


class Projects(Base):
    __tablename__ = 'projects'

    prjct_id = Column(Integer, primary_key=True, nullable=True)
    users_id = Column(Integer, ForeignKey('users.users_id'), nullable=True)
    tpmtr_id = Column(Integer, ForeignKey('type_method_training.tpmtr_id'), nullable=True)
    prckt_name = Column(String(50))
    prjct_description = Column(String(255))
    prjct_date_begin = Column(DateTime)
    prjct_date_edit = Column(DateTime)
    prjct_status = Column(String(25))

    def __init__(self, users_id, tpmtr_id, prckt_name, prjct_description, prjct_date_begin, prjct_date_edit,
                 prjct_status):
        self.users_id = users_id
        self.tpmtr_id = tpmtr_id
        self.prckt_name = prckt_name
        self.prjct_description = prjct_description
        self.prjct_date_begin = prjct_date_begin
        self.prjct_date_edit = prjct_date_edit
        self.prjct_status = prjct_status


class SelectionProject(Base):
    __tablename__ = 'selection_project'

    slnpr_id = Column(Integer, primary_key=True, nullable=True)
    prjct_id = Column(Integer, ForeignKey('projects.prjct_id', ondelete='CASCADE'), nullable=True)
    tpsel_id = Column(Integer, ForeignKey('type_selection.tpsel_id'), nullable=True)
    fildt_id = Column(Integer, ForeignKey('filedata.fildt_id', ondelete='CASCADE'), nullable=True)
    slnpr_date_create = Column(DateTime, nullable=True)

    def __init__(self, prjct_id, tpsel_id, fildt_id, slnpr_date_create):
        self.prjct_id = prjct_id
        self.tpsel_id = tpsel_id
        self.fildt_id = fildt_id
        self.slnpr_date_create = slnpr_date_create


class TypeSelection(Base):
    __tablename__ = 'type_selection'

    tpsel_id = Column(Integer, primary_key=True, nullable=True)
    tpsel_name = Column(String(50), nullable=True)


class TypeMethodTraining(Base):
    __tablename__ = 'type_method_training'

    tpmtr_id = Column(Integer, primary_key=True, nullable=True)
    tpmtr_name = Column(String(50), nullable=True)
    tpmtr_url = Column(String(255), nullable=True)


class TypicalSolution(Base):
    __tablename__ = 'typical_solution'

    tpslt_id = Column(Integer, primary_key=True, nullable=True)
    tpslt_name = Column(String(50), nullable=True)
    tpslt_description = Column(String(255))
