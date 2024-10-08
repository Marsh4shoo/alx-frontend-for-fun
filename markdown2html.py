#!/usr/bin/python3
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    
    with open(input_file, 'r') as md_file:
        md_content = md_file.read()
    
    with open(output_file, 'w') as html_file:
        html_file.write(md_content)
    
    sys.exit(0)

