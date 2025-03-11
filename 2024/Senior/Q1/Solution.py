result = 0
n = int(input())
h = []
for i in range(n):
    h.append(int(input()))

half_length = int(n/2)
for index, i in enumerate(h):
    #print(index)
    if index >= half_length:
        break
    across = h[index + half_length]
    if i == across:
        result += 1

result = result * 2
print(result)