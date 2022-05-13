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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == None or "":
      return False
    if user in group.get_users():
      return True 
    else:
      
      if len(group.get_groups())==0:
        return False
      else:
        for sub_group in group.get_groups():
          return is_user_in_group(user, sub_group)
    



  
    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("-----------Test Case 1-------")
print(is_user_in_group("sub_child_user", parent))  
### returns True
# Test Case 2
print("-----------Test Case 2-------")
print(is_user_in_group("child", child))
### returns True
# Test Case 3
print("-----------Test Case 3-------")
print(is_user_in_group("", child))
## returns False 
#Test Case 4
print("-----------Test Case 4-------")
print(is_user_in_group(None, child))
## returns False