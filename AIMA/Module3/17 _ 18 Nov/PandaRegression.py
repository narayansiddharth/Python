import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("poster")

# special matplotlib argument for improved plots
from sklearn.datasets import load_boston

boston = load_boston()

# Now let’s convert it into pandas
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
# print(bos.columns)
# Note that there is no column on PRICE .This is given in other attribute called target
# print(boston.target.shape)
bos['PRICE'] = boston.target
print(bos.head())
print(bos.describe())

plt.show()
