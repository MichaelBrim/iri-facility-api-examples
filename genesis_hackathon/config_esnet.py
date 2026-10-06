import os
import sys
from pathlib import Path
from models import Config
from dotenv import load_dotenv
load_dotenv()

# API access
# ESnet accepts AmSC tokens (PATs) on its v2 API only; v1 does not.
BASE_URL = "https://iri-dev.ppg.es.net/api/v2"
TOKEN = os.environ.get("AMSC_TOKEN")
if TOKEN is None:
    token_file = Path(os.environ.get("AMSC_TOKEN_FILE", "/tmp/amsc-token.txt"))
    if token_file.is_file():
        TOKEN = token_file.read_text().strip()
if not TOKEN:
    print("AMSC_TOKEN missing in .env file (or set AMSC_TOKEN_FILE to a file containing the AmSC token).")
    sys.exit(1)

# Job submission resources
COMPUTE_RESOURCE_ID = "fb0aafe1-c780-55c0-b635-a7121f1b0ce5" # Low Priority compute
FILESYSTEM_RESOURCE_ID = "b6d59ba3-5c2d-57dd-b3b9-108832da0578" # Storage

# Job submission parameters
# ESnet schedules jobs with Kueue: QUEUE and COMPUTE_ALLOCATION are accepted but not used.
NODES=1
WALLTIME_SEC=300
QUEUE="default"
COMPUTE_ALLOCATION="hackathon2610-project"
STDOUT_PATH="/data/home/hackathon2610/iri_test.out"
STDERR_PATH="/data/home/hackathon2610/iri_test.err"

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
