import time
import psutil
import os
start_time = time.time()
import random
from Solution import Solution

def setup():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    T = random.randint(1, 10000)
    N = random.randint(1, 100)
    _input = []
    for _ in range(T):
        _input.append("".join(random.choices(alphabet, k=N)))

    return T, N, _input

q_input = setup()
solution = Solution()
result = solution.solve(t=q_input[0], n=q_input[1], input=q_input[2])
print(f"Solution: {result}")

end_time = time.time()
process = psutil.Process(os.getpid())
memory_info = process.memory_info()
print(f"Execution time: {end_time - start_time} seconds")
print(f"Memory usage: {memory_info.rss / (1024 * 1024)} MB")



