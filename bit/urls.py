from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name = "index"),
    path ('about/', views.about, name = "about"),
    path ('contact/', views.contact, name = "contact"),
    path ('crypto-exchange/', views.crypto_exchange, name = "crypto_exchange"),
    path ('deposit/', views.deposit, name = "deposit"),
    path ('faq/', views.faq, name = "faq"),
    path ('status/', views.status, name = "status"),
    path ('home/', views.home, name = "home"),
    path ('login/', views.LoginPage, name = "login"),
    path ('plan1/', views.plan1, name = "plan1"),
    path ('plan2/', views.plan2, name = "plan2"),
    path ('plan3/', views.plan3, name = "plan3"),
    path ('plan4/', views.plan4, name = "plan4"),
    path ('profile/', views.profile, name = "profile"),
    path ('pricing/', views.pricing, name = "pricing"),
    path ('profit/', views.profit, name = "profit"),
    path ('refer/', views.refer, name = "refer"),
    path ('register/', views.registerPage, name = "register"),
    path ('logout/', views.logoutUser, name = "logout"),
    path ('services', views.services, name = "services"),
    path ('settings', views.settings, name = "settings"),
    path ('terms', views.terms, name = "terms"),
    path ('transaction', views.transaction, name = "transaction"),
    path ('withdraw', views.withdraw, name = "withdraw"),
    path ('forgotten_password', views.forgotten_password, name = "forgotten_password"),
    path ('reset_password', views.reset_password, name = "reset_password"),

    ]