"""API module for interacting with Merriam-Webster Collegiate Dictionary."""

from typing import Optional
import requests

MW_ENDPOINT = (
    "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
    "{word}?key={key}"
)


class MWEntry:
    """Represents a dictionary entry from Merriam-Webster API."""

    def __init__(self, entry_dict):
        """
        Initialize an MWEntry object.

        Args:
            entry_dict (dict): A dictionary containing entry data from the API.
        """
        self.fl = entry_dict.get("fl", "")
        self.shortdef = entry_dict.get("shortdef", [])
        # Pronunciation: try to get first available
        self.pron = ""
        hwi = entry_dict.get("hwi", {})
        if hwi and "prs" in hwi and hwi["prs"]:
            self.pron = hwi["prs"][0].get("mw", "")


def lookup(api_key: str, word: str) -> Optional[MWEntry]:
    """
    Look up the definition of a word from the Merriam-Webster API.

    Args:
        api_key (str): Merriam-Webster API key.
        word (str): Word to define.

    Returns:
        Optional[MWEntry]: An MWEntry object if found, else None.
    """
    url = MW_ENDPOINT.format(word=word, key=api_key)
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code}")
    data = response.json()
    if (
        not data
        or not isinstance(data, list)
        or not data
        or not isinstance(data[0], dict)
    ):
        return None
    return MWEntry(data[0])
