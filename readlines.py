import glob
import os


f = open("concatenate_texts.txt", "r", encoding = "UTF8")

print("텍스트 길이 : %d" % (len(f.readlines())))

f.close()
