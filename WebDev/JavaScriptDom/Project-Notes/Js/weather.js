
// WEATHER COMPONENTS


// VARIABLES

const cityTitle = document.getElementById('heading-city');
const searchCity = document.getElementById('search-city');
const searchBtnCity = document.getElementById('search-btn');
const h2 = document.getElementById('h2');
const paragraph = document.getElementById('paragraph');
const weatherBtn = document.getElementById('weather-btn');
const windBtn = document.getElementById('wind-btn');
const temperatureBtn = document.getElementById('temperature-btn');
const timeBtn = document.getElementById('time-btn');


navigator.geolocation.getCurrentPosition(
    async function(position) {
        try {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            
            console.log("Coordinates:", lat, lon);
            
            const response = await fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json`);
            const data = await response.json();
            let city = data.address.city || data.address.town || data.address.village || data.address.suburb || "Unknown Location";
            
            cityTitle.innerText = city;
            
            const dataResponse = await fetch(
                `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true&timezone=auto`
            );
            
            console.log("Response OK:", dataResponse.ok);
            
            if (!dataResponse.ok) {
                const error = await dataResponse.text();
                console.error("API Error:", error);
                return;
            }
            
            const weather = await dataResponse.json();
            console.log("Weather:", weather);
            
            const weatherCodeNum = weather.current_weather?.weathercode;
            console.log("Weather Code:", weatherCodeNum);
            
            const result = getWeatherDescription(weatherCodeNum);
            h2.innerText = `The Weather Condition here in the ${city} City.`;
            paragraph.innerText = result;

        } catch (error) {
            console.log("Error:", error);
        }
    },
    function(error) {
        cityTitle.innerText = 'Search for a city';
    }
)



async function getCoordinates(cityName) {

    try {

        const response = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${cityName}&count=1&language=en&format=json`);
        const position = await response.json();
        return position;

    } catch (error) {



    }

}

async function getWeather(position) {

    try {
        const latitude = position.results[0].latitude;
        const longitude = position.results[0].longitude;
        const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true&hourly=relativehumidity_2m,visibility_10m&timezone=auto`);
        const weather = await response.json();
        return weather;
    } catch (error) {
        
    }

}


function getWeatherDescription(weatherCode) {

    const staticWeather = {
        0: "The sky is clear and sunny today!",
        1: "It's mostly clear with a few clouds scattered around.",
        2: "Partly cloudy skies with sun peeking through the clouds.",
        3: "The sky is completely covered with clouds today."
    };

    if (staticWeather[weatherCode] !== undefined) {
        return staticWeather[weatherCode];
    }

    // 2. Handle ranges and specific codes cleanly
    if (weatherCode >= 45 && weatherCode <= 48) {
        return "Foggy conditions - visibility is low today.";
    }
    
    if (weatherCode >= 51 && weatherCode <= 57) {
        if (weatherCode >= 56) return "Freezing drizzle - cold rain freezing on surfaces!";
        if (weatherCode === 55) return "Dense drizzle - steady light rain covering everything.";
        if (weatherCode === 53) return "Moderate drizzle - consistent light rain falling.";
        return "Light drizzle falling - a gentle misty rain.";
    }

    if (weatherCode >= 61 && weatherCode <= 67) {
        if (weatherCode >= 66) return "Freezing rain - dangerous icy rain conditions!";
        if (weatherCode === 65) return "Heavy rain - strong rainfall, bring your umbrella!";
        if (weatherCode === 63) return "Moderate rain - steady rainfall continuing.";
        return "Light rain falling - a gentle shower today.";
    }

    if (weatherCode >= 71 && weatherCode <= 77) {
        if (weatherCode === 77) return "Snow grains - tiny ice crystals falling like snow.";
        if (weatherCode === 75) return "Heavy snow - strong snowfall today!";
        if (weatherCode === 73) return "Moderate snow - steady snowfall continuing.";
        return "Light snow falling - gentle snowflakes drift down.";
    }

    if (weatherCode >= 80 && weatherCode <= 82) {
        if (weatherCode === 82) return "Violent rain showers - intense rain bursts!";
        if (weatherCode === 81) return "Moderate rain showers - regular bursts of rain.";
        return "Light rain showers - brief periods of light rain.";
    }

    if (weatherCode >= 85 && weatherCode <= 86) {
        if (weatherCode === 86) return "Heavy snow showers - strong snow bursts!";
        return "Light snow showers - brief snow flurries.";
    }

    if (weatherCode >= 95 && weatherCode <= 99) {
        if (weatherCode === 99) return "Thunderstorm with heavy hail - dangerous!";
        if (weatherCode === 96) return "Thunderstorm with light hail - thunder and lightning!";
        return "Thunderstorm approaching - thunder and lightning out there!";
    }

    return "Weather conditions unknown.";
}



