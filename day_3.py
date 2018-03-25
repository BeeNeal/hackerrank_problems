N = int(raw_input().strip())

if N % 2 != 0 or N in set(range(6, 21, 2)):
    print 'Weird'
elif N in set(range(2, 6, 2)) or N > 20:
    print 'Not Weird'
else:
    print 'invalid number'
