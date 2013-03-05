import sys

for line in sys.stdin:
    if line == 'EOF':
	break
    print line,

