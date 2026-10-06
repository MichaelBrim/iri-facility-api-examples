"""
Script to query the state of a PBS job.
TODO: Pass the job ID when calling this script.
"""

import argparse
import json
import requests

from models import Config, Facilities
from utils import get_config, get_headers


# Query the state of a specific PBS job
def get_job(config: Config, job_id: str):
    response = requests.get(
        f"{config.base_url}/compute/status/{config.compute_resource_id}/{job_id}",
        headers=get_headers(config.token),
    )
    return json.dumps(response.json(), indent=2)


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "job_id",
        help="Job ID"
    )
    parser.add_argument(
            "--facility",
            required=True,
            choices=Facilities,
            help="Facility to query",
        )
    args = parser.parse_args()

    print(get_job(get_config(args.facility), args.job_id))
