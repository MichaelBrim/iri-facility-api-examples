import sys
import config_alcf
import config_nersc
import config_esnet
import config_olcf

from models import Config


def get_config(facility: str) -> Config:
    """Return the config for the target facility."""
    
    facility = facility.lower()

    if facility.lower() == "alcf":
        return config_alcf.config
    elif facility.lower() == "nersc":
        return config_nersc.config
    elif facility.lower() == "esnet":
        return config_esnet.config
    elif facility.lower() == "olcf":
        return config_olcf.config
    else:
        print(f"Facility {facility} not supported yet.")
        sys.exit(1)


def get_headers(token: str) -> dict[str, str]:
    """Return authenticated request headers."""
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
