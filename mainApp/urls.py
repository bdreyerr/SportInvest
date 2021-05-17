from mainApp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='index'),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('logout', views.logout_request, name='logout'),
    path('team/<slug:slug>/', views.team_view, name='team_view'),
    path('team/<slug:slug>', views.team_view, name='team_view'),
    path('transactions', views.transactions, name='transactions'),
    path('banking', views.banking, name='banking'),
    path('market', views.market, name='market'),
    path('chart', views.ChartData.as_view()),
    path('teamChart/<slug:slug>/', views.TeamChartData.as_view()),
    path('about', views.about, name='about'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
