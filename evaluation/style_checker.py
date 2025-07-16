
def check_style_issues(code):
    results = {
        "long_lines": 0,
        "tabs_instead_of_spaces": 0,
        "missing_header_comments": 0,
        "bad_naming_conventions": 0
    }

    lines = code.splitlines()

    # Line length > 80 (Linux kernel coding standard)
    results["long_lines"] = sum(1 for line in lines if len(line) > 80)

    # Check for tab usage
    results["tabs_instead_of_spaces"] = sum(1 for line in lines if '\t' in line)

    # Check for file header comments (basic heuristic: first 5 lines should have a comment)
    if not any(line.strip().startswith('//') or line.strip().startswith('/*') for line in lines[:5]):
        results["missing_header_comments"] = 1

    # Check variable naming conventions (e.g., camelCase instead of snake_case)
    import re
    bad_names = re.findall(r'\b[a-z]+[A-Z][a-zA-Z]*\b', code)
    results["bad_naming_conventions"] = len(bad_names)

    return results
