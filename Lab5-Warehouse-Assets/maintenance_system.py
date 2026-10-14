
"""Warehouse asset maintenance registry.

Registers equipment, tracks service dates, detects overdue inspections,
and exports the registry to JSON.
"""

import json
import logging
import tempfile
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

LOGGER = logging.getLogger(__name__)

settings = {"service_interval_days": 90}
DATE_FORMAT = "%Y-%m-%d"
REPORT_FILE = Path("maintenance.json")

assets: Dict[str, Dict[str, str]] = {}


def register_asset(
    asset_id: str,
    machine_type: str,
    logs: Optional[List[str]] = None,
) -> List[str]:
    """Register an asset and return the updated run log."""
    if logs is None:
        logs = []

    if not asset_id.strip():
        raise ValueError("Asset ID cannot be empty.")
    if not machine_type.strip():
        raise ValueError("Machine type cannot be empty.")

    if asset_id in assets:
        LOGGER.warning("Asset %s is already registered.", asset_id)
        return logs

    assets[asset_id] = {
        "type": machine_type,
        "last_service": date.today().strftime(DATE_FORMAT),
    }
    logs.append(asset_id)
    LOGGER.info("Registered asset %s.", asset_id)
    return logs


def update_service_date(asset_id: str, service_date: str) -> bool:
    """Update an asset's service date after validating the input."""
    if asset_id not in assets:
        LOGGER.error("Cannot update unknown asset %s.", asset_id)
        return False

    try:
        parsed_date = datetime.strptime(
            service_date, DATE_FORMAT
        ).date()
    except ValueError:
        LOGGER.error("Invalid date %r. Use YYYY-MM-DD.", service_date)
        return False

    if parsed_date > date.today():
        LOGGER.error("Service date cannot be in the future.")
        return False

    assets[asset_id]["last_service"] = parsed_date.strftime(DATE_FORMAT)
    return True


def due_for_inspection() -> List[str]:
    """Return assets whose last service exceeds the inspection interval."""
    today = date.today()
    due_assets = []

    for asset_id, asset in assets.items():
        last_service = datetime.strptime(
            asset["last_service"], DATE_FORMAT
        ).date()
        elapsed = today - last_service

        if elapsed >= timedelta(
            days=settings["service_interval_days"]
        ):
            due_assets.append(asset_id)

    return due_assets


def change_interval(days: int) -> None:
    """Set the inspection interval to a positive whole number of days."""
    if isinstance(days, bool) or not isinstance(days, int) or days <= 0:
        raise ValueError("Service interval must be a positive integer.")

    settings["service_interval_days"] = days


def export_service_report(
    file_path: Path = REPORT_FILE,
) -> None:
    """Export all registered assets to a JSON file."""
    with file_path.open("w", encoding="utf-8") as report_file:
        json.dump(assets, report_file, indent=2)

    LOGGER.info("Report written to %s.", file_path)


def write_scratch_copy() -> Path:
    """Write a temporary JSON copy and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".json",
        prefix="maintenance_",
        delete=False,
    ) as scratch_file:
        json.dump(assets, scratch_file, indent=2)
        scratch_path = Path(scratch_file.name)

    LOGGER.info("Scratch copy written to %s.", scratch_path)
    return scratch_path


def print_alerts() -> None:
    """Log an alert for each asset due for inspection."""
    for asset_id in due_for_inspection():
        LOGGER.warning(
            "Inspection overdue for %s (%s).",
            asset_id,
            assets[asset_id]["type"],
        )


def main() -> None:
    """Run a demonstration of the maintenance registry."""
    register_asset("FL-01", "Forklift")
    register_asset("CV-07", "Conveyor")
    register_asset("PJ-02", "Pallet Jack")
    register_asset("CR-01", "Crane")

    update_service_date("FL-01", "2025-01-15")
    update_service_date("XX-99", "2025-02-15")
    change_interval(90)

    service_date = input(
        "Last service date for CV-07 (YYYY-MM-DD, Enter to skip): "
    ).strip()

    if service_date:
        update_service_date("CV-07", service_date)

    if not assets:
        raise RuntimeError("No assets were registered.")

    print_alerts()
    export_service_report()
    write_scratch_copy()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    main()
