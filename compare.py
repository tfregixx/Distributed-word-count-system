import time
from collections import Counter
import re

def single_threaded(text):
    start = time.time()
    words = re.findall(r'\w+', text.lower())
    counts = Counter(words)
    return counts, time.time() - start

if __name__ == '__main__':
    text = "distributed systems are fun and distributed systems are powerful " * 100000
    
    # Single Threaded
    _, time_s = single_threaded(text)
    print(f"Single-threaded time: {time_s:.4f}s")
    
    
    from master import run_distributed
    _, time_d = run_distributed(text)
    print(f"Distributed time: {time_d:.4f}s")
