
class Solution():
    def __init__(self):
        self.result = 0

    def solve(self, n: int, h: list) -> int:
        half_length = int(n/2)
        for index, i in enumerate(h):
            if index == (n / 2):
                break
            across = h[index + half_length]
            if i == across:
                self.result += 1
        self.result = self.result * 2
        return self.result


