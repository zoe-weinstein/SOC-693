import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_stata("/Users/zoeweinstein/Desktop/spring-25/soc-693/programming/py/soc693_GSSex_step1v2.dta")

# make an education column from degree 
df["educ"] = df.apply(lambda _: '', axis=1)
df['educ'] = df['degree'].replace({'LT HIGH SCHOOL': '<hs',
                                    'HIGH SCHOOL': 'hs',
                                    'JUNIOR COLLEGE': '<hs',
                                    'bachelor': 'bachelor',
                                    'graduate': 'bachelor'})
# drop rows with missing values in agekdbrn
df = df.dropna(subset=['agekdbrn'])

# convert agekdbrn to integer
df['agekdbrn'] = pd.to_numeric(df['agekdbrn'], errors='coerce').astype('Int64') 

# making woman dataframe, then replacing df with it
df_wom = df[df["sex"] == "female"]
df = df_wom

# drop rows with missing values in cohort and educ
df = df.dropna(subset=['cohort'])
df = df.dropna(subset=['educ'])




if __name__ == "__main__":
    print("hello world")
    sns.lineplot(data=df, y="agekdbrn", x="cohort", hue="educ")
    plt.show()