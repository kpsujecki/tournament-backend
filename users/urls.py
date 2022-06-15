from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, ShowProfile, GetUsers

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('active-users/', GetUsers.as_view(), name='get_all_users'),
    path('', ShowProfile.as_view()),
]
