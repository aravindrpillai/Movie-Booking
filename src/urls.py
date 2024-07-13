from django.urls import path
from src.apis import agency,branches,screens

urlpatterns = [
   path('agency/add', agency.add_agency),
   path('branches/add', branches.add_branch),
   path('screens/add', screens.add_screens)
]
