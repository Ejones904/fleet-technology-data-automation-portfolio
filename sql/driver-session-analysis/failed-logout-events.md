# Failed Logout Events by Driver

## Problem

Driver sessions could remain active longer than expected when a logout was not properly recorded. I needed a way to identify these events and determine whether patterns existed across drivers or operating locations.

## Approach

The query calculates login duration, identifies sessions exceeding **16 hours**, determines the day of the week, counts repeated events by driver and operating location, and limits the analysis to a recent seven-day period.

The 16-hour threshold was selected as part of my troubleshooting methodology.

## SQL Techniques

`LEFT JOIN` • `DATEDIFF` • `DATEPART` • `CASE` • `COUNT` • `OVER` • `PARTITION BY` • date filtering

## Operational Use

The results provided a way to identify recurring failed-logout behavior and determine whether events were concentrated around particular drivers or operating locations.

## Sanitization

Production table names, column names, system identifiers, and organizational terminology have been replaced with generic equivalents while preserving the original query structure and troubleshooting logic.
