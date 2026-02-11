// script.js

// The API URL from your Render backend
const API_URL = "https://capstone-project-1-3n5w.onrender.com/api/properties/";

// Select the container where properties will be displayed
const propertiesContainer = document.getElementById("properties-container");

// Function to fetch properties
async function fetchProperties() {
  try {
    const response = await fetch(API_URL);

    // Check if the response is OK
    if (!response.ok) {
      throw new Error(`Error: ${response.status} ${response.statusText}`);
    }

    const properties = await response.json();

    // Clear container before rendering
    propertiesContainer.innerHTML = "";

    if (properties.length === 0) {
      propertiesContainer.innerHTML = "<p>No properties found.</p>";
      return;
    }

    // Render each property
    properties.forEach(property => {
      const propertyCard = document.createElement("div");
      propertyCard.classList.add("property-card");

      propertyCard.innerHTML = `
        <h3>${property.title}</h3>
        <p><strong>Price:</strong> $${property.price}</p>
        <p><strong>Location:</strong> ${property.location}</p>
        <p>${property.description}</p>
      `;

      propertiesContainer.appendChild(propertyCard);
    });
  } catch (error) {
    console.error(error);
    propertiesContainer.innerHTML = `<p style="color:red;">Failed to load properties. Try again later.</p>`;
  }
}

// Fetch properties when the page loads
window.addEventListener("DOMContentLoaded", fetchProperties);
