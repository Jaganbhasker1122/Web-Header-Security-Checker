# 🔍 Web Header & Security Checker  

A simple **Python tool** to fetch HTTP headers, check for **missing security headers**, and **identify server technology** of a target website.  

## 🚀 Features  
✅ Fetch HTTP response headers  
✅ Check for **missing security headers**  
✅ Identify **server technology**  
✅ Supports **redirects**  
✅ Uses a **real browser User-Agent** for better results  

---

## 📌 Installation  

1. **Install Python** (if not installed) → [Download Python](https://www.python.org/downloads/)  
2. **Install dependencies**  
   ```bash
   pip install requests
git clone (https://github.com/Jaganbhasker1122/Web-Header-Security-Checker/)
cd web-header-checker

## Usage
python webrecon.py
Enter your target website URL (https://example.com): 

## Sample Output
[+] HTTP Headers:
Server: Apache
Content-Type: text/html; charset=UTF-8
X-Powered-By: PHP/7.4.3

[+] Security Headers Check:
[❌] Strict-Transport-Security is missing!
[✅] Content-Security-Policy: default-src 'self'
[❌] X-Frame-Options is missing!
[✅] X-XSS-Protection: 1; mode=block

[+] Server Information:
Server: Apache
X-Powered-By: PHP/7.4.3

## To-Do / Improvements
 Save results to a file (e.g., JSON or TXT)
 Add multi-site scanning
 Integrate with Shodan API for deeper analysi

 ## Contributing
 Pull requests are welcome! If you have suggestions, create an issue or fork the repo.
