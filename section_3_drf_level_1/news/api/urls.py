from django.urls    import path
from news.api.views import (
    ArticleCreateListAPIView,
    ArticleDetailAPIView,
    JournalistListCreateAPIView,
    JobOfferCreateListAPIView,
    JobOfferDetailAPIView
)

# from news.api.views import (
#     article_list_create_api_view,
#     article_detail_api_view
# )

urlpatterns = [
    path('articles/', 
         ArticleCreateListAPIView.as_view(), 
         name='article-list'),
    
    path('articles/<int:pk>/', 
         ArticleDetailAPIView.as_view(), 
         name='article-detail'),
    
    path('journalists/', 
         JournalistListCreateAPIView.as_view(), 
         name='journalists-list'),
    
    path('joboffers/', 
         JobOfferCreateListAPIView.as_view(), 
         name='joboffer-list'),
    
    path('joboffers/<int:pk>/', 
         JobOfferDetailAPIView.as_view(), 
         name='joboffer-detail'),
    # path('articles/', article_list_create_api_view, name='article-list'),
    # path('articles/<int:pk>/', article_detail_api_view, name='article-detail'),
]



# urlpatterns = [

# ]