
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('resume/', jobs.views.resume, name='resume'),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
