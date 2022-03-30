import os

def validate_file_extension(filename):
    valid_extensions = ['.pdf']
    isValid = True
    ext = os.path.splitext(filename)[1]
    if not ext.lower() in valid_extensions:
        isValid = False
    return isValid
