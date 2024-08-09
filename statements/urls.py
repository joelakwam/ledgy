from django.urls import path
from .views import StatementListCreate, StatementRetrieveUpdateDestroy
from .views import ProtectedView

urlpatterns = [
    path('statements/', StatementListCreate.as_view(), name='statement-list-create'),
    path('statements/<int:pk>/', StatementRetrieveUpdateDestroy.as_view(), name='statement-detail'),
    path('protected/', ProtectedView.as_view(), name='protected-view')
]
