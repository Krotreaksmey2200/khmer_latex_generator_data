import os
from pathlib import Path

class DatasetWriter:
    def append_row(self, tsv_path, image_path, text):
        # Ensure directory exists
        Path(tsv_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Clean text: remove newlines and extra spaces
        text = text.replace("\n", " ").strip()
        
        # Write to TSV
        # If file doesn't exist, we could add a header, but user didn't ask for one
        with open(tsv_path, "a", encoding="utf-8") as f:
            f.write(f"{image_path}\t{text}\n")
