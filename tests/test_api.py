import os
import pytest
from mwdefine.api import lookup

@pytest.mark.skipif(not os.getenv("MW_API_KEY"), reason="No MW_API_KEY set")
def test_lookup():
    entry = lookup(os.getenv("MW_API_KEY"), "exercise")
    assert entry is not None
    assert isinstance(entry.fl, str)
    assert isinstance(entry.shortdef, list)
