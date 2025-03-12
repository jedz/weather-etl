# Weather ETL Pipeline

A simple ETL pipeline that extracts weather data from the OpenWeather API, transforms it, and loads it into a SQLite database.

## How to Run
1. Clone the repo: `git clone <your-repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Get an API key from [OpenWeather](https://openweathermap.org/).
4. Update `API_KEY` in `main.py` with your key.
5. Run the pipeline: `python main.py`

## Output
Data is saved to `weather.db`. Example:
- City: London
- Temp: 10.15°C
- Weather: Scattered clouds

## Files
- `extract.py`: Fetches data from the API.
- `transform.py`: Cleans and processes data.
- `load.py`: Saves data to SQLite.
- `main.py`: Runs the full pipeline.
