import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_excel("/Users/zoeweinstein/Desktop/spring-25/soc-693/SOC-693/GSS-clean.xlsx")


# Data Description
df.head()
df.info()
df.describe()

# Descriptive Statistics

# Continuous Variables
df['year'].describe()
df['incom16'].describe()
df['sei10'].describe()
df["prestg10"].describe()

# Discrete Variables
df['degree'].value_counts()
df['wrkstat'].value_counts()

