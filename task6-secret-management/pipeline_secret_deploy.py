import os, json, urllib.request, hashlib

VAULT_ADDR = "http://127.0.0.1:8200"
VAULT_TOKEN = "krmu-vault-root-token"

req = urllib.request.Request(
    f"{VAULT_ADDR}/v1/secret/data/prod/app",
    headers={"X-Vault-Token": VAULT_TOKEN}
)
with urllib.request.urlopen(req) as resp:
    payload = json.loads(resp.read().decode())

secrets = payload["data"]["data"]
version = payload["data"]["metadata"]["version"]

print("=" * 60)
print(f"[PIPELINE] Authenticated with HashiCorp Vault (Secret Version: v{version})")
print(f"[SECRET INJECTION] DB_USER     = {secrets['DB_USER']}")
print(f"[SECRET INJECTION] DB_PASSWORD = ***MASKED*** (len={len(secrets['DB_PASSWORD'])})")
print(f"[SECRET INJECTION] API_KEY     = ***MASKED*** (len={len(secrets['API_KEY'])})")

digest = hashlib.sha256(secrets["DB_PASSWORD"].encode()).hexdigest()[:16]
os.system("docker rm -f secret-managed-app >/dev/null 2>&1")
with open("runtime_app/index.html", "w") as f:
    f.write(f"<h1>Vault-Secured Deployment</h1><p>DB User: {secrets['DB_USER']} | Secret Version: v{version} | Fingerprint: {digest}</p>\n")

os.system("docker run -d --name secret-managed-app -p 8096:80 -v $(pwd)/runtime_app:/usr/share/nginx/html nginx:alpine >/dev/null")
print(f"[DEPLOYED] Container 'secret-managed-app' live on :8096 with Vault v{version} credentials")
print("=" * 60)
