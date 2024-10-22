files_data = {}
with open('1.txt', encoding='utf-8') as file_1, \
     open('2.txt', encoding='utf-8') as file_2, \
     open('3.txt', encoding='utf-8') as file_3:
    files = [file_1, file_2, file_3]
    for i, file in enumerate(files):
        lines = file.readlines()
        line_count = len(lines)
        file_name = f"{i + 1}.txt"
        content = f"{file_name}\n{line_count}\n" + ''.join(lines)
        files_data[line_count] = content
sorted_files_data = dict(sorted(files_data.items()))
with open('4.txt', 'w', encoding='utf-8') as file_4:
    for content in sorted_files_data.values():
        file_4.write(content)

with open ('4.txt') as file_4:
    data = file_4.read()
    print(data)
