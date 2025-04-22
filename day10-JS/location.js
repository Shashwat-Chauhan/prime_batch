const getData = async (text) => {
    try {
        const response = await fetch(`https://google-map-places.p.rapidapi.com/maps/api/place/autocomplete/json?input=${text}&language=en&region=en`, {
            headers: {
                'x-rapidapi-key': 'b3046c52eemsh42e22e651234629p1d1d45jsn67b6719b702b',
                'x-rapidapi-host': 'google-map-places.p.rapidapi.com'
            }
        });

        const data = await response.json();
        showLocations(data);
    } catch (error) {
        console.error("Error fetching locations:", error);
    }
};

const root = document.querySelector('#locations');

const showLocations = (data) => {
    root.innerHTML = '';
    const { predictions } = data;

    if (!predictions || predictions.length === 0) {
        root.style.display = "none";
        return;
    }

    predictions.forEach((elem) => {
        const p = document.createElement("p");
        p.classList.add("location-item");
        p.innerText = elem.description;
        p.onclick = () => selectLocation(elem.description);
        root.appendChild(p);
    });

    root.style.display = "block";
};

const selectLocation = (location) => {
    document.querySelector("#search-input").value = location;
    root.style.display = "none";
};

let timeoutId = null;

const handleSearch = (e) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
        const query = e.target.value.trim();
        if (query === "") {
            root.innerHTML = "";
            root.style.display = "none";
            return;
        }
        getData(query);
    }, 1000);
};

// Hide results when clicking outside
document.addEventListener("click", (event) => {
    if (!event.target.closest("nav")) {
        root.style.display = "none";
    }
});
