ngrok http http://localhost:8095

const urls = [
    "https://6174-103-23-29-122.ngrok-free.app/predict",
    "https://2086-103-23-29-121.ngrok-free.app/predict",
];

Installation:
pip install -r requirements_reduced.txt
python main.py


Todos:
- Handle the error case in app elegantly (all servers errored)
- Popup doesnt look nice - need to improve
- Integrate `data/parkinsons_predictions.csv` in your app.