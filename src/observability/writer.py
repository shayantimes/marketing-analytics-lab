import json
from pathlib import Path


class PipelineWriter:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        self.valid_file = self.output_dir / "valid.json"
        self.error_file = self.output_dir / "errors.json"
        self.report_file = self.output_dir / "report.json"

    def write_valid(self, rows: list):
        self.valid_file.write_text(
            json.dumps(rows, default=str, indent=2)
        )

    def write_errors(self, errors: list):
        serialized = [
            {
                "row_index": e.row_index,
                "errors": e.errors,
                "raw_row": e.raw_row,
            }
            for e in errors
        ]

        self.error_file.write_text(
            json.dumps(serialized, default=str, indent=2)
        )

    def write_report(self, total, valid, invalid):
        report = {
            "total": total,
            "valid": valid,
            "invalid": invalid,
        }

        self.report_file.write_text(
            json.dumps(report, indent=2)
        )