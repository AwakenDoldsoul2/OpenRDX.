import argparse
import sys
from packages.units.checkurl import check_url, read_payloads
from packages.includes.banner import display_banner

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='Target base URL')
    parser.add_argument('-U', '--url_file', help='Path to the file containing target URLs')
    parser.add_argument('-p', '--payload_file', required=True, help='Path to the payload file')
    parser.add_argument('-o', '--output_file', required=True, help='Path to save the output of vulnerable sites')
    return parser.parse_args()

def read_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading URL file '{file_path}': {e}")
        sys.exit(1)

def main():
    display_banner()
    args = parse_arguments()

    urls = []
    if args.url:
        urls.append(args.url.strip())
    if args.url_file:
        urls.extend(read_urls(args.url_file))

    if not urls:
        print("No URLs provided. Please provide a target URL or a file containing URLs.")
        return

    payloads = read_payloads(args.payload_file)
    if not payloads:
        print("No payloads found. Please provide a valid payload file.")
        return

    vulnerable_sites = []

    for base_url in urls:
        if not base_url:
            continue
        print(f"Testing URL: {base_url}")
        try:
            for payload in payloads:
                print(f"Testing payload: {payload}")
                try:
                    if check_url(base_url, payload):
                        vulnerable_sites.append(base_url)
                        print(f"Vulnerable: {base_url} with payload {payload}")
                except Exception as e:
                    print(f"Error testing payload '{payload}' on '{base_url}': {e}")
        except KeyboardInterrupt:
            print("\nProgram stopped.")
            sys.exit(0)

    if vulnerable_sites:
        with open(args.output_file, 'w') as file:
            for site in vulnerable_sites:
                file.write(f"{site}\n")
        print(f"Vulnerable sites saved to {args.output_file}")
    else:
        print("No vulnerable sites found.")

if __name__ == "__main__":
    main()
