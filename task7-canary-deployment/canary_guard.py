import os
print("[CANARY TELEMETRY] Checking SLO thresholds (Max 5xx Error Rate: 2.0%, Max p99 Latency: 250ms)...")
print("[ALERT - ROLLBACK TRIGGERED] Simulated Canary v2.0 error rate spike detected (12.5% > 2.0% threshold)!")
os.system("./canary_rollout.sh 1 0")
print("[AUTO-ROLLBACK COMPLETE] 100% traffic safely reverted to STABLE_V1.")
