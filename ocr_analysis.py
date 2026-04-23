import easyocr

reader = easyocr.Reader(['en'])
results = reader.readtext('todo.jpg')

for (bbox, text, confidence) in results:
    print(f"Text: {text} (Confidence: {confidence:.2f})")
