'''
统计任一英文文本文件，单词出现的个数
'''
import re
def count_words(file_path):
    with open(file_path) as file:
        text = file.read()
        words = re.findall(r'[a-zA-Z]+',text)
        count = len(words)
    return count

print(count_words('e:\english.txt'))