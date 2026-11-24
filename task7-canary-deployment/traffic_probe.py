import urllib.request, time
from collections import Counter

counts = Counter()
latencies = []
for _ in range(20):
    t0 = time.time()
    body = urllib.request.urlopen("http://localhost:8098").read().decode().strip()
    latencies.append((time.time() - t0) * 1000)
    counts[body] += 1

avg_ms = round(sum(latencies) / len(latencies), 2)
print(f"[TRAFFIC PROBE - 20 Requests] STABLE_V1: {counts['STABLE_V1']} ({counts['STABLE_V1']*5}%) | CANARY_V2: {counts['CANARY_V2']} ({counts['CANARY_V2']*5}%) | Avg Latency: {avg_ms}ms | Errors: 0%")
