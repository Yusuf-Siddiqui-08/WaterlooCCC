
class Solution():
    def __init__(self):
        self.result = []

    def solve(self, t: int, n: int, input: list):
        for i in range(t):
            heavy = []
            light = []
            string = input[i]
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
            self.result.append("T")
            prev_char = replaced[0]
            for index, char in enumerate(replaced):
                if index == 0:
                    continue
                if char == prev_char:
                    self.result[-1] = "F"
                    break
                prev_char = char
        return self.result


