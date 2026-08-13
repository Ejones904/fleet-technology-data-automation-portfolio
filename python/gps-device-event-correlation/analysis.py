import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

Low_GPS_Events = pd.read_excel(
    "sample-data/low_gps_quality.xlsx",
    header=0
)

Loose_Connections = pd.read_excel(
    "sample-data/loose_connection_events.xlsx",
    header=0
)

Gps_2_Loose_Corr, p = pearsonr(
    Loose_Connections.Loose_Events,
    Low_GPS_Events.GPS_Quality_Events
)

print(Gps_2_Loose_Corr)

plt.scatter(
    Loose_Connections.Loose_Events,
    Low_GPS_Events.GPS_Quality_Events
)

plt.xlabel("Low Quality GPS Events")
plt.ylabel("Loose Events")
plt.show()
plt.clf()
