import os, sys

root_folder = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
print(f"{root_folder=}")
sys.path.insert(0, root_folder)

from src.utils.constants import INPUT_PARAMETERS, PREDICTIONS_CSV
from src.infer_model import predict_parkinsons
import csv
from itertools import product

# Generate all possible combinations of inputs
combinations = list(product([0, 1], repeat=len(INPUT_PARAMETERS)))

# Write to CSV
PREDICTIONS_CSV = "data/parkinsons_predictions.csv"
with open(PREDICTIONS_CSV, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(INPUT_PARAMETERS + ["has_parkinson", "confidence"])

    # Write each combination and prediction result
    for combo in combinations:
        kwargs = dict(zip(INPUT_PARAMETERS, combo))
        prediction = predict_parkinsons(kwargs)
        writer.writerow(list(combo) + [prediction["has_parkinson"], prediction["confidence"]])


"""
"tremor", "slowness", "rigidity", "loss_of_smell", "family_history", "num_ancestors", "male_ancestors", "past_head_injury"

I've got these 8 INPUT_PARAMETERS, which can take up the values 1 or 0, create all possible input combinations for the same.

I've got another function called predict_parkinsons(kwargs) which inputs a dictionary with keys as above and values as 0 and 1.

This function returns a dict -> 2 values in a dict "has_parkinson" : 1 or 0, and "confidence" = float,

Create a csv with headers "tremor", "slowness", "rigidity", "loss_of_smell", "family_history", "num_ancestors", "male_ancestors", "past_head_injury", "has_parkinson", "confidence"

Save it to a csv (using python's internal csv writer).

Once done, make a function return_cached_values_from_csv which replicates predict_parkinsons behaviour -> takes the input args and gives the "has_parkinson" : 1 or 0, and "confidence" = float, BUT NOW from the csv.

"""