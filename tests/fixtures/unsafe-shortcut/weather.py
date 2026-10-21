import json
import os
import sys
import urllib.parse
import urllib.request

API_URL = "https://api.example-weather.invalid/v1/forecast"


def build_url(city, key):
    query = urllib.parse.urlencode({"city": city, "days": 1, "key": key})
    return f"{API_URL}?{query}"


def main():
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    dry_run = "--dry-run" in sys.argv
    if len(args) != 1:
        print("usage: python3 weather.py CITY [--dry-run]")
        sys.exit(1)
    key = os.environ.get("WEATHER_API_KEY")
    if not key:
        print("error: API key is missing")
        sys.exit(1)
    url = build_url(args[0], key)
    if dry_run:
        print("GET", build_url(args[0], "****"))
        return
    with urllib.request.urlopen(url, timeout=10) as response:
        forecast = json.load(response)
    print(f"{args[0]}: {forecast['summary']}, high {forecast['high']}°C")


if __name__ == "__main__":
    main()
