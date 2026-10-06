"""
Script to query the allocations of a specific project given its ID.
TODO: Pass the project ID when calling this script.
"""

import argparse
import json
import requests

from models import Config, Facilities
from utils import get_config, get_headers


# Query a specific project
def get_allocations(config: Config, project_id: str):
    response = requests.get(
        f"{config.base_url}/account/projects/{project_id}/project_allocations",
        headers=get_headers(config.token),
    )
    return json.dumps(response.json(), indent=2)


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "project_id",
        help="Project ID"
    )
    parser.add_argument(
        "--facility",
        required=True,
        choices=Facilities,
        help="Facility to query",
    )
    args = parser.parse_args()

    print(get_allocations(get_config(args.facility), args.project_id))
