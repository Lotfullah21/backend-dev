from django.urls import path
from .views import courses, get_path,get_user_info,get_course_path_info, get_course_query_string, show_form,capture_form


urlpatterns = [
    path("", courses, name="home_view"),
    path("path/",get_path),
    path("info",get_user_info),
    path("course-info/<name>/<id>",get_course_path_info),
    path("course-info/",get_course_query_string),
    path("show-form/",show_form),
    path("capture-form/",capture_form)
]
