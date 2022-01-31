from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from users_app.views import ProfileAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Vue&Django API Snippets",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="pramezani92@gmail.com"),
        license=openapi.License(name="order by Parsa"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  # /*-------------djoser----------------*/

                  path('admin/', admin.site.urls),
                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.authtoken')),

                  # /*-------------apps----------------*/
                  path('', include('users_app.urls')),
                  path('post/', include('blog_app.urls')),

                  # /*-----------swagger---------------*/
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
