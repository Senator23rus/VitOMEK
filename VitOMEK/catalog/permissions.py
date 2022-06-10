from django.http import Http404

class SalesmanPermissionsMixin:
    def has_permissions_salesman(self):
        return self.get_object().salesman == self.request.user