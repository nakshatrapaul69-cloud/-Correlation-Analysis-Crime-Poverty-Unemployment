import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dta=pd.read_csv("clean_merged.csv")
dta.rename(columns={'OBS_VALUE_x': 'crime_rank',
                    'OBS_VALUE_y': 'poverty',
                    'MEAN_OBS_OF_ALL_LEVEL_OF_KNOWLEDGE': 'unemployment'}, inplace=True)

#dta.to_csv("OBS_columns name changed.csv",index=False)

print(dta.to_string())
