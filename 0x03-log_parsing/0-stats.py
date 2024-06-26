#!/usr/bin/python3
"""
Structuring the Data
"""
import sys
import re
import signal


cnts = 0
status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_cnt = 0

log_pattern = re.compile(
    r'^(?P<ip>\d{1,3}(\.\d{1,3}){3}) - '
    r'\[(?P<date>.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" '
    r'(?P<status>\d{3}) '
    r'(?P<size>\d+)$'
)


def print_statistics():
    """
    Prints the computed statistics
    """
    print(f'File size: {cnts}')
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def handle_interrupt(signal, frame):
    """
    Handle Keyboard interrupt
    """
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    lst = []

    for i in line.rsplit():
        lst.append(i)

    # Updating the list every time
    size = int(lst[-1]) if int else None
    status = lst[-2]

    # Updating the metrics
    cnts += size
    status_counts[status] += 1

    line_cnt += 1
    if line_cnt % 10 == 0:
        print_statistics()


print_statistics()
