# Weather Information (Voice Assistant)

A simple Python script that fetches real-time weather data for a city using the WeatherAPI service and reads out the current temperature using text-to-speech.

## Features

- Fetches live temperature data via WeatherAPI
- Voice output using `pyttsx3` (offline text-to-speech)
- Simple command-line interface

## Requirements

- Python 3.x
- `requests`
- `pyttsx3`

Install dependencies:
```bash
pip install requests pyttsx3
```

## Setup

1. Get a free API key from [WeatherAPI](https://www.weatherapi.com/).
2. Set it as an environment variable:

```bash
# Windows
set WEATHER_API_KEY=your_api_key_here

# Linux/macOS
export WEATHER_API_KEY=your_api_key_here
```

## Usage

```bash
git clone https://github.com/AhadAhmad0/Weather-Information.git
cd Weather-Information
python Weather_Information.py
```

Enter a city name when prompted — the script will print and speak the current temperature.

## Author

**Ahad Ahmad** — [@AhadAhmad0](https://github.com/AhadAhmad0)
