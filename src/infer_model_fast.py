import os, sys

root_folder = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
print(f"{root_folder=}")
sys.path.insert(0, root_folder)

import csv
from src.utils.constants import INPUT_PARAMETERS, PREDICTIONS_CSV

# Function to retrieve cached values from the CSV
def predict_parkinsons(input_args):
    with open(PREDICTIONS_CSV, mode="r") as file:
        reader = csv.DictReader(file)
        # Find the matching row
        for row in reader:
            if all(int(row[arg]) == input_args[arg] for arg in INPUT_PARAMETERS):
                return {
                    "has_parkinson": int(row["has_parkinson"]),
                    "confidence": float(row["confidence"])
                }
    return None  # Return None if no match is found

# Example usage
result = predict_parkinsons({
    "tremor": 1,
    "slowness": 1,
    "rigidity": 1,
    "loss_of_smell": 1,
    "family_history": 1,
    "num_ancestors": 1,
    "male_ancestors": 1,
    "past_head_injury": 1
})
print(result)

