import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


# Production datasets are intentionally excluded from the repository.
# File locations are supplied through environment variables.

gps_file = os.getenv("GPS_EVENT_FILE")
loose_connection_file = os.getenv("LOOSE_CONNECTION_FILE")


Low_GPS_Events = pd.read_excel(
    gps_file,
    header=0
)

Loose_Connections = pd.read_excel(
    loose_connection_file,
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
