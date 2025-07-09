import socket
import ssl
import sys
from OpenSSL import SSL
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timezone
 
def count_certificate_issuers(domain: str, port: int = 443):
    context = SSL.Context(SSL.TLS_CLIENT_METHOD)
    context.set_default_verify_paths()
 
    conn = SSL.Connection(context, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    conn.set_tlsext_host_name(domain.encode())
    conn.connect((domain, port))
    conn.do_handshake()
 
    cert_chain = conn.get_peer_cert_chain()
    total_certs = len(cert_chain)
    expired_count = 0
 
    print(f"\n🔐 Certificate Chain for {domain}:\n")
 
    for idx, cert in enumerate(cert_chain):
        # Convert to cryptography.x509 format
        x509_cert = x509.load_der_x509_certificate(
            cert.to_cryptography().public_bytes(encoding=serialization.Encoding.DER)
        )
 
        # Use timezone-aware datetime fields
        not_valid_before = x509_cert.not_valid_before_utc
        not_valid_after = x509_cert.not_valid_after_utc
        now = datetime.now(timezone.utc)
 
        expired = now > not_valid_after
        if expired:
            expired_count += 1
 
        print(f"📄 Certificate {idx + 1}:")
        print(f"  • Subject: {x509_cert.subject.rfc4514_string()}")
        print(f"  • Issuer:  {x509_cert.issuer.rfc4514_string()}")
        print(f"  • Valid From: {not_valid_before}")
        print(f"  • Valid To:   {not_valid_after}")
        print(f"  • Expired:    {'Yes' if expired else 'No'}\n")
 
    conn.close()
 
    print("✅ Summary:")
    print(f"  • Total Certificates in Chain: {total_certs}")
    print(f"  • Expired Certificates:        {expired_count}")
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Cert_Check.py <domain>")
        sys.exit(1)
 
    domain_name = sys.argv[1]
    count_certificate_issuers(domain_name)
