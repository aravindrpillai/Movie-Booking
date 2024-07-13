from django.urls import path
from src.apis import agency,branches

urlpatterns = [
   path('agency/add', agency.add_agency),
   path('branches/add', branches.add_branch),
]
