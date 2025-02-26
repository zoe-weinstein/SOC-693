import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_excel("/Users/zoeweinstein/Desktop/spring-25/soc-693/SOC-693/GSS.xlsx")

# only keep rows where mother or father has died before 16 years old
df = df[(df["padeath"] == 1) | (df["madeath"] == 1)] 

# drop rows with missing values for income at age 16 
df = df[df["incom16"] != -100]
df = df[df["incom16"] != -99]
df = df[df["incom16"] != -98]
df = df[df["incom16"] != -97]

# drop rows where respondent degree is missing
df = df[df["degree"] != -98]

# drop rows where respondents socio-economic status is missing
df = df[df["sei10"] != -100]


# # drop rows where respondents education is missing
# df = df[df["educ"] != -99]
# df = df[df["educ"] != -98]
# # If completed 12 or more years of education, set to 12
# df.loc[df["educ"] >= 12, "educ"] = 12

# # drop rows where respondents parents's education is missing
# df = df[df["paeduc"] != -100]
# df = df[df["paeduc"] != -99]
# df = df[df["paeduc"] != -98]

# df = df[df["maeduc"] != -100]
# df = df[df["maeduc"] != -99]
# df = df[df["maeduc"] != -98]


# degree variable codebook:
# 0 Less than high school	
# 1 high school
# 2 Associate/junior college
# 3 Bachelor's
# 4 Graduate

# wrkstat variable codebook:
# 1 Working full time
# 2	Working part time
# 3	With a job, but not at work because of temporary illness, vacation, strike
# 4	Unemployed, laid off, looking for work
# 5 Retired
# 6	In school
# 7	Keeping house
# 8	Other

df.to_excel("GSS-clean.xlsx")  # save cleaned data to new file


