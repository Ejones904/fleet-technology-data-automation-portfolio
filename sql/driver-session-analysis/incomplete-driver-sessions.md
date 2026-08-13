# Incomplete Driver Session Analysis

## Problem

Driver sessions could contain a login record without a corresponding logout record, requiring investigation of incomplete session data.

## Approach

The query identifies sessions containing a login timestamp, searches the previous **seven days**, finds records where the logout timestamp is `NULL`, applies driver and session status filters, and associates session records with driver and operating-location information.

## SQL Techniques

Multiple `LEFT JOIN` operations • `NULL` detection • status filtering • `DATEADD` • `GETDATE` • date filtering • sorting

## Operational Use

The results provided a targeted list of incomplete driver sessions that could be investigated rather than manually reviewing individual session records.

## Sanitization

Production table names, column names, organizational terminology, and identifiers have been replaced with generic equivalents. The original status conditions and troubleshooting logic have been retained.
