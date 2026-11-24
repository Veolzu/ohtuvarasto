# ohtuvarasto

[![CI](https://github.com/Veolzu/ohtuvarasto/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Veolzu/ohtuvarasto/actions/workflows/main.yml)

[![codecov](https://codecov.io/github/Veolzu/ohtuvarasto/branch/main/graph/badge.svg?token=LXNSCRR5M0)](https://codecov.io/github/Veolzu/ohtuvarasto)

## Warehouse web app

The Flask application lets you create warehouses, view their stock and capacity,
and add or remove stock. Warehouse data is kept in memory, so it resets when the
application is restarted.

Run the application with:

```sh
uv sync
uv run python src/app.py
```

Then open <http://127.0.0.1:5000> in a browser.

Run the Python and Robot Framework tests with:

```sh
uv run pytest
uv run robot src/tests/robot
```
