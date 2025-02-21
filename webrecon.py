import requests


# function for fetching the headers
def get_header(url):
    try:
        response = requests.get(url,timeout=5,allow_redirects=True)
        headers = response.headers
        print("\n[+] HTTP Headers :")
        for key, value in headers.items():
            print(f"{key} : {value}")
            return headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")


# function for checking security headers
def get_security_headers(headers):
    print("\n[+] Security headers check :")
    security_headers = [ "Strict-Transport-Security", "Content-Security-Policy",
        "X-Frame-Options", "X-XSS-Protection", "X-Content-Type-Options",
        "Referrer-Policy", "Permissions-Policy"]
    
    for header in security_headers:
        if header in headers:
            print(f"[✅] {header}:{headers[header]}")
        else:
            print(f"[❌] {header} is missing!")


# function for identifying server
def identify_server(headers):
    server = headers.get("Server","Unknown")
    powered_by = headers.get("X-Powered-By", "Unknown")
    
    print("\n[+] Server Information:")
    print(f"Server: {server}")
    print(f"X-Powered-By: {powered_by}")


url = input("Enter your target website url(https://webisteurl.com): ")
headers = get_header(url)
get_security_headers(headers)
identify_server(headers)
