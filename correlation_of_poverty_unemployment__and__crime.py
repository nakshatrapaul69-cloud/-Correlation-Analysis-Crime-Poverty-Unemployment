import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dta=pd.read_csv("clean_merged.csv")
dta.rename(columns={'OBS_VALUE_x': 'crime_rank',
                    'OBS_VALUE_y': 'poverty',
                    'MEAN_OBS_OF_ALL_LEVEL_OF_KNOWLEDGE': 'unemployment'}, inplace=True)

#dta.to_csv("OBS_columns name changed.csv",index=False)

corr = dta[[
    "crime_rank",
    "poverty",
    "unemployment"
]].corr()
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(3), corr.columns, rotation=45)
plt.yticks(range(3), corr.columns)
plt.title("Crime Poverty Unemployment Correlation")
plt.savefig("chart.png", dpi=300, bbox_inches="tight")
plt.show()
