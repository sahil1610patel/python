import csv
import json
import os

def parse_file(file_path):
    # Clean up any accidental quotes or whitespace from the path input
    file_path = file_path.strip('"\'')
    
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    print(f"\n--- Parsing: {os.path.basename(file_path)} ---")
    
    try:
        if ext == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return {
                "file_type": "text",
                "character_count": len(content),
                "line_count": content.count('\n') + 1,
                "content": content
            }
            
        elif ext == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return {
                "file_type": "json",
                "data": data
            }
            
        elif ext == '.csv':
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            return {
                "file_type": "csv",
                "row_count": len(rows),
                "columns": reader.fieldnames,
                "data": rows
            }
        else:
            return {"error": f"Unsupported file extension: {ext}"}
            
    except Exception as e:
        return {"error": f"An error occurred while reading the file: {str(e)}"}

def main():
    print("=== Universal File Parser Utility ===")
    while True:
        path_input = input("\nEnter the path of the file to parse (txt, json, csv) or 'q' to quit: ")
        if path_input.lower() == 'q':
            print("Exiting. Goodbye!")
            break
            
        result = parse_file(path_input)
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()