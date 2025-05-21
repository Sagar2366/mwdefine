import requests
from typing import Optional

MW_ENDPOINT = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={key}"

class MWEntry:
    def __init__(self, entry_dict):
        self.fl = entry_dict.get("fl", "")
        self.shortdef = entry_dict.get("shortdef", [])
        # Pronunciation: try to get first available
        self.pron = ""
        hwi = entry_dict.get("hwi", {})
        if hwi and "prs" in hwi and hwi["prs"]:
            self.pron = hwi["prs"][0].get("mw", "")

def lookup(api_key: str, word: str) -> Optional[MWEntry]:
    url = MW_ENDPOINT.format(word=word, key=api_key)
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code}")
    data = response.json()
    if not data or not isinstance(data, list) or not data or not isinstance(data[0], dict):
        return None
    return MWEntry(data[0])
