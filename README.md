# 🔐 Certificate Chain Checker

This Python script, `Cert_Check.py`, checks the SSL/TLS certificate chain of a given domain and provides a summary including:

- The subject and issuer of each certificate in the chain  
- Validity period (start and expiry dates)  
- Whether each certificate is expired  
- Total number of certificates and how many are expired  

---

## 📦 Prerequisites

Ensure the following Python packages are installed:

```bash
pip install pyOpenSSL cryptography

# Usage
python Cert_Check.py <domain>

#Example:
python Cert_Check.py example.com

#Sample Output
🔐 Certificate Chain for example.com:

📄 Certificate 1:
  • Subject: CN=example.com
  • Issuer:  CN=R3,O=Let's Encrypt,C=US
  • Valid From: 2024-06-01 00:00:00+00:00
  • Valid To:   2024-08-30 23:59:59+00:00
  • Expired:    No

📄 Certificate 2:
  • Subject: CN=R3,O=Let's Encrypt,C=US
  • Issuer:  CN=ISRG Root X1,O=Internet Security Research Group,C=US
  • Valid From: 2020-09-04 00:00:00+00:00
  • Valid To:   2025-09-15 16:00:00+00:00
  • Expired:    No

✅ Summary:
  • Total Certificates in Chain: 2
  • Expired Certificates:        0

