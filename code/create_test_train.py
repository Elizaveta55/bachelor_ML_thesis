import logging
import glob, os, re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
code_0_0 = []
i=0
s=[]

path=r"C:\Users\kolma\Desktop\медикопроект\temp\stac"
path_write_0_0=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac00"
path_write_0_1=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac01"
path_write_1_0=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac10"
path_write_1_1=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac11"
filename_x_train =r"C:\Users\kolma\Desktop\медикопроект\temp\stac\x_train.txt"
filename_y_train = r"C:\Users\kolma\Desktop\медикопроект\temp\stac\y_train.txt"
filename_x_test = r"C:\Users\kolma\Desktop\медикопроект\temp\stac\x_test.txt"
filename_y_test = r"C:\Users\kolma\Desktop\медикопроект\temp\stac\y_test.txt"
f_write_x_train = open(filename_x_train, 'w')
f_write_y_train = open(filename_y_train, 'w')
f_write_x_test = open(filename_x_test, 'w')
f_write_y_test = open(filename_y_test, 'w')
for filename in glob.glob(os.path.join(path_write_0_0, '*.txt')):
    f = open(filename, 'r', encoding='utf-8',errors='ignore')
    s = f.read()
    print(filename)
    if (i<75):
        f_write_x_train.write("[")
        data = re.sub(r'\[', r'', s)
        data = re.sub(r'\]', r'', data)
        f_write_x_train.write(data)
        f_write_x_train.write("] ")
        f_write_x_train.write('\n')
        f_write_y_train.write("[0]")
        f_write_y_train.write('\n')
    else:
        f_write_x_test.write("[")
        data = re.sub(r'\[', r'', s)
        data = re.sub(r'\]', r'', data)
        f_write_x_test.write(data)
        f_write_x_test.write("] ")
        f_write_x_test.write('\n')
        f_write_y_test.write("[0]")
        f_write_y_test.write('\n')
    i=i+1


i=0
for filename in glob.glob(os.path.join(path_write_1_0, '*.txt')):
    f = open(filename, 'r', encoding='utf-8',errors='ignore')
    s = f.read()
    print(filename)
    if (i<1000):
        f_write_x_train.write("[")
        data = re.sub(r'\[', r'', s)
        data = re.sub(r'\]', r'', data)
        f_write_x_train.write(data)
        f_write_x_train.write("] ")
        f_write_x_train.write('\n')
        f_write_y_train.write("[0]")
        f_write_y_train.write('\n')
    else:
        f_write_x_test.write("[")
        data = re.sub(r'\[', r'', s)
        data = re.sub(r'\]', r'', data)
        f_write_x_test.write(data)
        f_write_x_test.write("] ")
        f_write_x_test.write('\n')
        f_write_y_test.write("[0]")
        f_write_y_test.write('\n')
    i=i+1


i=0
j=0
for filename in glob.glob(os.path.join(path_write_1_1, '*.txt')):
    if (j<1330):
        f = open(filename, 'r', encoding='utf-8',errors='ignore')
        s = f.read()
        print(filename)
        if (i<5000):
            f_write_x_train.write("[")
            data = re.sub(r'\[', r'', s)
            data = re.sub(r'\]', r'', data)
            f_write_x_train.write(data)
            f_write_x_train.write("] ")
            f_write_x_train.write('\n')
            f_write_y_train.write("[1]")
            f_write_y_train.write('\n')
        else:
            f_write_x_test.write("[")
            data = re.sub(r'\[', r'', s)
            data = re.sub(r'\]', r'', data)
            f_write_x_test.write(data)
            f_write_x_test.write("] ")
            f_write_x_test.write('\n')
            f_write_y_test.write("[1]")
            f_write_y_test.write('\n')
        i=i+1

f_write_y_test.close()
f_write_x_test.close()
f_write_y_train.close()
f_write_x_train.close()
