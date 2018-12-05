import numpy as np
import pandas as pd

print(pd.cut(np.array([1, 3, 2, 6, 5]), 4, retbins=True, right=False))
