from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import blurdetect.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("fileupload/", hello.views.simple_upload, name="simple_upload"),
    path("formupload/", hello.views.model_form_upload, name="model_form_upload"),
    path("blurdetect/", blurdetect.views.detect, name="detect"),
    path("output/", blurdetect.views.output, name="script"),
    path("bd/", blurdetect.views.start_page, name="start"),
    path("bdupload/", blurdetect.views.bd_upload, name="upload")
]
