import re

def extract_title(md: str):
    lines = md.splitlines()
    find_header = lambda line: re.match(r"^# ", line) != None
    headers = list(filter(find_header, lines))
    if not headers:
        raise Exception('No headers found')
    trim = lambda line: line.removeprefix("# ").strip()
    return trim(headers[0])
