from rest_framework.pagination import PageNumberPagination
from rest_framework import response

class CustomPagination(PageNumberPagination):
    page_size = 20