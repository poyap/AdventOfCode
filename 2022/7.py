from collections import defaultdict


directories = []
dir_sizes = defaultdict(int)

with open('7.txt' , 'r') as f:
    # list directories file
    for l in f.readlines():
        l = l.strip().split()
        if l[0]=='$':
            if len(l) == 3:
                if l[2] == '..':
                    directories.pop()
                else:
                    directories.append(l[2])
        elif l[0] == 'ls':
            continue
        elif l[0] == 'dir':
            continue
        else:
            sz = int(l[0])
            for i in range(1, len(directories)+1):
                dir_sizes['/'.join(directories[:i])] += sz

p1 = 0
most_size = 100_000


p2 = 1e9
delete_size = 70000000 - 30000000
total_used = dir_sizes['/']
need_to_free = total_used - delete_size

for i in dir_sizes.values():
    if i < most_size:
        p1 += i
    if i >= need_to_free:
        p2 = min(p2, i)


print(p1, p2)
