import os

def find_files(suffix, path):
    assert(type(suffix) == str), "Suffix has to be a string"
    assert(type(path) == str), "Path has to be a string"
    if not os.path.isdir(path):
        return 'Invalid Directory'
    list_of_current_files = os.listdir(path)
    
    files_found = []
    for item in list_of_current_files:
        item_path = os.path.join(path,item)

        if os.path.isdir(item_path):
            output = find_files(suffix, item_path)
            files_found += output
        else:
            if os.path.isfile(item_path):
                if (f"{item_path}".endswith(suffix)):
                    files_found.append(item_path)

     
        
        
    
    return files_found


print("-----------Test Case 1-------")
print(find_files(".c", "./testdir"))  
## test 1 returns  
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
print("-----------Test Case 2-------")
print(find_files(".h", "./testdir"))
## test 2 returns
# ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']
print("-----------Test Case 3-------")
print(find_files(".pow", "./testhhhdir"))
## test 3 returns invalid directory


print("-----------Test Case 4-------")
print(find_files(56, "./testhhhdir"))
#returns AssertionError: Suffix has to be a string
