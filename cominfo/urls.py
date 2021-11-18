# urls for the cominfo app


from django.urls import path
from . views import CominfoListView, CominfoThumbsView, CominfoDetailView, CominfoCreateView, CominfoUpdateView, CominfoDeleteView

urlpatterns = [
    path('list/', CominfoListView.as_view(), name='cominfo-list'),
    path('thumbs/<int:category_id>', CominfoThumbsView.as_view(), name='cominfo-thumbs'),
    path('detail/<int:pk>', CominfoDetailView.as_view(), name='cominfo-details'),
    path('create/', CominfoCreateView.as_view(), name='cominfo-create'),
    path('update/<int:pk>', CominfoUpdateView.as_view(), name='cominfo-update'),
    path('delete/<int:pk>', CominfoDeleteView.as_view(), name='cominfo-delete'),
]