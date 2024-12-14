import httpx

async def make_request():
    url = "http://127.0.0.1:8095/predict/"
    payload = {"kwargs": {
        "tremor" : 1,
        "slowness" : 1,
        "rigidity" : 1,
        "loss_of_smell" : 1,
        "family_history" : 1,
        "num_ancestors" : 1,
        "male_ancestors" : 1,
        "past_head_injury" : 1,
    }
    }  # Example payload
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)

# Run the async function
import asyncio
asyncio.run(make_request())
