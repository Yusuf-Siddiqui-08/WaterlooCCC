x = input().split()
n = int(x[0])
t = int(x[1])
result = []
strings = []
for i in range(n):
    strings.append(input())

for i in range(n):
    heavy = []
    light = []
    string = strings[i]
    for char in string:
        if char in heavy or char in light:
            continue
        count = string.count(char)
        if count > 1:
            heavy.append(char)
        else:
            light.append(char)
    replaced = []
    for char in string:
        if char in heavy:
            replaced.append(2)
        else:
            replaced.append(1)
    result.append("T")
    prev_char = replaced[0]
    for index, char in enumerate(replaced):
        if index == 0:
            continue
        if char == prev_char:
            result[-1] = "F"
            break
        prev_char = char

    print(result[-1])
