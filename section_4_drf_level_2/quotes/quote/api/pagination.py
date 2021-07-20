from rest_framework.pagination import PageNumberPagination


class DefaultSetPagination(PageNumberPagination):
    page_size = 30
