from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    # Core URLS
    path("", include('itscsapp.core.urls')),
    # Carrers URLS
    path("carrers/", include('itscsapp.carrers.urls')),
    # Contact URLS
    path("contact-us/", include('itscsapp.contact.urls')),
    # Researches URLS
    path("", include('itscsapp.research.urls')),
    # URL Create Coment
    path("", include('itscsapp.comment.urls')),
    #URls of Evetns Views
    path("", include('itscsapp.events.urls')),
    #Urls of Blogs Views
    path("",include('itscsapp.blog.urls')),
    #URls Admision
    path("", include('itscsapp.admision.urls')),

    # About Urls
    path("about/", include('itscsapp.about.urls')),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("itscsapp.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
