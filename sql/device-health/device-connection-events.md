# Device Undocked / Loose Connection Analysis

## Problem

Repeated device-undocked events could indicate a recurring hardware or connectivity issue affecting a vehicle.

## Approach

The query identifies `Device Undocked` events during the previous **30 days**, counts occurrences by vehicle, surfaces vehicles with **more than 30 events**, associates affected vehicles with their operating location, and ranks them by event count.

The thresholds were selected as troubleshooting criteria to focus the investigation on vehicles experiencing recurring events rather than isolated occurrences.

## SQL Techniques

`COUNT` • `GROUP BY` • `HAVING` • subquery • `LEFT JOIN` • `DATEADD` • `GETDATE`

## Operational Use

The results helped prioritize vehicles experiencing repeated device connection events for further investigation.

## Sanitization

Production schema and field names have been replaced with generic equivalents. The original analytical criteria and query structure have been retained.
