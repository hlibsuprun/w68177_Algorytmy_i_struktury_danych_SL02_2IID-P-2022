n = int(input())
data = input().split()

count = 0
max_jump = 0

for i in data:
    if int(i):
        count += 1
        if max_jump < count:
            max_jump = count
    else:
        count = 0

print(max_jump)
