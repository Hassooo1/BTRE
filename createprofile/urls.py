from django.urls import path


from . import views

urlpatterns = [
    path('profiles/', views.profiles, name = "profiles"),
    path('createprofile/', views.cprofiles, name = "createprofile"),
    path('profiles/delete/<int:id>/', views.delete, name="delete"),
    # path('profiles/update/<int:id>/', views.update, name="update"),
    path('profiles/updateprofile/<int:id>', views.updateprofile, name='updateprofile'),

]