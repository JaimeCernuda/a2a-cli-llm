from adios2 import FileReader


def inspect_variables(filename: str) -> dict[str, dict]:
    """
    Discover all variables in a BP5 file.
    Returns a dict mapping each variable name to its metadata:
      - "Shape": global dimensions as a string
      - "Type": ADIOS data type as a string
      - "AvailableStepsCount": number of timesteps written
      - any additional ADIOS Params
    """
    # Open in read mode
    with FileReader(filename) as stream:
        vars_info = stream.available_variables()
        # Convert ADIOS Params to plain dicts for JSON serialization
        return {name: dict(info) for name, info in vars_info.items()}