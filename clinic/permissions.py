from rest_framework import permissions


class IsDoctorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Allow doctors to view/edit only their own appointments.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods like GET are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # If user is a doctor and owns the object, allow edit
        return hasattr(request.user, "doctor") and obj.doctor.user == request.user
