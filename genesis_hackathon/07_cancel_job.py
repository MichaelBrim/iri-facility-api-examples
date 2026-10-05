"""
Script to cancel a PBS job given its ID.
TODO: Pass the job ID when calling this script.
"""

import argparse
import json
import requests

from config import BASE_URL, HEADERS, COMPUTE_RESOURCE_ID


# Cancel a PBS job
def get_job(job_id):
    response = requests.delete(
        f"{BASE_URL}/compute/cancel/{COMPUTE_RESOURCE_ID}/{job_id}",
        headers=HEADERS,
    )
    if response.status_code == 204:
        return "Cancellation submitted."
    else:
        return json.dumps(response.json(), indent=2)


if __name__ == "__main__":

    # Parse mandatory job_id argument
    parser = argparse.ArgumentParser()
    parser.add_argument("job_id", help="PBS job ID")
    args = parser.parse_args()

    print(get_job(args.job_id))
