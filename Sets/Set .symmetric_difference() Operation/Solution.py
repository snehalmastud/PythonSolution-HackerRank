a = int(raw_input())
b = raw_input().split()
b = list(map(int, b))
c = int(raw_input())
d = raw_input().split()
d = list(map(int, d))

print len(set(b).symmetric_difference(set(d)))
