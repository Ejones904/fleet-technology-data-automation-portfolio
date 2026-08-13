import os

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from openpyxl import load_workbook


# ============================================================
# DATABASE CONNECTION
# Sanitized for public GitHub publication.
# Original server/database/user/password values removed.
# ============================================================

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)


# ============================================================
# EXTRACT YARD TASK DATA
# Production database object name has been sanitized.
# ============================================================

query = """
SELECT
    site,
    date,
    task_created_hour,
    task_created_time,
    task_type,
    task_created_by,
    shunter,
    carrier,
    trailer_num,
    origin_zone,
    destination_zone,
    task_assigned_time,
    task_planned_time,
    task_completed_time,
    task_completed_hour,
    task_distance,
    empty_distance
FROM reporting_completed_yard_tasks
WHERE task_type = 'Move Task'
  AND date >= DATEADD(DAY, -7, GETDATE())
"""

yard = pd.read_sql(query, engine, params={"date": "date"})

yard["date"] = yard["date"].dt.date


# ============================================================
# CREATE CALCULATED COLUMNS
# ============================================================

yard["Task Wait Time"] = (
    yard["task_completed_time"].astype(str).str.split().str[-1]
)

yard["Shunter Task Completion Time"] = (
    yard["task_assigned_time"].astype(str).str.split().str[-1]
)

yard["task_type"] = yard["task_type"].replace(
    {"Move": "Move Task"}
)


# ============================================================
# DROP NULL VALUES
# Original helper function preserved.
# ============================================================

def drop_na_dataframe(yard):
    yard = yard.dropna()
    yard = yard.reset_index(drop=True)
    return yard


yard = drop_na_dataframe(yard)


# ============================================================
# DROP OUTLIERS
# ============================================================

yard["Shunter Task Completion Time"] = pd.to_timedelta(
    yard["Shunter Task Completion Time"],
    errors="coerce"
)

yard["Shunter Task Completion Time"] = (
    yard["Shunter Task Completion Time"]
    .apply(pd.Timedelta)
)

yard = yard[
    (yard["Shunter Task Completion Time"] > pd.Timedelta(minutes=1))
    &
    (yard["Shunter Task Completion Time"] < pd.Timedelta(hours=1))
]


# ============================================================
# CONVERT COLUMNS TO STRING VALUES AND STRIP
# ============================================================

yard["shunter"] = yard["shunter"].astype(str).str.strip()
yard["site"] = yard["site"].astype(str).str.strip()
yard["task_created_hour"] = yard["task_created_hour"].astype(str).str.strip()
yard["task_completed_hour"] = yard["task_completed_hour"].astype(str).str.strip()


# ============================================================
# CREATE SEPARATE DATAFRAMES BASED ON GROUPING
# ============================================================

yard_dc_hour_demand = (
    yard.groupby(
        [
            "site",
            "task_created_hour"
        ]
    )
    .size()
    .unstack()
    .rename(
        columns={
            "site": "Site",
            "task_created_hour": "Hour",
            0: "Created Count"
        }
    )
    .reset_index()
)

yard_dc_hour_completed = (
    yard.groupby(
        [
            "site",
            "task_completed_hour"
        ]
    )
    .size()
    .unstack()
    .rename(
        columns={
            "site": "Site",
            "task_completed_hour": "Hour",
            0: "Completed Count"
        }
    )
    .reset_index()
)


# ============================================================
# DEMAND / COMPLETION DATA CLEANUP
# ============================================================

yard_dc_hour_demand = yard_dc_hour_demand.apply(
    lambda col: col.astype(str)
)

yard_dc_hour_completed = yard_dc_hour_completed.apply(
    lambda col: col.astype(str)
)

yard_dc_hour_demand = yard_dc_hour_demand.drop(
    columns=["site"],
    errors="ignore"
)

yard_dc_hour_completed = yard_dc_hour_completed.drop(
    columns=["site"],
    errors="ignore"
)


# ============================================================
# SHUNTER TASK COUNTS
# ============================================================

yard_dc_hour_tasks = (
    yard.groupby(
        [
            "site",
            "shunter",
            "task_created_hour"
        ]
    )
    .size()
    .unstack()
    .fillna(0)
)

