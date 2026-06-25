import csv

from src.pipeline.row_processor import process_row
from src.mappings.registry import MAPPINGS, SCHEMAS
from src.observability.error_summary import build_error_summary
from src.observability.exporter import export_json, export_text
from src.observability.debug_report import build_debug_report
from src.observability.serializer import to_json_safe


def process_csv(file_path: str, source: str = "google_ads"):
    """
    Batch ingestion orchestrator (JSON-safe contract version)
    """

    try:
        mapping = MAPPINGS[source]
        schema = SCHEMAS[source]
    except KeyError:
        raise ValueError(f"Unknown source: {source}")

    valid_rows = []
    errors = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):

            result = process_row(
                row=row,
                mapping=mapping,
                row_index=i,
                source=source,
                schema=schema,
            )

            if result["valid"]:
                valid_rows.append(result["data"])
            else:
                errors.extend(result.get("errors", []))

    # =========================
    # CONTRACT ENFORCEMENT LAYER (IMPORTANT)
    # =========================

    valid_rows = [to_json_safe(r) for r in valid_rows]
    errors = [to_json_safe(e) for e in errors]

    # =========================
    # SUMMARY
    # =========================

    summary = {
        "total": len(valid_rows) + len(errors),
        "valid": len(valid_rows),
        "invalid": len(errors),
    }

    error_summary = build_error_summary(errors)

    # =========================
    # DEBUG REPORT
    # =========================

    report = build_debug_report(
        summary=summary,
        error_summary=error_summary
    )

    # =========================
    # EXPORTS
    # =========================

    export_json(valid_rows, "valid.json")
    export_json(errors, "errors.json")
    export_text(report, "debug_report.txt")

    return {
        "valid_rows": valid_rows,
        "errors": errors,
        "summary": summary,
        "error_summary": error_summary,
        "debug_report": report,
    }