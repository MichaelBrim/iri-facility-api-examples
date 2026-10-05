"""
Script to list PBS jobs on a compute resource.
"""

import json
import requests

from config import BASE_URL, HEADERS, COMPUTE_RESOURCE_ID, FILTERS

# Define query parameters
params = {
    "historical": "true", # "true" will include completed jobs
    "limit": 50, # maximum number of jobs returned
    "offset": 0,
}


# Submit request
response = requests.post(
    f"{BASE_URL}/compute/status/{COMPUTE_RESOURCE_ID}",
    params=params,
    json=FILTERS,
    headers=HEADERS,
)
print(json.dumps(response.json(), indent=2))