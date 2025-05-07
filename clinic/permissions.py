from rest_framework.permissions import BasePermission


class IsDoctorOrStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, "role"):
            return request.user.role == "staff" or obj.doctor.user == request.user
        return request.user.is_staff or obj.doctor.user == request.user
