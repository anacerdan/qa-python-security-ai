# Database Testing

Database validation should verify both technical persistence and business correctness.

## Example checks

```sql
-- Find duplicate business identifiers
SELECT customer_id, COUNT(*) AS record_count
FROM customer
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Validate required data
SELECT COUNT(*) AS invalid_rows
FROM customer
WHERE customer_id IS NULL
   OR status IS NULL;

-- Reconcile transaction totals
SELECT status, COUNT(*) AS records, SUM(amount) AS total_amount
FROM transaction
GROUP BY status;
```

## QA approach
- Validate inserts/updates/deletes after API actions.
- Compare source and target records for integrations.
- Check nullability, uniqueness, referential integrity, and business rules.
- Use parameterized queries in automation; never concatenate untrusted input into SQL.
