from rest_framework import permissions

from api.permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [
        IsStaffEditorPermission,
        permissions.IsAdminUser,
    ]


class UserQuerysetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        queryset = super().get_queryset(*args, **kwargs)
        if user.is_staff:
            return queryset
        return queryset.filter(**lookup_data)
