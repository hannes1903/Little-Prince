
import sys
for line in sys.stdin:
    for word in line.strip().split():
        sys.stdout.write("{0}\t1\n".format(word.lower()))

