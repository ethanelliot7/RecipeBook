from django.urls import path,include

urlpatterns = [
    path('auth/', include('api.auth.urls'), name='auth'),
    path('user/', include('api.users.urls'), name='user'),

]
