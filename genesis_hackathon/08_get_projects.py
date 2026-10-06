"""
Script to query projects.
Optional argument to extract a project based on its name.
"""

import argparse
import json
import requests

from models import Config, Facilities
from utils import get_config, get_headers


def get_projects(config: Config, project_name: str = None):

    # Query all projects
    response = requests.get(
        f"{config.base_url}/account/projects",
        headers=get_headers(config.token),
    )
    projects = response.json()

    # Filter to extract a project based on its name
    if project_name is not None:
        projects = [r for r in projects if r["name"].lower() == project_name.lower()]
        
    return json.dumps(projects, indent=2)


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "project_name", 
        nargs="?", 
        help="Project name"
    )
    parser.add_argument(
        "--facility",
        required=True,
        choices=Facilities,
        help="Facility to query",
    )
    args = parser.parse_args()

    print(get_projects(get_config(args.facility), args.project_name))
