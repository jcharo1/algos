import os

def find_files(suffix, path):
  
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_current_files = os.listdir(f"{path}")
    files_found = []
    for file in list_of_current_files:
      
      if os.path.isdir(f'./{file}'):   # is this a directory if so continue serarching
        print(file)
        find_files(suffix,path)
      else:                               # else it is not a directory it is a file 


       if os.path.isfile(f"./{file}"): 
         print("i made it here")
         if (f"{file}".endswith(suffix)): #check if it ends with suffix
           print("and here tooo")
           files_found.append(f"{file}") 
      print(files_found)
        

    
          

    
    
    

    return None



find_files(".c", "./testdir")
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3