#!/usr/bin/env python3

import sys
import re
from datetime import datetime

# Set UTF-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

# Regex pattern to match the URL and extract the filename
pattern = re.compile(r'^\s*\S+\s+\S+\s*\S+gdeltv2/(\S+)\.zip$')
pattern_filename = re.compile(r'(\d{14})\.(\S+)\.\S+$')

# Read from standard input
for line in sys.stdin:
    line = line.strip()

    # Match the pattern
    match = pattern.match(line)
    if match:
        match_filename = pattern_filename.match(match.group(1))

        if match_filename:
            # Print the extracted filename prefixed with "data/"
            print(f"data/{match_filename.group(2)}.is_completed/{match.group(1)}.is_completed")

