from django.db.models import query
from django.db.models.query import QuerySet
from profiles.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from profiles.api.serializers import (ProfileAvatarSerializer,
                                      ProfileSerializer,
                                      ProfileStatusSerializer)
from profiles.models import Profile, ProfileStatus
from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["city"]
    # def get_queryset(self):
    #     queryset = Profile.objects.all()
    #     city = self.request.query_params.get("city", None)
    #     if city is not None:
    #         queryset = queryset.filter(city=city)
    #     return queryset
    
class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            # Lookup query : ProfileStatus -> Profile -> User 
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset
    
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


