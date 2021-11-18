"""_djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . views import VideoListView, VideoThumbsView, VideoDetailView, VideoCreateView, VideoUpdateView, VideoDeleteView


urlpatterns = [
    path('list/', VideoListView.as_view(), name='videos-list'),
    path('thumbs/<int:category_id>', VideoThumbsView.as_view(), name='videos-thumbs'),
    path('detail/<int:pk>', VideoDetailView.as_view(), name='videos-details'),
    path('create/', VideoCreateView.as_view(), name='videos-create'),
    path('update/<int:pk>', VideoUpdateView.as_view(), name='videos-update'),
    path('delete/<int:pk>', VideoDeleteView.as_view(), name='videos-delete'),
]
