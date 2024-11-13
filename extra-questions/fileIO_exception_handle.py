import requests

def check_urls(file_path, log_file='status_log.txt'):
    with open(file_path, 'r') as file, open(log_file, 'w') as log:
        for url in file:
            url = url.strip()
            try:
                response = requests.get(url)
                log.write(f"{url}: {response.status_code}\n")
            except requests.RequestException as e:
                log.write(f"Error accessing {url}: {e}\n")

# Example usage
check_urls('urls.txt')
