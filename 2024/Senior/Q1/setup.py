import time
import psutil
import os
import random
from Solution import Solution

def setup():
    N = 1000000
    x = random.randint(1, int((N/2))) * 2
    H = []
    for _ in range(x):
        H.append(random.randint(1, 2000000))

    return x, H

input = setup()
solution = Solution()
start_time = time.time()
result = solution.solve(n=input[0], h=input[1])
end_time = time.time()
print(f"Solution: {result}")


process = psutil.Process(os.getpid())
memory_info = process.memory_info()
print(f"Execution time: {end_time - start_time} seconds")
print(f"Memory usage: {memory_info.rss / (1024 * 1024)} MB")



