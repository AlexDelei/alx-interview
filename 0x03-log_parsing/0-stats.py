#!/usr/bin/python3
"""
Log Parsing
"""
import sys
import re
import random
import signal
from typing import Any
from time import sleep


s = []
fmt = r'^(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$'
for idx, line in enumerate(sys.stdin):
    try:
        lst = []
        inp_format = re.match(fmt, line)
        if not inp_format:
            break
        for i in line.rsplit():
            lst.append(i)

        s.append(int(lst[8]))
        if idx % 10 == 0:
            print(f'File size: {sum(s)}')

        print(f'{lst[7]}: {random.randint(1, 10)}')
    except KeyboardInterrupt:
        continue

print("Done")
