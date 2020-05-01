from rest_framework import permissions

class UpdateOwnProfiles(permissions.BasePermission):
    #allow users to edit their own permissions
    def has_object_permission(self,request,view,obj):
        #check user is trying to edit their own profile
        #safe methods will not make any changes to objects
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.id == obj.id:
            return True
        return False

class UpdateOwnStatus(permissions.BasePermission):
    #allow users to edit their own permissions
    def has_object_permission(self,request,view,obj):
        #check user is trying to edit their own profile
        #safe methods will not make any changes to objects
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.id == obj.user_profile.id:
            return True
        return False