
from pydantic import Field
from pydantic_settings import BaseSettings

from dotenv import load_dotenv
load_dotenv(".env")
load_dotenv(".env.secret", override=True)


class Settings(BaseSettings):

    # API access
    base_url: str = Field(min_length=1)
    iri_api_token: str = Field(min_length=1)

    # Job submission
    nodes: int = Field(ge=1)
    walltime_sec: int = Field(ge=300)
    queue: str = Field(min_length=1)
    compute_allocation: str = Field(min_length=1)
    stdout_path: str = Field(min_length=1)
    stderr_path: str = Field(min_length=1)
    compute_resource_id: str = Field(min_length=1)


    class SettingsConfigDict:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"


# Load and validate environment variables
settings = Settings()
BASE_URL = settings.base_url
IRI_API_TOKEN = settings.iri_api_token
NODES = settings.nodes
WALLTIME_SEC = settings.walltime_sec
QUEUE = settings.queue
COMPUTE_ALLOCATION = settings.compute_allocation
STDOUT_PATH = settings.stdout_path
STDERR_PATH = settings.stderr_path
COMPUTE_RESOURCE_ID = settings.compute_resource_id

# Headers for authenticated requests
HEADERS = {
    "Authorization": f"Bearer {IRI_API_TOKEN}",
    "Content-Type": "application/json"
}