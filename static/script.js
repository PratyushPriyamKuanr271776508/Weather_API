document.getElementById('weatherForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const city = document.getElementById('cityInput').value;
    fetch(`/api/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            displayWeather(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

function displayWeather(data) {
    const resultDiv = document.getElementById('weatherResult');
    if (data.error) {
        resultDiv.innerHTML = `<p class="error">${data.error}</p>`;
        return;
    }
    
    resultDiv.innerHTML = `
        <div class="weather-card">
            <img src="http://openweathermap.org/img/wn/${data.icon}@2x.png" class="weather-icon">
            <div>
                <h2>${data.city}, ${data.country}</h2>
                <p>Temperature: ${data.temp}°C (Feels like ${data.feels_like}°C)</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Wind: ${data.wind_speed} m/s</p>
                <p>Conditions: ${data.conditions}</p>
            </div>
        </div>
    `;
}

function exportData(format) {
    const city = document.getElementById('cityInput').value;
    if (!city) {
        alert('Please enter a city first');
        return;
    }
    window.location.href = `/export/${format}?city=${city}`;
}