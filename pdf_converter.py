from pdf2image import convert_from_path
from pathlib import Path

class PDFConverter:
    def __init__(self):
        self.image_dir = Path("dataset/images")
        self.image_dir.mkdir(parents=True, exist_ok=True)

    def pdf_to_image(self, pdf_path, output_path):
        try:
            images = convert_from_path(
                pdf_path,
                dpi=300
            )
            if images:
                # Ensure parent directory exists
                Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                images[0].save(output_path, "JPEG")
                return True, "Success"
            return False, "No image generated from PDF"
        except Exception as e:
            return False, str(e)
