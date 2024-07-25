console.log("my id {{id}}");
const weatherData = {
    city: "Cape Coast, Ghana",
    date: "Today, 14 July 4:00 PM",
    current: {
        icon: "/static/images/sunny.png",
        temperature: 20,
        description: "Cloudy",
        humidity: "42%",
        precipitation: "10%",
        wind: "18 km/h"
    },
    forecast: [
        { day: "Mon, 15 July", icon: "/static/images/rain.png", temperature: 22 },
        { day: "Tue, 16 July", icon: "/static/images/thunderstorm.png", temperature: 17 },
    ]
};

document.getElementById("city").textContent = weatherData.city;
document.getElementById("date").textContent = weatherData.date;
document.getElementById("current-icon").src = weatherData.current.icon;
document.getElementById("current-temp").textContent = weatherData.current.temperature;
document.getElementById("description").textContent = weatherData.current.description;
document.getElementById("humidity").textContent = weatherData.current.humidity;
document.getElementById("precipitation").textContent = weatherData.current.precipitation;
document.getElementById("wind").textContent = weatherData.current.wind;

const forecastContainer = document.getElementById("forecast-container");
weatherData.forecast.forEach(day => {
    const dayDiv = document.createElement("div");
    dayDiv.className = "day";

    const dayName = document.createElement("span");
    dayName.textContent = day.day;

    const dayIcon = document.createElement("img");
    dayIcon.src = day.icon;

    const dayTemp = document.createElement("span");
    dayTemp.textContent = `${day.temperature}°`;

    dayDiv.appendChild(dayName);
    dayDiv.appendChild(dayIcon);
    dayDiv.appendChild(dayTemp);

    forecastContainer.appendChild(dayDiv);
});
