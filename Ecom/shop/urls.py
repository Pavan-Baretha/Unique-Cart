
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('admin/',admin.site.urls),
     path("",views.index,name = "ShopHome"),
     path("shop/about/",views.about,name = "AboutUs"),
     path("shop/contact/",views.contact,name = "ConatctUs"),
     path("shop/tracker/",views.tracker,name = "TrackingStatus"),
     path("shop/search/",views.search,name = "Search"),
     path("shop/products/<int:myid>",views.productView,name = "ProductView"),
     path("shop/checkout/",views.checkout,name = "Checkout"),

] 

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
     urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


     