from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from pathlib import Path

input_path = Path("assets/ocr_pics/newspaper.jpg")

converter = DocumentConverter()

result = converter.convert(input_path)

md_output = result.document.export_to_markdown(image_mode="placeholder")

print(md_output)
