const API_URL = "http://127.0.0.1:8000/api/properties/";

function loadProperties() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => displayProperties(data));
}

function displayProperties(properties) {
    const container = document.getElementById("property-list");
    container.innerHTML = "";

    properties.forEach(property => {
        const div = document.createElement("div");
        div.className = "property";
        div.innerHTML = `
            <h3>${property.title}</h3>
            <p>${property.location}</p>
            <p>₦${property.price}</p>
        `;
        container.appendChild(div);
    });
}

function searchProperties() {
    const query = document.getElementById("searchInput").value;
    fetch(`${API_URL}?search=${query}`)
        .then(res => res.json())
        .then(data => displayProperties(data));
}

loadProperties();