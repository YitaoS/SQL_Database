from mylib.extractData import extract_data
from mylib.loadData import load_data_to_db
from mylib.queryData import (
    insert_polling_place, query_polling_places_by_city, count_polling_places_by_county,
    update_polling_place_name, delete_polling_place
)

def log_output(message):
    with open("testOutputs.md", "a") as f:
        f.write(message + "\n")
    print(message)  # Print to console

def log_query_output(query, result):
    log_output(f"Query: {query}")
    log_output(f"Result: {result}")

def test_pipeline():
    DATA_PATH = "Data/polling_place_20240514.csv"
    DB_PATH = "database1.db"
    
    log_output("Starting tests...\n")

    # Step 1: Extract
    data = extract_data(DATA_PATH)
    assert data is not None
    log_output("Data extraction test passed.\n")
    
    # Step 2: Load
    load_data_to_db(data, DB_PATH)
    log_output("Data loading test passed.\n")
    
    # Step 3: Create (Insert)
    new_polling_place = ("05/15/2024", "DURHAM", 999, "DURHAM CONVENTION CENTER", "DURHAM 1", 
                         "500 FOSTER ST", "DURHAM", "NC", "27701")  # Unique polling_place_id
    insert_polling_place(DB_PATH, new_polling_place)
    
    # Verify insertion
    inserted_place = query_polling_places_by_city(DB_PATH, "DURHAM")
    log_query_output("SELECT * FROM polling_places WHERE city = 'DURHAM'", inserted_place)
    assert any(place[3] == "DURHAM CONVENTION CENTER" for place in inserted_place), "Inserted place not found."
    log_output("Insert test passed.\n")
    
    # Step 4: Read (Query by city)
    result_by_city = query_polling_places_by_city(DB_PATH, "BURLINGTON")
    log_query_output("SELECT * FROM polling_places WHERE city = 'BURLINGTON'", result_by_city)
    assert len(result_by_city) > 0
    log_output("Query by city test passed.\n")
    
    # Step 5: Read (Count by county)
    polling_place_counts = count_polling_places_by_county(DB_PATH)
    log_query_output("SELECT county_name, COUNT(*) FROM polling_places GROUP BY county_name", polling_place_counts)
    assert len(polling_place_counts) > 0
    log_output("Count by county test passed.\n")
    
    # Step 6: Update
    update_polling_place_name(DB_PATH, 999, "NEW DURHAM CONVENTION CENTER")
    updated_place = query_polling_places_by_city(DB_PATH, "DURHAM")
    log_query_output("SELECT * FROM polling_places WHERE city = 'DURHAM' after update", updated_place)
    assert any(place[3] == "NEW DURHAM CONVENTION CENTER" for place in updated_place), "Update failed."
    log_output("Update test passed.\n")
    
    # Step 7: Delete
    delete_polling_place(DB_PATH, 999)
    
    # Verify deletion
    deleted_place = query_polling_places_by_city(DB_PATH, "DURHAM")
    log_query_output("SELECT * FROM polling_places WHERE city = 'DURHAM' after deletion", deleted_place)
    assert not any(place[3] == "NEW DURHAM CONVENTION CENTER" for place in deleted_place), "Delete failed."
    log_output("Delete test passed.\n")
    
    log_output("All tests passed!\n")

if __name__ == "__main__":
    test_pipeline()
