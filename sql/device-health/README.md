# Device Health Analysis

SQL analyses developed to investigate recurring fleet-device connectivity and GPS-quality issues.

## Device Undocked / Loose Connection Events

**File:** `device-undocked-loose-connections.sql`

Identifies vehicles generating more than 30 device-undocked events during a rolling 30-day period.

### Techniques

- Subquery
- `COUNT`
- `GROUP BY`
- `HAVING`
- `LEFT JOIN`
- Date filtering

The 30-event / 30-day criteria were selected as part of the original troubleshooting methodology.

## Poor GPS Quality Events

**File:** `poor-gps-quality-events.sql`

Counts recurring poor GPS-quality events by vehicle and operating location over a 90-day analysis period.

### Techniques

- `COUNT`
- `LEFT JOIN`
- `IN`
- `GROUP BY`
- `DATEADD`
- `GETDATE`
- Aggregation

## Device / DSN Lookup

**File:** `device-dsn-lookup.sql`

Provides a targeted lookup used during troubleshooting to associate a device identifier with its vehicle and operating location.

Actual production device identifiers have been replaced with fictional values.

## Sanitization

Production schema names, vehicle identifiers, device serial numbers, internal operating-center terminology, and confidential production information have been removed or replaced.
