import pandas as pd

def clean_weather_data(data):
    # Convert JSON to DataFrame
    df = pd.json_normalize(data)
    
    # Extract relevant fields and convert temperature from Kelvin to Celsius
    df['main.temp'] = df['main.temp'] - 273.15

    # Checking the comuns, can be commented off after testing
    print(df.columns)
    # Select only the columns we want
    #cleaned_df = df[['name', 'main.temp', 'weather[0].description']].rename(
    #    columns={'main.temp': 'temp_celsius', 'weather[0].description': 'weather'}


    # Extract the description from the nested weather column
    #df['description'] = df['weather'].apply(lambda x: x[0]['description'] if isinstance(x, list) and len(x) > 0 else None)
    
    # Select and rename the required columns
    cleaned_df = df[['name', 'main.temp', 'main.feels_like']].rename(
        columns={'name': 'city', 'main.temp': 'temperature'}

    )
    return cleaned_df