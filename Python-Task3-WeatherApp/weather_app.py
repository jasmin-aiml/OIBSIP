import sys

def simulate_meteorological_client():
    print("===================================================")
    print("         METEOROLOGICAL TELEMETRY CLIENT           ")
    print("===================================================\n")
    
    target_city = input("Query location network identity (City Name): ").strip()
    
    if not target_city:
        print("❌ Process termination: Empty geographic identifier field.")
        return

    print(f"\n📡 Opening simulated api endpoint connection for: {target_city}...")
    print("📥 Stream connection established. Parsing telemetry metrics...\n")
    
    parsed_payload = {
        "coord": {"lon": 78.4744, "lat": 17.3753},
        "weather": {"main": "Scattered Clouds", "description": "scattered low-altitude altocumulus clouds"},
        "main": {"temp": 29.5, "feels_like": 32.1, "humidity": 68, "pressure": 1011},
        "wind": {"speed": 4.1, "deg": 240},
        "sys": {"country": "IN"}
    }

    location_label = target_city.upper()
    condition_profile = parsed_payload['weather']['description']
    thermal_reading = parsed_payload['main']['temp']
    perceived_thermal = parsed_payload['main']['feels_like']
    moisture_ratio = parsed_payload['main']['humidity']
    barometric_stat = parsed_payload['main']['pressure']
    velocity_reading = parsed_payload['wind']['speed']

    print("===================================================")
    print(f" METEOROLOGICAL TELEMETRY REPORT: {location_label} ")
    print("===================================================")
    print(f" 📑 Atmosphere Profile  : {condition_profile.title()}")
    print(f" 🌡️ Core Temperature   : {thermal_reading}°C")
    print(f" 🧪 Apparent Thermal   : {perceived_thermal}°C")
    print(f" 💧 Moisture Saturation: {moisture_ratio}%")
    print(f" 🌀 Barometric Metrics : {barometric_stat} hPa")
    print(f" 💨 Kinetic Wind Vector: {velocity_reading} m/s")
    print("===================================================")

if __name__ == "__main__":
    simulate_meteorological_client()

