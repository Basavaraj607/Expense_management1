from django.urls import path
from . import views

app_name = "expenses"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create/", views.expense_create, name="create"),
    path("history/", views.history, name="history"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("manager/pending/", views.manager_pending, name="manager_pending"),
    path("manager/review/<int:pk>/", views.manager_review, name="manager_review"),
    path("manager/report/", views.manager_report, name="manager_report"),

]
