document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("deals-container").innerHTML = "<p>Enter the number of deals and click 'Show Deals'</p>";
});

function fetchDeals() {
    let dealCount = document.getElementById("deal-count").value;
    if (dealCount < 1) {
        alert("Please enter a valid number of deals!");
        return;
    }

    fetch(`http://127.0.0.1:5000/recommend?n=${dealCount}`)
        .then(response => response.json())
        .then(data => {
            if (!data.recommendations || data.recommendations.length === 0) {
                document.getElementById("deals-container").innerHTML = "<p>No deals available at the moment.</p>";
                return;
            }

            let dealsHTML = "";
            data.recommendations.forEach(deal => {
                dealsHTML += `
                    <div class="deal-card">
                        <img src="${deal.image_url}" alt="${deal.product_name}">
                        <h3>${deal.product_name}</h3>
                        <p>Price: $${deal.price}</p>
                        <p>Category: ${deal.category}</p>
                        <p>Rating: ⭐ ${deal.rating}</p>
                        <a href="${deal.product_link}" target="_blank">
                            <button class="buy-btn" onclick="showConfirmation(event)">Buy Now</button>
                        </a>
                    </div>
                `;
            });

            document.getElementById("deals-container").innerHTML = dealsHTML;
        })
        .catch(error => console.error("Error fetching deals:", error));
}

function showConfirmation(event) {
    event.preventDefault(); // Prevents default action
    document.getElementById("deals-container").style.display = "none";
    document.getElementById("confirmation-message").style.display = "block";
    document.getElementById("home-btn").style.display = "block";

    setTimeout(() => {
        window.location.reload(); // Redirects to home page after 5 sec
    }, 5000);
}
