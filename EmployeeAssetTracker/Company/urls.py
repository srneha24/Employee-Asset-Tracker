from django.urls import path

from .views import (
    add_company,
    company_login,
    EmployeeView
)

app_name = 'Company'

urlpatterns = [
    path('new_company', add_company, name="AddCompany"),
    path('login', company_login, name='CompanyLogin'),
    path('employee/', EmployeeView.as_view(), name="Employee"),
    path('employee/<int:id>/', EmployeeView.as_view(), name="Employee")
]