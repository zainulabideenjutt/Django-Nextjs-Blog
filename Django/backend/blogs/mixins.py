from .permissions import IsStaffEditor
from rest_framework import permissions

class StaffEditorPermissionsMixin():
    permission_classes=[permissions.IsAdminUser,IsStaffEditor]
    # permission_classes=[
    #     # permissions.IsAdminUser,
    #                     # IsStaffEditor
    # ]