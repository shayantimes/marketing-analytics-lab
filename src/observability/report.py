def build_report(valid, invalid):
    return {
        "total": valid + invalid,
        "valid": valid,
        "invalid": invalid,
        "success_rate": valid / (valid + invalid) if (valid + invalid) else 0
    }