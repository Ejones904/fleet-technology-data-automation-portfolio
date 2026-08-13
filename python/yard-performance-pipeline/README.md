# Yard Performance Analysis Pipeline

A sanitized reconstruction of a Python data-processing and operational-analysis workflow I developed professionally to analyze yard activity, shunter performance, task demand, completion activity, and operational capacity.

## Purpose

The workflow was developed to extract operational yard-task data from SQL Server, transform and clean the records with pandas, calculate task-performance metrics, and produce Excel-based operational reporting.

This project demonstrates how I combined database querying, Python data processing, business-rule calculations, and report generation in a single workflow.

## Workflow

```text
SQL Server
    ↓
SQLAlchemy
    ↓
SQL data extraction
    ↓
pandas DataFrame
    ↓
Data cleaning
    ↓
Datetime processing
    ↓
Task-time calculations
    ↓
Outlier filtering
    ↓
Data normalization
    ↓
Operational grouping
    ↓
Demand and completion analysis
    ↓
Shunter performance analysis
    ↓
Capacity calculations
    ↓
Multi-sheet Excel reporting
```

## Technical Implementation

The workflow includes:

- Connecting Python to SQL Server with SQLAlchemy
- Extracting operational yard-task data with SQL
- Loading query results into a pandas DataFrame
- Converting and processing date/time fields
- Calculating task completion duration
- Removing incomplete records
- Filtering abnormal task-duration values
- Normalizing string-based operational fields
- Grouping activity by site, shunter, and hour
- Measuring task demand
- Measuring task completion activity
- Counting shunter task activity
- Calculating average task duration
- Calculating estimated operational capacity
- Exporting multiple reporting views to Excel
- Appending analysis results to existing workbook sheets

## Technologies

- Python
- pandas
- NumPy
- SQLAlchemy
- SQL Server / T-SQL
- PyODBC
- openpyxl
- Excel reporting
- Datetime / Timedelta processing

## Example Analytical Logic

The reconstructed workflow retains the original analytical approach, including filtering task-completion durations to remove abnormal observations before calculating performance metrics.

The analysis then groups operational activity across dimensions such as:

- Operating location
- Shunter
- Task-created hour
- Task-completed hour

These grouped datasets were used to analyze operational demand, completed activity, task performance, and estimated capacity.

## Reporting

The workflow generates several Excel-based reporting views, including reconstructed equivalents of:

- Raw operational data
- Task demand
- Completed task activity
- Task counts
- Shunter performance
- Capacity analysis

The original production report and production data are intentionally excluded from this repository.

## Security and Sanitization

This repository contains a sanitized reconstruction of the original professional workflow.

The public version does **not** contain:

- Original database server names
- Production database names
- Database usernames
- Database passwords
- Internal connection strings
- Proprietary production schema identifiers
- Production yard-task records
- Internal facility identifiers where sensitive
- Personal workstation paths
- Confidential operational data

Database configuration has been replaced with environment variables:

- `DB_SERVER`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

Environment-variable credential handling is a public-release security modification and should not be interpreted as the exact configuration of the original implementation.

## Source

The sanitized Python implementation is located at:

`src/yard_performance_analysis.py`

## Portfolio Context

This project demonstrates applied professional experience using Python as part of a broader data-processing workflow rather than only for isolated scripts or exercises.

It shows how I used:

**SQL → Python → pandas → operational calculations → aggregation → reporting**

to turn enterprise operational records into information that could support troubleshooting and performance analysis.

## Confidentiality

This project is provided to demonstrate the technical approach and code structure of work I performed professionally.

The original production datasets and infrastructure are intentionally not included. The public version preserves the recoverable analytical logic while replacing sensitive identifiers and configuration information.
