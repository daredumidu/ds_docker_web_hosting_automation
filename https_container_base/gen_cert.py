import subprocess
import os

# Output files
KEY_FILE = "server.key"
CSR_FILE = "server.csr"
CRT_FILE = "server.crt"

# Certificate details
#SUBJECT = "/C=IE/ST=Dublin/L=Dublin/O=MyOrg/OU=IT/CN=example.com"
SUBJECT = "/C=LK/ST=Western/L=Colombo/O=SriLanka Inc./OU=IT/CN=SriLankan"

def run(cmd):
    print("> " + cmd)
    subprocess.run(cmd, shell=True, check=True)

# 1. Generate private key
run(f"openssl genrsa -out {KEY_FILE} 2048")

# 2. Generate CSR (Certificate Signing Request)
run(f"openssl req -new -key {KEY_FILE} -out {CSR_FILE} -subj \"{SUBJECT}\"")

# 3. Generate self‑signed certificate (valid 365 days)
run(f"openssl x509 -req -days 3650 -in {CSR_FILE} -signkey {KEY_FILE} -out {CRT_FILE}")

print("\n✅ Self‑signed certificate generated:")
print(f" - Private key: {KEY_FILE}")
print(f" - CSR:         {CSR_FILE}")
print(f" - Certificate: {CRT_FILE}")
