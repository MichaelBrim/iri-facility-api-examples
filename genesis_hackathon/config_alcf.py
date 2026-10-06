import os
import sys
from models import Config
from dotenv import load_dotenv
load_dotenv()

# API access
BASE_URL = "https://api.alcf.anl.gov/api/v1"
TOKEN = os.environ.get("IRI_TOKEN_ALCF")
if TOKEN is None:
    print("IRI_TOKEN_ALCF missing in .env file.")
    sys.exit(1)

# Job submission resources
COMPUTE_RESOURCE_ID = "55c1c993-1124-47f9-b823-514ba3849a9a" # Polaris
FILESYSTEM_RESOURCE_ID = "6115bd2c-957a-4543-abff-5fae52992ff2" # Polaris:Home

# Job submission parameters
NODES=1
WALLTIME_SEC=300
QUEUE="debug"
COMPUTE_ALLOCATION="datascience"
STDOUT_PATH="/home/bcote/iri_test.out"
STDERR_PATH="/home/bcote/iri_test.err"

# Commands to be executed in the job
COMMANDS="""
echo Start
sleep 5
whoami
hostname
echo End
"""

# Job list
#FILTERS={"accountingId": "alcf_training", "states": ["completed"]}
FILTERS={}

# Automatic assignment of custom attributes
if COMPUTE_RESOURCE_ID == "55c1c993-1124-47f9-b823-514ba3849a9a" or \
    COMPUTE_RESOURCE_ID == "8b9b42f7-572a-4909-8472-a0453436304c":
    custom_attributes = {"filesystems": "home:eagle"}
elif COMPUTE_RESOURCE_ID == "0325fc07-6fb7-4453-b772-3d5030b2df72":
    custom_attributes = {"filesystems": "flare"}

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
    custom_attributes = custom_attributes,
)
