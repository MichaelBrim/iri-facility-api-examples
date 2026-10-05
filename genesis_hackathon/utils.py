import sys

def get_custom_attributes(resource_id: str) -> dict[str,str]:
    """Create facility-specific attributes."""

    # ALCF
    if resource_id == "55c1c993-1124-47f9-b823-514ba3849a9a" or \
       resource_id == "8b9b42f7-572a-4909-8472-a0453436304c":
        return {"filesystems": "home:eagle"}
    elif resource_id == "0325fc07-6fb7-4453-b772-3d5030b2df72":
        return {"filesystems": "flare"}
    
    return {}


def get_filesystem_id_from_path(
        base_url:str,
        file_path: str,
    ) -> str | None:
    """Automatically find filesystem ID."""

    # ALCF
    if "alcf.anl.gov" in base_url:
        if file_path.startswith("/home/"):
            return "6115bd2c-957a-4543-abff-5fae52992ff2"
        elif file_path.startswith("/eagle/") or file_path.startswith("/lus/eagle/"):
            return "1c3ad9d4-2e91-42bc-becb-72b1fde1235c"
        else:
            print("File must be on /home/, /eagle/, or /lus/eagle/.")
            sys.exit(1)

    # NERS
    if "nersc.gov" in base_url:
        if file_path.startswith("/global/u1"):
            return "65b28619-c3b6-4942-8da1-044a3b3a2a9e"
        else:
            print("File must be on /global/u1/.")
            sys.exit(1)

    print("Target filesystem not implemented in get_filesystem_id_from_path.")
    sys.exit(1)
