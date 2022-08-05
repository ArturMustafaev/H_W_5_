"""magazin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views
from profile_app import views as user_views
from movie_app import views as movie_views
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test_view),
    path('api/v1/categories/', views.CategoryListAPIView.as_view()),
    path('api/v1/categories/<int:id>', views.CategoryItemUpdateDeleteAPIView.as_view()),
    path('api/v1/categories/', views.CategoryAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/directors/', movie_views.director),
    path('api/v1/movies', movie_views.MovieAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/reviews', movie_views.ReviewAPIViewSet.as_view({
            'get': 'list', 'post': 'create'
    })),
    path('api/v1/movies/reviews', movie_views.review_list_view),
    path('api/v1/directors', movie_views.DirectorAPIViewSet.as_view({
            'get': 'list', 'post': 'create'
    })),
    path('api/v1/products/', views.product_list_view),
    path('api/v1/product/<int:id>/', views.product_item_view),
    path('api/v1/authorization/', user_views.authorization),
    path('api/v1/registratuion/', user_views.registration),
]

urlpatterns += swagger.urlpatterns
