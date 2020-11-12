from . import views
from django.urls import path
urlpatterns = [
    path('',views.product_list),
    path('<int:id>/',views.product_detail),

]