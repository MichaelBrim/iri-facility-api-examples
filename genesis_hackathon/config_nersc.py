import os
import sys
from models import Config
from dotenv import load_dotenv
load_dotenv()

# API access
BASE_URL = "https://api.iri.nersc.gov/api/v1"
TOKEN = os.environ.get("IRI_TOKEN_NERSC")
if TOKEN is None:
    print("IRI_TOKEN_NERSC missing in .env file.")
    sys.exit(1)

# Job submission resources
COMPUTE_RESOURCE_ID = "94351904-6dba-4c16-b5cd-fbd280d8615b" # Perlmutter
FILESYSTEM_RESOURCE_ID = "65b28619-c3b6-4942-8da1-044a3b3a2a9e" # Global home

# Job submission parameters
NODES=1
WALLTIME_SEC=300
QUEUE="express_amsc"
COMPUTE_ALLOCATION="amsc013"
STDOUT_PATH="/global/u1/b/bcote/iri_test.out"
STDERR_PATH="/global/u1/b/bcote/iri_test.err"

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
    filters = FILTERS
)