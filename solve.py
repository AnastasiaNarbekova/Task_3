import os
def read_files_in_directory(directory):
    files_data = {}
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and filename.endswith('.txt'):
            with open(os.path.join(directory, filename), encoding='utf-8') as file:
                lines = file.readlines()
                line_count = len(lines)
                content = f"{filename}\n{line_count}\n" + ''.join(lines)
                files_data[line_count] = content
    sorted_files_data = dict(sorted(files_data.items()))
    with open(os.path.join(directory, '4.txt'), 'w', encoding='utf-8') as file_4:
        for content in sorted_files_data.values():
            file_4.write(content)
    with open(os.path.join(directory, '4.txt'), 'r', encoding='utf-8') as file_4:
        data = file_4.read()
        print(data)
directory_path = '/Users/anastasianarbekova/Desktop/Task_3'
read_files_in_directory(directory_path)
