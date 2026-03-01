import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def read_docx(file_path):
    try:
        if not os.path.exists(file_path):
            return "File not found."
            
        with zipfile.ZipFile(file_path) as z:
            xml_content = z.read('word/document.xml')
            
            # Parse XML
            root = ET.fromstring(xml_content)
            
            # Namespace for Word document XML
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text = []
            # Iterate through paragraphs
            for p in root.findall('.//w:p', ns):
                paragraph_text = []
                # Iterate through runs
                for r in p.findall('.//w:r', ns):
                    # Iterate through text nodes
                    for t in r.findall('.//w:t', ns):
                        if t.text:
                            paragraph_text.append(t.text)
                
                # Join runs in a paragraph and append to text list
                if paragraph_text:
                    text.append(''.join(paragraph_text))
            
            return '\n'.join(text)
    except Exception as e:
        return f"Error reading docx: {str(e)}"

if __name__ == "__main__":
    # Handle filename with spaces and special chars by joining args or using a fixed temp file
    # For this specific case, we'll try to find the file matching the pattern if direct path fails
    import glob
    
    target_file = "e:\\Skills库\\提示词Skills\\🎬 即梦 Seedance 2.0 使用手册（全新多模态创作体验） (1).docx"
    
    # Try direct access first
    content = read_docx(target_file)
    
    if content == "File not found.":
        # Fallback: try to find the file in the directory
        files = glob.glob("e:\\Skills库\\提示词Skills\\*Seedance*.docx")
        if files:
            content = read_docx(files[0])
            print(f"Read from: {files[0]}")
        else:
            print("Could not find the file.")
            sys.exit(1)
            
    print(content)
