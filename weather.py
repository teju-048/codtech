import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = '375c6f8493b328d52a2f0c6b10494821'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

def get_current_weather(city):
    url = BASE_URL.format(city, API_KEY)
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'main' not in data:
        raise ValueError("Invalid city name or API issue.")

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['main']
    description = data['weather'][0]['description']
    city_name = data['name']
    country = data['sys']['country']

    return {
        'city': city_name,
        'country': country,
        'temperature': temperature,
        'humidity': humidity,
        'condition': condition,
        'description': description
    }

def plot_current_weather(weather_data):
    sns.set(style="whitegrid")

    # Data to plot
    labels = ['Temperature (°C)', 'Humidity (%)']
    values = [weather_data['temperature'], weather_data['humidity']]
    colors = ['skyblue', 'lightgreen']

    # Create bar plot
    plt.figure(figsize=(8, 5))
    bars = sns.barplot(x=labels, y=values, palette=colors)

    # Annotate values on top of bars
    for i, value in enumerate(values):
        plt.text(i, value + 1, f"{value:.1f}", ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Title and labels
    city_title = f"{weather_data['city']}, {weather_data['country']}"
    plt.title(f"Current Weather in {city_title}\n{weather_data['condition']} ({weather_data['description']})",
              fontsize=14, fontweight='bold')
    plt.ylim(0, max(values) + 20)
    plt.tight_layout()
    plt.show()

def main():
    city = input("Enter city name: ").strip()
    try:
        weather = get_current_weather(city)
        plot_current_weather(weather)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()
