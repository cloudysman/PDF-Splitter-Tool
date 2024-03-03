# PDF Page Extractor

## Overview
This Python script, leveraging the PyPDF2 library, provides a convenient way to extract specific pages from a PDF file, saving them into a new document. Designed for simplicity and efficiency, it's perfect for anyone needing to work with parts of PDF documents.

## Features
- **Selective Page Extraction:** Specify the exact range of pages you need from any PDF.
- **New Document Creation:** Automatically saves the extracted pages as a new PDF file.

## Requirements
- **PyPDF2 Library:** Ensure you have PyPDF2 installed to handle PDF operations.

## Installation
First, make sure Python is installed on your system. Then, install PyPDF2 with pip:
```bash
pip install PyPDF2
```
## Usage
Run the script from your terminal or command prompt:
```bash
python Cut_File_PDF.py
```
## Example
To extract pages 48 to 83 from LSD.pdf into LSD_cut.pdf:
```bash
extract_pages_from_pdf("LSD.pdf", "LSD_cut.pdf", 48, 83)
```
## Contribution
Contributions are welcome! Feel free to fork, add features, or improve the script. Let's make PDF handling easier for everyone.