yard_dc_hour_tasks = yard_dc_hour_tasks.reset_index()


# ============================================================
# SHUNTER COMPLETION / CAPACITY ANALYSIS
# ============================================================

yard_dc_shunter = (
    yard.groupby(
        [
            "site",
            "shunter"
        ]
    )["Shunter Task Completion Time"]
    .mean()
    .reset_index()
)

yard_dc_shunter["Capacity"] = (
    pd.Timedelta(hours=1)
    /
    yard_dc_shunter["Shunter Task Completion Time"]
)

yard_dc_shunter["Capacity"] = (
    yard_dc_shunter["Capacity"]
    .apply(lambda x: int(x))
)


# ============================================================
# AVERAGE TASK DURATION
# ============================================================

yard_dc_shunter_capacity = (
    yard.groupby(
        [
            "site",
            "shunter"
        ]
    )["Shunter Task Completion Time"]
    .mean()
    .reset_index()
)

yard_dc_shunter_capacity["Avg Task Duration"] = (
    yard_dc_shunter_capacity[
        "Shunter Task Completion Time"
    ]
    .apply(lambda x: x.total_seconds() / 60)
)

yard_dc_shunter_capacity["Avg Task Duration"] = (
    yard_dc_shunter_capacity["Avg Task Duration"]
    .round(2)
)


# ============================================================
# DAILY / HOURLY CAPACITY
# ============================================================

yard_dc_shunter_capacity["Day Hour"] = (
    yard_dc_shunter_capacity["Capacity"] * 8
)

yard_dc_shunter_capacity["Day Hour"] = (
    yard_dc_shunter_capacity["Day Hour"]
    .astype(int)
)


# ============================================================
# TASK COMPLETION TIME OUTPUT FORMATTING
# ============================================================

yard["Shunter Task Completion Time"] = (
    yard["Shunter Task Completion Time"]
    .astype(str)
)


# ============================================================
# INITIAL EXPORT TO EXCEL
#
# Original screenshot used a personal Desktop path.
# Public portfolio version uses the project's output directory.
# ============================================================

output_file = "output/yard_shunter_analysis.xlsx"

with pd.ExcelWriter(
    output_file,
    engine="openpyxl",
    mode="w"
) as writer:

    yard.to_excel(
        writer,
        sheet_name="Raw Data",
        index=False
    )

    yard_dc_hour_demand.to_excel(
        writer,
        sheet_name="Demand",
        index=False
    )

    yard_dc_hour_completed.to_excel(
        writer,
        sheet_name="Completed",
        index=False
    )

    yard_dc_hour_tasks.to_excel(
        writer,
        sheet_name="Tasks",
        index=False
    )

    yard_dc_shunter.to_excel(
        writer,
        sheet_name="Shunter",
        index=False
    )

    yard_dc_shunter_capacity.to_excel(
        writer,
        sheet_name="Capacity",
        index=False
    )


# ============================================================
# APPEND DATA TO EXISTING EXCEL FILE
# ============================================================

with pd.ExcelWriter(
    output_file,
    engine="openpyxl",
    mode="a",
    if_sheet_exists="overlay"
) as writer:

    yard.to_excel(
        writer,
        sheet_name="Raw Data",
        index=False,
        header=False,
        startrow=writer.sheets["Raw Data"].max_row
    )

    yard_dc_hour_demand.to_excel(
        writer,
        sheet_name="Demand",
        index=False,
        header=False,
        startrow=writer.sheets["Demand"].max_row
    )

    yard_dc_hour_completed.to_excel(
        writer,
        sheet_name="Completed",
        index=False,
        header=False,
        startrow=writer.sheets["Completed"].max_row
    )

    yard_dc_hour_tasks.to_excel(
        writer,
        sheet_name="Tasks",
        index=False,
        header=False,
        startrow=writer.sheets["Tasks"].max_row
    )

    yard_dc_shunter.to_excel(
        writer,
        sheet_name="Shunter",
        index=False,
        header=False,
        startrow=writer.sheets["Shunter"].max_row
    )

    yard_dc_shunter_capacity.to_excel(
        writer,
        sheet_name="Capacity",
        index=False,
        header=False,
        startrow=writer.sheets["Capacity"].max_row
    )
