import os, subprocess, re

with open("manifests/deployment.yaml") as f:
    manifest = f.read()

desired_version = re.search(r'version:\s*"([^"]+)"', manifest).group(1)
port = re.search(r'port:\s*(\d+)', manifest).group(1)
app_name = "gitops-web-app"

print(f"[GITOPS] Single Source of Truth -> {app_name} | Desired Version: {desired_version}")

ps = subprocess.getoutput(f"docker ps --filter name=^{app_name}$ --format '{{{{.Names}}}}'")
current_html = open("runtime_html/index.html").read() if os.path.exists("runtime_html/index.html") else ""

if ps != app_name or desired_version not in current_html:
    print(f"[DRIFT DETECTED] Live state diverges from Git ({desired_version}). Reconciling...")
    os.system(f"docker rm -f {app_name} >/dev/null 2>&1")
    with open("runtime_html/index.html", "w") as out:
        out.write(f"<h1>GitOps Managed Service ({app_name})</h1><p>Synced Release: {desired_version}</p>\n")
    os.system(f"docker run -d --name {app_name} -p {port}:80 -v $(pwd)/runtime_html:/usr/share/nginx/html nginx:alpine >/dev/null")
    print(f"[RECONCILED] Container {app_name} converged to {desired_version} on port {port} (Status: SYNCED)")
else:
    print(f"[IN-SYNC] Live state matches Git Single Source of Truth ({desired_version})")
