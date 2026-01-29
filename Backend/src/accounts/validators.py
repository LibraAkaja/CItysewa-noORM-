from rest_framework.serializers import ValidationError

MAX_FILE_UPLOAD_SIZE = 10 * 1024 * 1024   # 10 MB


def validate_file_size(file):
    if file.size > MAX_FILE_UPLOAD_SIZE:
        size_limit = MAX_FILE_UPLOAD_SIZE / 1024 
        size_limit = size_limit / 1024
        err_msg = f"Max file upload size is {int(size_limit)} MB"
        raise ValidationError(err_msg)

def validate_phone_number(phone_number):
    pass