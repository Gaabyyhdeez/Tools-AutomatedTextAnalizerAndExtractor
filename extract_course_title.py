import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_txt="output.txt"):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        full_text += page.get_text()

    # Write full text to output.txt
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"[✓] Full text extracted to {output_txt}")

def extract_course_title(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc[0]  # First page

    blocks = page.get_text("dict")["blocks"]
    title_spans = []
    max_font_size = 0

    # First pass: find max font size
    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                size = span["size"]
                if size > max_font_size:
                    max_font_size = size

    # Second pass: collect all spans with max font size
    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if span["size"] == max_font_size:
                    title_spans.append(span["text"].strip())

    # Join the spans into a full title
    title = " ".join(title_spans)
    return title


if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) != 2:
        print("Usage: python extract_course_title.py path_to_pdf")
        sys.exit(1)

    pdf_file = sys.argv[1]

    if not os.path.isfile(pdf_file):
        print(f"Error: File not found -> {pdf_file}")
        sys.exit(1)

    # Extract and save full text
    extract_text_from_pdf(pdf_file)

    # Extract course title
    title = extract_course_title(pdf_file)
    print(f"\n📘 Course Title: {title}")
