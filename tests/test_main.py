import sys
from pathlib import Path

# Make the src directory importable for this test.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from business_tools.main import get_message


def test_get_message():
    assert get_message() == "Workspace setup successful!"