import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def save_to_file(folder, filename, content):
    """Helper function to save content to a file inside a folder and return the file size."""
    file_path = os.path.join(folder, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return os.path.getsize(file_path)

def create_folder_from_url(url):
    """Create a subfolder based on the domain name from the URL."""
    parsed_url = urlparse(url)
    folder_name = parsed_url.netloc.replace('.', '_')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def download_and_split_content(url):
    # Create folder based on the URL domain
    folder = create_folder_from_url(url)
    
    # Download the web page
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return
    
    # Save the raw HTML to the folder
    raw_html_file = os.path.join(folder, "raw_page.html")
    with open(raw_html_file, 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract <style> tags content
    style_tags = soup.find_all('style')
    styles_content = '\n'.join(style_tag.get_text() for style_tag in style_tags)
    
    # Remove <style> tags from the original HTML
    for style_tag in style_tags:
        style_tag.extract()
    
    # Extract <script> tags content
    script_tags = soup.find_all('script')
    scripts_content = '\n'.join(script_tag.get_text() for script_tag in script_tags)
    
    # Remove <script> tags from the original HTML
    for script_tag in script_tags:
        script_tag.extract()
    
    # The remaining HTML (without <style> and <script>)
    html_only_content = soup.prettify()

    # Save the content into separate files and get their sizes
    html_file_size = save_to_file(folder, "html_only.html", html_only_content)
    script_file_size = save_to_file(folder, "scripts_only.js", scripts_content)
    style_file_size = save_to_file(folder, "styles_only.css", styles_content)

    # Calculate total size
    total_size = html_file_size + script_file_size + style_file_size

    # Convert sizes to KB for display
    html_file_size_kb = html_file_size / 1024
    script_file_size_kb = script_file_size / 1024
    style_file_size_kb = style_file_size / 1024
    total_size_kb = total_size / 1024

    # Print a table-like output
    print(f"\n{'='*60}")
    print(f"{'Content Type':<18} | {'File Name':<20} | {'Size (KB)':<10}")
    print(f"{'-'*60}")
    print(f"HTML              | html_only.html       | {html_file_size_kb:.2f} KB")
    print(f"JavaScript        | scripts_only.js      | {script_file_size_kb:.2f} KB")
    print(f"CSS               | styles_only.css      | {style_file_size_kb:.2f} KB")
    print(f"{'-'*60}")
    print(f"Total Size        | N/A                  | {total_size_kb:.2f} KB")
    print(f"{'='*60}")

    print(f"All files have been saved in the folder: {folder}")

# Example usage
if __name__ == "__main__":
    url = input("Enter the URL of the web page: ")
    download_and_split_content(url)
