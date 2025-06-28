# bp5.py
import numpy as np
import adios2

def read_all_variables(filename: str) -> dict:
    """
    Read a BP5 file and return a dict of the form:
      {
        var_name: {
          "Step:0": <scalar or list>,
          "Step:1": <…>,
           …
        },
        …
      }
    i.e. all data for each variable, keyed by step.
    """
    result: dict[str, dict[str, any]] = {}
    with adios2.Stream(filename, "r") as s:
        first = True
        for _ in s.steps():
            step = s.current_step()
            avail = s.available_variables()  # var_name → metadata dict
            if first:
                # initialize one entry per variable
                for var in avail.keys():
                    result[var] = {}
                first = False
            for var_name in avail:
                arr = s.read(var_name)
                # scalar?
                if isinstance(arr, np.generic) or (hasattr(arr, "shape") and arr.shape == ()):
                    val = np.array(arr).item()
                else:
                    val = np.array(arr).flatten().tolist()
                result[var_name][f"Step:{step}"] = val
    return result
