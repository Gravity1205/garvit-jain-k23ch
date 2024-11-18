// Add temperature unit conversion
function convertTemperature(celsius) {
    const fahrenheit = (celsius * 9/5) + 32;
    return fahrenheit;
}

// Add refresh button with animation
function refreshWeather() {
    const refreshBtn = document.querySelector('.refresh-btn');
    refreshBtn.classList.add('spinning');
    // Trigger form submission
    document.querySelector('form').submit();
}

function saveRecentSearch(city) {
    let searches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
    if (!searches.includes(city)) {
        searches.unshift(city);
        searches = searches.slice(0, 5); // Keep only last 5 searches
        localStorage.setItem('recentSearches', JSON.stringify(searches));
    }
} 