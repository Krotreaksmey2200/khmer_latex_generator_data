import subprocess
import os
from pathlib import Path

class LatexEngine:
    def __init__(self):
        self.tex_dir = Path("dataset/tex")
        self.pdf_dir = Path("dataset/pdf")
        self.tex_dir.mkdir(parents=True, exist_ok=True)
        self.pdf_dir.mkdir(parents=True, exist_ok=True)

    def build_tex(self, content, tex_path):
        latex = rf"""\documentclass[border=5pt]{{standalone}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{fontspec}}
\usepackage{{amsmath,amsfonts,amssymb,multicol}}
\usepackage[no-math]{{fontspec}}
\setmainfont [Scale = 1, Script=Khmer,AutoFakeBold=2.5,AutoFakeSlant=0.3]{{Khmer OS Siemreap}}
\everymath{{\displaystyle}}

\begin{{document}}
{content}
\end{{document}}
"""
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(latex)

    def compile_pdf(self, tex_path):
        tex_path = Path(tex_path)
        try:
            # We want the PDF to be in dataset/pdf
            result = subprocess.run(
                [
                    "xelatex",
                    "-interaction=nonstopmode",
                    f"-output-directory={self.pdf_dir}",
                    str(tex_path)
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )

            # Clean up aux and log files in the pdf directory
            base_name = tex_path.stem
            for ext in [".aux", ".log"]:
                aux_file = self.pdf_dir / f"{base_name}{ext}"
                if aux_file.exists():
                    os.remove(aux_file)

            return True, "Success"
        except subprocess.CalledProcessError as e:
            # Use stdout if stderr is empty, as xelatex often writes errors to stdout
            error_msg = e.stderr if e.stderr.strip() else e.stdout
            return False, f"LaTeX Error: {error_msg}"
        except Exception as e:
            return False, str(e)
