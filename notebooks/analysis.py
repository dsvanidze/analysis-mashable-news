# %% [markdown]
# # Libraries

# %%
from sklearn.ensemble import RandomForestClassifier
import ydata_profiling as yp
import pandas as pd
import numpy as np
import seaborn as sb

# %% [markdown]
# # Data Preparation

# %%
data_raw = pd.read_csv("../data/OnlineNewsPopularity.csv")

# %%
# Remove empty spaces in the begining of columns names
data_raw.rename({columnName:columnName.replace(" ", "") for columnName in data_raw.columns}, 
                axis="columns", 
                inplace=True)

# %%
# profile = yp.ProfileReport(data_raw, title = "Mashable News Data Analysis - Descriptive Statistics", minimal=True)
# profile.to_file("../output/descriptive-statistics.html")

# %%
data_raw.info()

# %%
