import os

def generate_file_list(directory='.'):
    file_list = []
    
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            file_info = {
                'file_name': file_name,
                'file_path': file_path,
                'file_size': file_size
            }
            file_list.append(file_info)
    return file_list

file_list = generate_file_list()
for file_info in file_list:
    print(file_info)
