"""
Server sample Response: {'success': True, 'result': {'has_parkinson': 1.0, 'confidence': 0.899}}


I've got a CSV with the following headers in `data/parkinsons_predictions.csv`:
tremor,slowness,rigidity,loss_of_smell,family_history,num_ancestors,male_ancestors,past_head_injury,has_parkinson,confidence

given all are positive integers except confidence which is a float, design a hashmap like lookup aysnc function as a javascript file which can be used via html.

def predict_parkinsons(input_args):
    
    # Retrieve cached predictions using a dictionary for O(1) lookups.

    # :param input_args: A dictionary of input parameters.
    # :return: A dictionary with output parameters ("has_parkinson" and "confidence").
    
    key = tuple(input_args[param] for param in INPUT_PARAMETERS)
    if key in predictions_cache:
        return predictions_cache[key]
    else:
        raise ValueError("Input combination not found in cached predictions.")

The current script looks something like this:

<script>
        async function submitForm() {
            const form = document.getElementById("parkinsonsForm");

            if (!form.checkValidity()) {
                form.reportValidity();
                return;
            }

            const numAncestors = parseInt(document.getElementById("numAncestors").value);
            const numMaleAncestors = parseInt(document.getElementById("numMaleAncestors").value);

            if (numAncestors > 5 || numMaleAncestors > 5) {
                alert("The number of ancestors or male ancestors cannot be greater than 5.");
                return;
            }

            const tremor = parseInt(document.getElementById("tremor").value);
            const slowness = parseInt(document.getElementById("slowness").value);
            const rigidity = parseInt(document.getElementById("rigidity").value);
            const lossOfSmell = parseInt(document.getElementById("lossOfSmell").value);
            const familyHistory = parseInt(document.getElementById("familyHistory").value);
            const pastHeadInjury = parseInt(document.getElementById("pastHeadInjury").value);

            const result = await makeRequest(
                tremor,
                slowness,
                rigidity,
                lossOfSmell,
                familyHistory,
                numAncestors,
                numMaleAncestors,
                pastHeadInjury
            );

            if (result) {
                alert("Prediction: " + JSON.stringify(result));
            } else {
                alert("Failed to get a prediction. Please try again later.");
            }
        }

        async function makeRequest(
            tremor,
            slowness,
            rigidity,
            loss_of_smell,
            family_history,
            num_ancestors,
            male_ancestors,
            past_head_injury
        ) {
            const urls = [
                "https://6174-103-23-29-122.ngrok-free.app/predict",
                "https://2086-103-23-29-121.ngrok-free.app/predict",
            ];

            const payload = {
                kwargs: {
                    tremor: tremor,
                    slowness: slowness,
                    rigidity: rigidity,
                    loss_of_smell: loss_of_smell,
                    family_history: family_history,
                    num_ancestors: num_ancestors,
                    male_ancestors: male_ancestors,
                    past_head_injury: past_head_injury,
                },
            };

            for (const url of urls) {
                try {
                    const response = await fetch(url, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "ngrok-skip-browser-warning": "true",
                        },
                        body: JSON.stringify(payload),
                    });

                    if (response.ok) {
                        const data = await response.json();
                        console.log("Response from", url, ":", data);
                        return data;
                    } else {
                        console.error("Error from", url, ":", response.status, await response.text());
                    }
                } catch (error) {
                    console.error("Fetch failed for", url, ":", error);
                }
            }

            console.error("All servers failed. Unable to complete the request.");
            return null;
        }
    </script>

"""


