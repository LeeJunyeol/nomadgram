from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex='^explore/$',
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    )

]
