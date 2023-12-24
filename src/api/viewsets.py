from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.mixins import (CreateModelMixin,
                                    ListModelMixin,
                                    RetrieveModelMixin,
                                    DestroyModelMixin, 
                                    UpdateModelMixin)

class BaseModelViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin, 
    UpdateModelMixin,
    GenericViewSet,
):
    pass


class BaseViewSet(
    ViewSet,
):
    pass