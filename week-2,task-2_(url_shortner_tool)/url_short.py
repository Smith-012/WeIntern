import json
import os
import uuid
import hashlib

DATA_FILE = "urls.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

def generate_slug(url):
    return hashlib.md5((url + str(uuid.uuid4())).encode()).hexdigest()[:6]

def shorten_url(data):
    url = input("Enter URL: ").strip()

    if not is_valid_url(url):
        print("Invalid URL.")
        return

    for slug, stored_url in data.items():
        if stored_url == url:
            print(f"Already shortened: {slug}")
            return

    slug = generate_slug(url)
    data[slug] = url
    save_data(data)
    print(f"Short URL slug: {slug}")

def retrieve_url(data):
    slug = input("Enter slug: ").strip()
    url = data.get(slug)

    if not url:
        print("Slug not found.")
    else:
        print(f"Original URL: {url}")

def main():
    data = load_data()

    while True:
        print("\n1. Shorten URL")
        print("2. Retrieve URL")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            shorten_url(data)
        elif choice == "2":
            retrieve_url(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
