"""
Submit a job to a compute resource and get the job ID back.
"""

import json
import requests

from config import (
    HEADERS,
    BASE_URL,
    NODES,
    WALLTIME_SEC,
    QUEUE,
    COMPUTE_ALLOCATION,
    STDOUT_PATH,
    STDERR_PATH,
    COMPUTE_RESOURCE_ID,
)
from utils import get_custom_attributes


# Define commands to be executed
COMMANDS="""
echo Start
sleep 5
whoami
hostname
echo End
"""


# Submit job to compute resource
response = requests.post(
    f"{BASE_URL}/compute/job/{COMPUTE_RESOURCE_ID}",
    json={
        "executable": "/bin/bash",
        "arguments": ["-lc", COMMANDS],
        "name": "my-job",
        "stdout_path": STDOUT_PATH,
        "stderr_path": STDERR_PATH,
        "resources": {
            "node_count": NODES
        },
        "attributes": {
            "duration": WALLTIME_SEC,
            "queue_name": QUEUE,
            "account": COMPUTE_ALLOCATION,
            "custom_attributes": get_custom_attributes(COMPUTE_RESOURCE_ID)
        }
    },
    headers=HEADERS
)

# Print job submission details with the job ID (or error if any) 
print(json.dumps(response.json(), indent=2))