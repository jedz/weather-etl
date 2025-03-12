from extract import fetch_weather
from transform import clean_weather_data
from load import load_to_db

# Replace with your API key
API_KEY = "129b27c982bdd16e69532d1160f0ff80"

def run_etl(city):
    # Extract
    raw_data = fetch_weather(city, API_KEY)
    # Transform
    clean_data = clean_weather_data(raw_data)
    # Load
    load_to_db(clean_data)
    print(f"ETL completed for {city}")

if __name__ == "__main__":
    run_etl("Manila")  # Test with London; you can change the city