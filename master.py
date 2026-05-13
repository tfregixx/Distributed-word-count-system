import requests
from collections import Counter
import time

WORKERS = ["http://127.0.0.1:5001/map", "http://127.0.0.1:5002/map"]

def split_text(text, n):
    words = text.split()
    k, m = divmod(len(words), n)
    return [" ".join(words[i*k + min(i, m):(i+1)*k + min(i+1, m)]) for i in range(n)]

def run_distributed(text):
    chunks = split_text(text, len(WORKERS))
    results = []
    
    start = time.time()
    for i, worker in enumerate(WORKERS):
        response = requests.post(worker, json={'text': chunks[i]})
        results.append(Counter(response.json()))
    
    # Aggregate
    final_count = sum(results, Counter())
    return final_count, time.time() - start

# Example usage:
if __name__ == '__main__':
    sample_text = "distributed systems are fun and distributed systems are powerful " * 1000
    counts, duration = run_distributed(sample_text)
    print(f"Distributed processing took: {duration:.4f}s")