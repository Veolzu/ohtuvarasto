"""Flask web interface for managing warehouses."""

import math

from flask import Flask, flash, redirect, render_template, request, url_for

try:
    from .varasto import Varasto
except ImportError:  # Support running with `python src/app.py` as well.
    from varasto import Varasto


def create_app():  # pylint: disable=too-many-statements
    """Create the application and its in-memory warehouse collection."""
    application = Flask(__name__)
    application.config["SECRET_KEY"] = "warehouse-app-development-key"
    application.config["WAREHOUSES"] = []

    @application.get("/")
    def index():
        return render_template(
            "index.html", warehouses=application.config["WAREHOUSES"]
        )

    @application.post("/warehouses")
    def create_warehouse():  # pylint: disable=too-many-statements
        name = request.form.get("name", "").strip()
        capacity_text = request.form.get("capacity", "").strip()
        try:
            capacity = float(capacity_text)
        except ValueError:
            capacity = 0

        if not name:
            flash("Enter a name for the warehouse.", "error")
        elif not math.isfinite(capacity) or capacity <= 0:
            flash("Capacity must be a number greater than zero.", "error")
        else:
            warehouses = application.config["WAREHOUSES"]
            warehouses.append({
                "id": len(warehouses) + 1,
                "name": name,
                "stock": Varasto(capacity),
            })
            flash(f"Warehouse {name} was created.", "success")

        return redirect(url_for("index"))

    @application.post("/warehouses/<int:warehouse_id>/<action>")
    def update_stock(warehouse_id, action):  # pylint: disable=too-many-statements
        warehouse = next(
            (
                item for item in application.config["WAREHOUSES"]
                if item["id"] == warehouse_id
            ),
            None,
        )
        if warehouse is None:
            flash("Warehouse not found.", "error")
            return redirect(url_for("index"))

        amount_text = request.form.get("amount", "").strip()
        try:
            amount = float(amount_text)
        except ValueError:
            amount = 0

        if action not in ("add", "take"):
            flash("Unknown stock operation.", "error")
        elif not math.isfinite(amount) or amount <= 0:
            flash("Amount must be a number greater than zero.", "error")
        elif action == "add":
            warehouse["stock"].lisaa_varastoon(amount)
            flash(f"Added {amount:g} to {warehouse['name']}.", "success")
        else:
            taken = warehouse["stock"].ota_varastosta(amount)
            flash(f"Removed {taken:g} from {warehouse['name']}.", "success")

        return redirect(url_for("index"))

    return application


flask_app = create_app()


if __name__ == "__main__":
    flask_app.run()
