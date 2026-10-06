import os
import sys
from models import Config
from dotenv import load_dotenv
load_dotenv()

# API access
BASE_URL = "..."
TOKEN = os.environ.get("IRI_TOKEN_OLCF")
if TOKEN is None:
    print("IRI_TOKEN_OLCF missing in .env file.")
    sys.exit(1)

# Job submission resources
COMPUTE_RESOURCE_ID = "..."
FILESYSTEM_RESOURCE_ID = "..." 

# Job submission parameters
NODES=1
WALLTIME_SEC=300
QUEUE="..."
COMPUTE_ALLOCATION="..."
STDOUT_PATH="..."
STDERR_PATH="..."

# Commands to be executed in the job
COMMANDS="""
echo Start
sleep 5
whoami
hostname
echo End
"""

# Job list
FILTERS={}

config = Config(
    base_url=BASE_URL,
    token=TOKEN,
    compute_resource_id = COMPUTE_RESOURCE_ID,
    filesystem_resource_id = FILESYSTEM_RESOURCE_ID,
    nodes = NODES,
    walltime_sec = WALLTIME_SEC,
    queue = QUEUE,
    compute_allocation = COMPUTE_ALLOCATION,
    stdout_path = STDOUT_PATH,
    stderr_path = STDERR_PATH,
    commands = COMMANDS,
    filters = FILTERS,
)
