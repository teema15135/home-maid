from django.contrib import admin
from django.urls import path

from maids.views import MaidListView

urlpatterns = [
    path('', MaidListView.as_view(), name='maid-list'),
]
