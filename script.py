import requests
import os

# Nahraď těmito URL adresami, co chceš stahovat
urls = ["https://example.com/file1.txt", "https://example.com/file2.txt"]
downloaded_files = []

for i, url in enumerate(urls):
    response = requests.get(url)
    filename = f"file{i+1}.txt"
    with open(filename, "wb") as f:
        f.write(response.content)
    downloaded_files.append(filename)

# Základní analýza (např. porovnání velikosti)
with open("results.csv", "w") as f:
    f.write("Soubor,Velikost\n")
    for file in downloaded_files:
        size = os.path.getsize(file)
        f.write(f"{file},{size}\n")
