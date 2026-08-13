# Additional Operational Analysis

Additional SQL examples demonstrating operational auditing and cross-table investigation.

## Placeholder / Landmark Audit

**File:** `placeholder-landmark-audit.sql`

Audits placeholder landmark records and associates them with dispatch-stop and dispatch information.

### Techniques

- `SELECT DISTINCT`
- Multiple `LEFT JOIN` operations
- Cross-table analysis
- Filtering
- `IS NOT NULL`

## Sanitization

Production schema terminology and organizational identifiers have been replaced with generic equivalents while retaining the original query structure.
