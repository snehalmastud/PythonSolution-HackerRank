import re
for i in xrange(input()):
    k = raw_input()
    print bool(re.match(r'^[+-]?\d*?\.{1}\d+$',k))
