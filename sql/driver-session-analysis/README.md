# Driver Session Analysis

SQL troubleshooting examples focused on driver login/logout behavior and incomplete session records.

## Failed Logout Events by Driver

**File:** `failed-logout-events-by-driver.sql`

Identifies driver sessions exceeding a 16-hour troubleshooting threshold and analyzes recurring events by driver and operating location.

### Techniques

- `LEFT JOIN`
- `DATEDIFF`
- `DATEPART`
- `CASE`
- `COUNT`
- Window functions
- `PARTITION BY`
- Date filtering

The 16-hour threshold was selected as part of the original troubleshooting methodology.

## Drivers Who Did Not Log Out

**File:** `drivers-who-did-not-logout.sql`

Identifies recent sessions where a login occurred but a corresponding logout was not recorded.

### Techniques

- Multiple `LEFT JOIN` operations
- `NULL` detection
- Status filtering
- Date filtering
- Multi-table troubleshooting

## Sanitization

Production table names, column names, driver identifiers, operating-location terminology, and other proprietary information have been replaced with generic equivalents while retaining the original troubleshooting logic.
