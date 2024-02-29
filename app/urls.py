from django.urls import path

from .views import ExploreView, DetailsView, AuthorView, CreatView,  UserLoginview, UserRegisterView, homeView, product_updateView

urlpatterns = [
    path('', homeView, name = 'home-page' ),
    path('explore/', ExploreView.as_view(), name = 'explore-page' ),
    path('detail/', DetailsView.as_view(), name = 'detail-page' ),
    path('author/', AuthorView.as_view(), name = 'author-page' ),
    path('create/', CreatView.as_view(), name = 'create-page' ),    
    path('login/', UserLoginview.as_view(), name = 'login-page' ),    
    path('register/', UserRegisterView.as_view(), name = 'register-page' ),
    path('update/<pk>', product_updateView, name = 'update-page'),    

]
