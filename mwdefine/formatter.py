"""Formatter for Merriam-Webster dictionary entries."""

from typing import Optional
from mwdefine.api import MWEntry


def pretty(entry: Optional[MWEntry]) -> str:
    """
    Format an MWEntry object into a user-friendly string.

    Args:
        entry (Optional[MWEntry]): The dictionary entry to format.

    Returns:
        str: Formatted string or a message if entry is None.
    """
    if entry is None:
        return "No definition found."
    pron = entry.pron if entry.pron else "N/A"
    fl = entry.fl if entry.fl else "N/A"
    definition = entry.shortdef[0] if entry.shortdef else "N/A"
    return f"{pron} ({fl}): {definition}"