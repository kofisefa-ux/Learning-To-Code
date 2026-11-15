file = input("File name: ").strip().lower()

if file.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
    print("Your file is an Image")
elif file.endswith((".pdf", ".txt", ".doc", ".docx")):
    print("Your file is a document")
elif file.endswith((".csv", ".xls", ".xlsx")):
    print("Your file is a spreadsheet")
elif file.endswith((".html", ".css", ".js")):
    print("Your file is a web page")
else:
    print("application/octet-stream")