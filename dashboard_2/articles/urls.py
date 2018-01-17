from django.urls import path
from .api import ArticleDetailAPIView, CurrentArticlesAPIView
from .views import (
    IndexView,
    CurrentPageView,
    DetailPageView,
    ScheduledPageView,
)

app_name = 'articles'

urlpatterns = [
    path('current', CurrentPageView.as_view(), name='current_page'),
    path('scheduled', ScheduledPageView.as_view(), name='scheduled_page'),
    path('article', DetailPageView.as_view(), name='detail'),
    path('article/<int:article_id>', DetailPageView.as_view(), name='detail-id'),
    path('article/<int:article_id>/<int:version>', DetailPageView.as_view(), name='detail-id-version'),
    path('article/<int:article_id>/<int:version>/<str:run_id>',
         DetailPageView.as_view(),
         name='detail-id-version-run_id'),
    path('api/article/<str:article_id>', ArticleDetailAPIView.as_view(), name='api-article-detail'),
    path('api/current', CurrentArticlesAPIView.as_view(), name='api-current-articles'),
    path('', IndexView.as_view(), name='index'),


    # '/api/article_publication_status', methods=['POST']
    # '/api/article_schedule_for_range/from/<from_date>/to/<to_date>/'
    # '/api/article_scheduled_status', methods=['POST']
    # '/api/queue_article_publication', methods=['POST'] + remote [POST]
    # '/api/schedule_article_publication', methods=['POST']

]

# TODO version api endpoints, will require change to consumers urls
