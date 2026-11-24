"""Small Robot Framework library that drives Flask's in-process test client."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import create_app  # pylint: disable=wrong-import-position

_app = create_app()
_client = _app.test_client()


def reset_warehouses():
    """Start a test with an empty warehouse list."""
    _app.config["WAREHOUSES"].clear()


def get_warehouse_page():
    """Return the rendered warehouse page."""
    return _client.get("/").get_data(as_text=True)


def create_warehouse(name, capacity):
    """Create a warehouse through the public form endpoint."""
    response = _client.post(
        "/warehouses",
        data={"name": name, "capacity": capacity},
        follow_redirects=True,
    )
    return response.get_data(as_text=True)


def add_stock(warehouse_id, amount):
    """Add stock through the public form endpoint."""
    response = _client.post(
        f"/warehouses/{warehouse_id}/add",
        data={"amount": amount},
        follow_redirects=True,
    )
    return response.get_data(as_text=True)


def remove_stock(warehouse_id, amount):
    """Remove stock through the public form endpoint."""
    response = _client.post(
        f"/warehouses/{warehouse_id}/take",
        data={"amount": amount},
        follow_redirects=True,
    )
    return response.get_data(as_text=True)
