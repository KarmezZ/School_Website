from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('rekrutacja/', views.rekrutacja_page, name='rekrutacja_page'),
    path('aktualności/', views.news_page, name='news_page'),
    path('informacje_dla_rodziców/', views.info_for_parent_page, name='info_parents_page'),
    path('sekretariat/', views.sekretariat_page, name='sekretariat_page'),
    path('zdjęcia/', views.photos_page, name='zdjęcia_page')
]
