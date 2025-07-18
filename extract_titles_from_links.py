import subprocess
import fitz  # PyMuPDF

LINKS_FILE = "links.txt"
PDF_FILENAME = "general.pdf"
TITLES_FILE = "titles.txt"

def download_pdf(url):
    # Download PDF using curl
    result = subprocess.run(["curl", "--silent", "--output", PDF_FILENAME, url])
    if result.returncode != 0:
        raise RuntimeError(f"Failed to download: {url}")

def extract_course_title(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc[0]
    blocks = page.get_text("dict")["blocks"]

    title_spans = []
    max_font_size = 0

    # Find max font size
    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                size = span["size"]
                if size > max_font_size:
                    max_font_size = size

    # Collect all spans with max font size
    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if span["size"] == max_font_size:
                    title_spans.append(span["text"].strip())

    title = " ".join(title_spans)
    return title

def main():
    with open(LINKS_FILE, "r") as file:
        urls = [line.strip() for line in file if line.strip()]

    with open(TITLES_FILE, "w", encoding="utf-8") as out_file:
        for i, url in enumerate(urls, 1):
            try:
                print(f"[{i}] Downloading from: {url}")
                download_pdf(url)

                title = extract_course_title(PDF_FILENAME)
                print(f"[✓] Extracted title: {title}\n")

                out_file.write(title + "\n")
            except Exception as e:
                print(f"[✗] Error processing URL: {url}\n    Reason: {e}")
                out_file.write("[Error extracting title]\n")

if __name__ == "__main__":
    main()
