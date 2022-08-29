# breadth first search
queue = ["0","1"]
for i in range(15):
    val = queue[0]
    one = val + "0"
    two = val + "1"
    del queue[0]
    queue.append(one)
    queue.append(two)

print(len(queue))


