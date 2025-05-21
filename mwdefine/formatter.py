from typing import Optional
from mwdefine.api import MWEntry

def pretty(entry: Optional[MWEntry]) -> str:
    if entry is None:
        return "No definition found."
    pron = entry.pron if entry.pron else "N/A"
    fl = entry.fl if entry.fl else "N/A"
    definition = entry.shortdef[0] if entry.shortdef else "N/A"
    return f"{pron} ({fl}): {definition}"
