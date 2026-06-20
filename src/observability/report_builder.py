from collections import Counter


def build_report(errors):
    report = {
        "total_errors": len(errors),
        "by_type": Counter(),
        "by_field": Counter(),
        "by_stage": Counter(),
    }

    for e in errors:
        report["by_type"][e.error_type] += 1
        report["by_field"][e.field] += 1
        report["by_stage"][e.stage] += 1

    return report