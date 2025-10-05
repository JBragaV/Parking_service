from rest_framework import permissions


class IsOwnerOfVehicleOrRecord(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(obj, 'owner'):
            print()
            print()
            print()
            print(obj, '============================')
            print()
            print()
            print()
            return obj.owner and obj.owner.user == user
        print(obj)
        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
            print()
            print()
            print()
            print(obj, '============================')
            print()
            print()
            print()
            return obj.vehicle.owner and obj.vehicle.owner.user == user

        return False
