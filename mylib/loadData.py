import sqlite3

def load_data_to_db(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS polling_places (
                        election_dt TEXT,
                        county_name TEXT,
                        polling_place_id INTEGER,
                        polling_place_name TEXT,
                        precinct_name TEXT,
                        street_address TEXT,
                        city TEXT,
                        state TEXT,
                        zip TEXT)''')

    # Append data into the table
    data.to_sql('polling_places', conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
