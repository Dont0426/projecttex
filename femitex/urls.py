from django.urls import path
from femitex import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'), 
    path('create-post/', views.createpost, name='createpost'),   
    path('side_bar/', views.side_bar, name='Side_bar'),    
    path('details/<int:pk>', views.post_detail, name='post-detail'),    
    path('login/', auth_views.LoginView.as_view(template_name = 'femitex/builtin-login.html'), name='loginpage'),    
    path('logout/', auth_views.LogoutView.as_view(template_name = 'femitex/builtin-logout.html'), name='logoutpage'),   
    path('plist/', views.PostListView.as_view(template_name = 'femitex/plist.html'), name='listpage'),
    path('pdetail/<int:pk>', views.PostDetailView.as_view(template_name = 'femitex/pdetail.html'), name='detailpage'), 
    path('create/', views.ClassCreatePost.as_view(), name='classcreatepost'), 
    path('update/<int:pk>/', views.ClassUpdatePost.as_view(template_name = 'femitex/post_update.html' ), name='classupdatepost'),
    path('delete/<int:pk>/', views.ClassDeletePost.as_view(), name='classdeletepost'),
    path('funcdelete/<int:pk>/', views.postdelete, name='func_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
