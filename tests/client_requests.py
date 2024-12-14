import requests

def make_request():
    url = "http://127.0.0.1:8095/predict/"
    # url = "http://172.19.193.24/predict/"
    # url = "http://172.19.193.24/"

    payload = {
        "kwargs": {
            "tremor": 1,
            "slowness": 1,
            "rigidity": 1,
            "loss_of_smell": 1,
            "family_history": 1,
            "num_ancestors": 1,
            "male_ancestors": 1,
            "past_head_injury": 1,
        }
    }  # Example payload

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)
    except requests.RequestException as e:
        print("Request failed:", e)

# Run the function
make_request()
