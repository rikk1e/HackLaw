from PIL import Image
import warnings
warnings.simplefilter("ignore", Image.DecompressionBombWarning)

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions

from pathlib import Path

# locate the file we want to perform OCR on
input_path = Path("assets/ocr_docs/APP1988.pdf")

# create some options
pipeline_options = PdfPipelineOptions()

# make it so that OCR actually works on this
pipeline_options.do_table_structure = True
pipeline_options.do_ocr = True

pipeline_options.generate_page_images = False
pipeline_options.generate_picture_images = False

# create a converter, taking the options we made earlier
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_options=pipeline_options
        )
    }
)

result = converter.convert(input_path)

# This can take a second because loading the weights/engine used for OCR can be a bit of a time consuming task
# This doesn't make it any less useable though; we just need to load the engine once, and can use it for multiple documents in the same program

# doing the actual conversion
md_output = result.document.export_to_markdown(image_mode="placeholder")
print(md_output)


# writing all our outputs to a new file
output_path = Path("assets/regex_text/output.md")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_output)


# for files that don't actually contain any encoded text, OCR is significantly more useful
# take ocr_docs/selectionreport.jpg for example
# it's an image that contains text, so we will actually need to use OCR to extract the text


# this will take a while (especially if your machine does not have a dGPU)
pipeline_options.do_ocr = True 
input_path2 = Path("assets/ocr_docs/selectionreport.jpg")
md_output2 = converter.convert(input_path2).document
print(md_output2.export_to_markdown())
