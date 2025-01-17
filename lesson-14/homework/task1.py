from bs4 import BeautifulSoup
import statistics

# Load HTML file
with open("D:\pythonProject\PythonHometasks\lesson-14\homework\weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract weather forecast data
weather_data = []
rows = soup.find("table").find("tbody").find_all("tr")
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append((day, temp, condition))

# Display weather data
print("Weather Forecast:")
for day, temp, condition in weather_data:
    print(f"{day}: {temp}°C, {condition}")

# Find highest temperature day(s)
max_temp = max(weather_data, key=lambda x: x[1])[1]
hottest_days = [day for day, temp, _ in weather_data if temp == max_temp]
print(f"\nHottest Day(s): {', '.join(hottest_days)} with {max_temp}°C")

# Find days with "Sunny" condition
sunny_days = [day for day, _, condition in weather_data if condition.lower() == "sunny"]
print(f"Sunny Day(s): {', '.join(sunny_days)}")

# Calculate average temperature
avg_temp = statistics.mean(temp for _, temp, _ in weather_data)
print(f"\nAverage Temperature: {avg_temp:.2f}°C")
