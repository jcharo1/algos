import os

def main():
    
    return find_files()

def find_files(suffix, path):
    
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



print(find_files(".c", "./testdir"))