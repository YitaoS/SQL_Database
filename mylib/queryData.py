import sqlite3

def logQuery(query):
    with open("queryLog.md", "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")

# CREATE operation - Insert a new polling place
def insert_polling_place(db_path, polling_place):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = '''INSERT INTO polling_places (election_dt, county_name, polling_place_id, polling_place_name, precinct_name, street_address, city, state, zip)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    logQuery(query)  # Log the query
    cursor.execute(query, polling_place)
    
    conn.commit()
    conn.close()

# READ operation - Query polling places by city
def query_polling_places_by_city(db_path, city_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT * FROM polling_places WHERE city = ?"
    logQuery(query)  # Log the query
    cursor.execute(query, (city_name,))
    result = cursor.fetchall()
    
    conn.close()
    return result

# READ operation - Count polling places by county
def count_polling_places_by_county(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT county_name, COUNT(*) FROM polling_places GROUP BY county_name"
    logQuery(query)  # Log the query
    cursor.execute(query)
    result = cursor.fetchall()
    
    conn.close()
    return result

# UPDATE operation - Update the name of a polling place by its ID
def update_polling_place_name(db_path, polling_place_id, new_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = '''UPDATE polling_places
               SET polling_place_name = ?
               WHERE polling_place_id = ?'''
    logQuery(query)  # Log the query
    cursor.execute(query, (new_name, polling_place_id))
    
    conn.commit()
    conn.close()

# DELETE operation - Remove a polling place by its ID
def delete_polling_place(db_path, polling_place_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = '''DELETE FROM polling_places WHERE polling_place_id = ?'''
    logQuery(query)  # Log the query
    cursor.execute(query, (polling_place_id,))
    
    conn.commit()
    conn.close()
