import decimal
import io
import numpy.typing
import numpy as np
from scipy.sparse import spmatrix
import pandas as pd

Decimal = decimal.Decimal
PythonScalar = str | int | float | bool

ArrayLike = numpy.typing.ArrayLike
MatrixLike = np.ndarray | pd.DataFrame | spmatrix
FileLike = io.IOBase
PathLike = str
Int = int | np.int8 | np.int16 | np.int32 | np.int64
Float = float | np.float16 | np.float32 | np.float64
