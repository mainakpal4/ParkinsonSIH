// const fetch = require('node-fetch'); // Import fetch for Node.js

async function makeRequest(tremor, slowness, rigidity, loss_of_smell, family_history, num_ancestors, male_ancestors, past_head_injury) {
    const url = "http://127.0.0.1:8095/predict/";
    const payload = {
        kwargs: {
            // feature1: feature1,
            // feature2: feature2
            tremor: tremor,
            slowness: slowness,
            rigidity: rigidity,
            loss_of_smell: loss_of_smell,
            family_history: family_history,
            num_ancestors: num_ancestors,
            male_ancestors: male_ancestors,
            past_head_injury: past_head_injury
        }
    };

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Response:", data);
        } else {
            console.error("Error:", response.status, await response.text());
        }
    } catch (error) {
        console.error("Fetch failed:", error);
    }
}

// Sample call to the function
makeRequest(1, 1, 1, 1, 1, 1, 1, 1,);

// {/* <script src="client.js"></script> */}