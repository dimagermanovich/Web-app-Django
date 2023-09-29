from django.urls import path
from . import views

urlpatterns = [
    path('', views.sia, name='sick_leaves'),
    path('incapable', views.infoIncapables, name='incapable'),
    path('create', views.create, name='create'),
    path('createincapable', views.createIncapable, name='createIncapable'),
    path('incapable/<int:pk>', views.IncapablesDetailView.as_view(), name='incap_det'),
    path('<int:pk>', views.LeaveDetailView.as_view(), name='leave_det'),
    path('incapable/<int:pk>/all_l', views.testfunc, name='func'),
    path('<int:pk>/update', views.DetailUpdateView.as_view(), name='leave_update'),
    path('incapable/<int:pk>/update', views.DetailIncapableUpdateView.as_view(), name='incapable_update'),
    path('<int:pk>/delete', views.DetailDeleteView.as_view(), name='leave_delete'),
    path('incapable/<int:pk>/delete', views.DetailIncapableDeleteView.as_view(), name='incapable_delete'),
]
