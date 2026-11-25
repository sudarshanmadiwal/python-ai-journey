count = 0
def increment(value):
    return value+1


for _ in range(3):
    count = increment(count)
    print(count)