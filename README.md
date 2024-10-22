# Webpage Content Extractor

**Webpage Content Extractor** is a Python tool that downloads a webpage, extracts its HTML, JavaScript, and CSS content, and saves them into separate files. The tool also provides size information for each content type and organizes the files into a subfolder based on the webpage's domain name.

## Features:
- Downloads a webpage and saves the raw HTML.
- Extracts and saves the following components:
  - HTML (without `<style>` and `<script>` tags)
  - JavaScript (from `<script>` tags)
  - CSS (from `<style>` tags)
- Organizes the extracted content into a subfolder named after the webpage's domain.
- Outputs a summary of file sizes, including the total size.

## Usage:
1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the script and provide a webpage URL when prompted.

Example:

```bash
python webpage_content_splitter.py
```

4. The HTML, JavaScript, and CSS files will be saved in a subfolder based on the webpage’s domain name.

## Requirements:
- `requests`
- `beautifulsoup4`

## Example:

```bash
python webpage_content_splitter.py
```

Enter the URL of the web page: `https://example.com`

```
============================================================
Content Type       | File Name           | Size (KB) 
------------------------------------------------------------
HTML              | html_only.html       | 12.34 KB
JavaScript        | scripts_only.js      | 5.67 KB
CSS               | styles_only.css      | 2.89 KB
------------------------------------------------------------
Total Size        | N/A                  | 20.90 KB
============================================================
All files have been saved in the folder: example_com
```
