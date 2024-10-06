```sql
INSERT INTO polling_places (election_dt, county_name, polling_place_id, polling_place_name, precinct_name, street_address, city, state, zip)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
```

```sql
SELECT * FROM polling_places WHERE city = ?
```

```sql
SELECT * FROM polling_places WHERE city = ?
```

```sql
SELECT county_name, COUNT(*) FROM polling_places GROUP BY county_name
```

```sql
UPDATE polling_places
               SET polling_place_name = ?
               WHERE polling_place_id = ?
```

```sql
SELECT * FROM polling_places WHERE city = ?
```

```sql
DELETE FROM polling_places WHERE polling_place_id = ?
```

```sql
SELECT * FROM polling_places WHERE city = ?
```

