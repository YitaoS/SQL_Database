from mylib.extractData import extract_data
from mylib.loadData import load_data_to_db
from mylib.queryData import (
    insert_polling_place, query_polling_places_by_city, count_polling_places_by_county,
    update_polling_place_name, delete_polling_place
)

DATA_PATH = "Data/polling_place_20240514.csv"
DB_PATH = "database1.db"

def main():
    # Step 1: Extract data
    data = extract_data(DATA_PATH)
    
    # Step 2: Load data into the database
    load_data_to_db(data, DB_PATH)
    
    # Step 3: Insert a new polling place (CREATE)
    new_polling_place = ("05/15/2024", "DURHAM", 99, "DURHAM CONVENTION CENTER", "DURHAM 1", 
                         "500 FOSTER ST", "DURHAM", "NC", "27701")
    insert_polling_place(DB_PATH, new_polling_place)
    print("Inserted a new polling place.")
    
    # Step 4: Query polling places by city (READ)
    results_by_city = query_polling_places_by_city(DB_PATH, "BURLINGTON")
    print(f"Polling places in Burlington: {results_by_city}")
    
    # Step 5: Count polling places by county (READ)
    polling_place_counts = count_polling_places_by_county(DB_PATH)
    print(f"Polling places by county: {polling_place_counts}")
    
    # Step 6: Update the name of a polling place (UPDATE)
    update_polling_place_name(DB_PATH, 99, "NEW DURHAM CONVENTION CENTER")
    print("Updated the name of polling place with ID 99.")
    
    # Step 7: Delete a polling place (DELETE)
    delete_polling_place(DB_PATH, 99)
    print("Deleted the polling place with ID 99.")

if __name__ == "__main__":
    main()
