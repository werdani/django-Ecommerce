from . import views
from django.urls import path
urlpatterns = [
    path('',views.product_list),
    path('detail/',views.product_detail),

]