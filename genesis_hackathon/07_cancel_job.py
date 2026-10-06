"""
Script to cancel a PBS job given its ID.
TODO: Pass the job ID when calling this script.
"""

import argparse
import json
import requests

from models import Config, Facilities
from utils import get_config, get_headers


# Cancel a PBS job
def get_job(config: Config, job_id: str):
    response = requests.delete(
        f"{config.base_url}/compute/cancel/{config.compute_resource_id}/{job_id}",
        headers=get_headers(config.token),
    )
    if response.status_code == 204:
        return "Cancellation submitted."
    else:
        return json.dumps(response.json(), indent=2)


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "job_id",
        help="PBS job ID"
    )
    parser.add_argument(
        "--facility",
        required=True,
        choices=Facilities,
        help="Facility to query",
    )
    args = parser.parse_args()

    print(get_job(get_config(args.facility), args.job_id))
