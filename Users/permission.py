from rest_framework.permissions import BasePermission

class productmanager(BasePermission):
     def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'productmanager', False )


class cartmanager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'cartmanager', False )
