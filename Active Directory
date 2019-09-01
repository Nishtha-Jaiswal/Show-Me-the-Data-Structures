class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True # we found the user
    else:
        if len(group.get_groups()) == 0:
            return False # user not found
        else:
            for members in group.get_groups():
                active_mem = is_user_in_group(user,members)

                if active_mem:
                    return True
                else:
                    return False
    
    return None
        
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
parent.add_user(parent_user)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group(sub_child_user, parent))
# True
print(is_user_in_group(sub_child_user, child))
# True
print(is_user_in_group(sub_child_user, sub_child))
#True

print(is_user_in_group(child_user, parent))
# True
print(is_user_in_group(child_user, child))
# True
print(is_user_in_group(child_user, sub_child))
# False

print(is_user_in_group(parent_user, parent))
# True
print(is_user_in_group(parent_user, child))
# False
print(is_user_in_group(parent_user, sub_child))
# False

