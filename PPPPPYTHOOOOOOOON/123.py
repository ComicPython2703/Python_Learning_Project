# coding=utf-8
file = open("静夜思.txt", "a+", encoding='utf8')
seq = ['床前明月光，\n', '疑是地上霜。\n', '举头望明月，\n', '低头思故乡。']
file.writelines(seq)
file.seek(0, 0)
info = file.read()
print(info)
file.close()
