# SQL Troubleshooting & Analysis

This section contains sanitized reconstructions of SQL queries I developed while supporting enterprise fleet technology systems.

The queries were used for real-world troubleshooting, operational analysis, device-health investigation, driver-session analysis, and data-quality review.

Production schema names, identifiers, infrastructure information, and confidential data have been removed or replaced while preserving the original troubleshooting logic and analytical criteria.

## Driver Session Analysis

- [Failed Logout Events by Driver](driver-session-analysis/failed-logout-events-by-driver.sql)
- [Drivers Who Did Not Log Out](driver-session-analysis/drivers-who-did-not-logout.sql)

## Device Health Analysis

- [Device Undocked / Loose Connection Events](device-health/device-undocked-loose-connections.sql)
- [Poor GPS Quality Events](device-health/poor-gps-quality-events.sql)
- [Device / DSN Lookup](device-health/device-dsn-lookup.sql)

## Additional Operational Analysis

- [Placeholder / Landmark Audit](additional-analysis/placeholder-landmark-audit.sql)

## SQL Skills Demonstrated

- T-SQL
- SQL Server
- `LEFT JOIN`
- Subqueries
- Window functions
- `PARTITION BY`
- Conditional aggregation
- `GROUP BY`
- `HAVING`
- `DATEDIFF`
- `DATEADD`
- `DATEPART`
- `NULL` detection
- Operational troubleshooting
- Data-quality analysis
