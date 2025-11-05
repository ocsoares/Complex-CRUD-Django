from rest_framework import status
from rest_framework.exceptions import APIException

class UserAlreadyExistsByEmailException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A user with this email already exists.'
    default_code = 'user_already_exists'
