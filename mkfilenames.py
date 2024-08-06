#!/usr/bin/env python3

import sys
import re
import argparse
from datetime import datetime

# Parse command line arguments
parser = argparse.ArgumentParser(description='Filter the URLs with dates.')
parser.add_argument('--start_date', type=str, help='Date in YYYYMMDD format to filter the data.')
parser.add_argument('--end_date', type=str, help='Date in YYYYMMDD format to filter the data.')
args = parser.parse_args()

# Convert the date strings to datetime objects
if args.start_date:
    try:
        start_date = datetime.strptime(args.start_date, '%Y%m%d')
    except ValueError:
        print("Error: Invalid start_date format. Use YYYYMMDD format.", file=sys.stderr)
        sys.exit(1)
else:
    start_date = datetime.strptime('19700101', '%Y%m%d')

if args.end_date:
    try:
        end_date = datetime.strptime(args.end_date, '%Y%m%d')
    except ValueError:
        print("Error: Invalid end_date format. Use YYYYMMDD format.", file=sys.stderr)
        sys.exit(1)
else:
    end_date = datetime.strptime('99991231', '%Y%m%d')

# Check if start_date < end_date
if args.start_date and args.end_date:
    if args.start_date > args.end_date:
        print("Error: start_date should be less than end_date.", file=sys.stderr)
        sys.exit(1)

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
            if end_date < datetime.strptime(match_filename.group(1)[:8], '%Y%m%d'):
                sys.exit(0)

            # Print the extracted filename prefixed with "data/"
            if start_date <= datetime.strptime(match_filename.group(1)[:8], '%Y%m%d'):
                print(f"data/{match_filename.group(2)}/{match.group(1)}")

