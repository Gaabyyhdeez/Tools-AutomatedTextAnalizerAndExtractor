# Tools-AutomatedTextAnalizerAndExtractor
A Python-based automation tool to download, extract, and organize training course PDFs from a list of URLs. Features include bulk downloading, title extraction using PyMuPDF, and structured storage of course metadata.

Locate your files:

1. extract_cours_title.py
2. extract_titles_from_links.py
3. general.pdf
4. links.txt
5. output.txt
6. titles.txt

1. extract_cours_title.py: here is where, given an specific PDF with the GCP Official Courses Format, the title of the course is extracted.
2. extract_titles_from_links.py: this is where the automation happens. We used the file "links", where we upload the full list of links for all public and downloadlable PDFs, and we iterate it. One by one we analyse those links and extract the name of the course (the title).
3. general.pdf: this is the pdf which is going to be used to extract the title by overwriting the content of the file. Instead of having dozens or hundreds of different pdfs we have only one which is going to be used to be analyzed.
4. links.txt: the list of the links for the pdfs that we want to analyze.
5. output.txt: this is a txt file which is goint to help the "extract_cours_title" process.
6. titles.txt: the final result. The list of all the titles.


You must:
a. Update the links.txt file with your own links.
b. Clean the titles.txt file. Leave it in blank.
c. Execute in your terminal: "python extract_titles_from_links.py"
d. Wait for the results to be writen and completed.