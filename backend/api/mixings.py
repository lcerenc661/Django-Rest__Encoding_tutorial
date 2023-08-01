from rest_framework import permissions

from api.permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [
        IsStaffEditorPermission,
        permissions.IsAdminUser,
        ]