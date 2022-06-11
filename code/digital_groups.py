import gensim, logging
import glob, os, re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
new_model = gensim.models.Word2Vec.load('sentmodel2xPlusJalob2')
#morph = pymorphy2.MorphAnalyzer()

jalob=[]
description=[]
anamnez=[]
statement=[]
sent=[]
all_words = []
sluches = []
osmotrs = []
counter_0_0 = 0
counter_0_1 = 0
counter_1_0 = 0
counter_1_1 = 0

path=r"C:\Users\kolma\Desktop\медикопроект\temp\stac"

# Change path to files where data is supposed to be written
path_write_0_0=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac00"
path_write_0_1=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac01"
path_write_1_0=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac10"
path_write_1_1=r"C:\Users\kolma\Desktop\медикопроект\temp\stac_write\stac\stac11"

for filename in glob.glob(os.path.join(path, '*.xml')):
    f = open(filename, 'r', encoding='utf-8',errors='ignore')
    print(filename)
    s = ""
    for line in f:
        s += line.strip()
        sluches = re.findall("<SLUCH>(.*?)</SLUCH>", s)
    for j in range(len(sluches)):
        statement = re.findall("<HOSP_RESULT>(.*?)</HOSP_RESULT>", sluches[j])
        osmotrs = re.findall("<OSMOTR>(.*?)</OSMOTR>", sluches[j])
        lab = re.findall("<LAB_ISSL>(.*?)", sluches[j])
        for k in range(len(osmotrs)):
            resultEpic = re.findall("<USL>(.*?)</USL>", osmotrs[k])
            if (len(resultEpic)>0 and resultEpic[0]!="Выписной эпикриз"):
                jalob = re.findall("<JALOB>(.*?)</JALOB>", osmotrs[k])
                description = re.findall("<DESCRIPTION>(.*?)</DESCRIPTION>", osmotrs[k])
                anamnez = re.findall("<ANAMNEZ>(.*?)</ANAMNEZ>", osmotrs[k])
                anamnez = list(filter(None, anamnez))
                words_anamnez = []
                for i in range(len(anamnez)):
                    anamnez[i] = re.sub(r"(_)+", r" ", anamnez[i])
                    anamnez[i] = re.sub(r"([а-я])([А-Я])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([0-9])([А-Я])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([0-9])([A-Z])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([0-9])([a-z])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([a-z])([0-9])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([A-Z])([0-9])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([А-Я])([0-9])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([а-я])([0-9])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([а-я])([A-Z])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([a-z])([А-Я])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([0-9])([а-я])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([A-Z])([А-Я])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([a-z])([а-я])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([а-я])([a-z])", r"\1 \2", anamnez[i])
                    anamnez[i] = re.sub(r"([а-я])((_)+)([а-я])", r"\1 \3", anamnez[i])
                    anamnez[i] = re.sub(r"([а-я])(\.)([А-Я])", r"\1 |\3", anamnez[i])
                    anamnez[i] = re.sub(r"([а-я])(\.)(\s)([А-Я])", r"\1 |\4", anamnez[i])
                    anamnez[i] = re.sub(r"([А-Я])([А-Я])([а-я])", r"\1 \2\3", anamnez[i])
                    anamnez[i] = re.sub(r"([А-Я])([А-Я])(\.)([А-Я])", r"\1\2 |\4", anamnez[i])
                    anamnez[i] = re.sub(r'[^\w\d+\s|]', ' ', anamnez[i])
                    anamnez[i] = re.sub(r'(\+)', ' ', anamnez[i])
                    anamnez[i] = re.sub(r"quot", r"", anamnez[i])
                    anamnez[i] = re.sub(r"6F", r"", anamnez[i])
                    words_anamnez.extend(anamnez[i].split(' |'))
                for i in range(len(words_anamnez)):
                    words_anamnez[i] = words_anamnez[i].split(' ')
                description = list(filter(None, description))
                words_description = []
                for i in range(len(description)):
                    description[i] = re.sub(r"(_)+", r" ", description[i])
                    description[i] = re.sub(r"([а-я])([А-Я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([0-9])([А-Я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([0-9])([а-я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([a-z])([а-я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([а-я])([a-z])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([A-Z])([А-Я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([0-9])([A-Z])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([0-9])([a-z])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([a-z])([0-9])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([A-Z])([0-9])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([А-Я])([0-9])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([а-я])([0-9])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([а-я])([A-Z])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([a-z])([А-Я])", r"\1 \2", description[i])
                    description[i] = re.sub(r"([а-я])((_)+)([а-я])", r"\1 \3", description[i])
                    description[i] = re.sub(r"([а-я])(\.)([А-Я])", r"\1 |\3", description[i])
                    description[i] = re.sub(r"([а-я])(\.)(\s)([А-Я])", r"\1 |\4", description[i])
                    description[i] = re.sub(r"([А-Я])([А-Я])([а-я])", r"\1 \2\3", description[i])
                    description[i] = re.sub(r"([А-Я])([А-Я])(\.)([А-Я])", r"\1\2 |\4", description[i])
                    description[i] = re.sub(r'[^\w\d+\s|]', ' ', description[i])
                    description[i] = re.sub(r'(\+)', ' ', description[i])
                    description[i] = re.sub(r"quot", r"", description[i])
                    description[i] = re.sub(r"6F", r"", description[i])
                    words_description.extend(description[i].split(' |'))
                for i in range(len(words_description)):
                    words_description[i] = words_description[i].split(' ')
                jalob = list(filter(None, jalob))
                words_jalob = []
                for i in range(len(jalob)):
                    jalob[i] = re.sub(r"(_)+", r" ", jalob[i])
                    jalob[i] = re.sub(r"([а-я])([А-Я])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([0-9])([А-Я])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([0-9])([а-я])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([a-z])([а-я])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([а-я])([a-z])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([A-Z])([А-Я])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([0-9])([A-Z])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([0-9])([a-z])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([a-z])([0-9])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([A-Z])([0-9])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([А-Я])([0-9])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([а-я])([0-9])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([а-я])([A-Z])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([a-z])([А-Я])", r"\1 \2", jalob[i])
                    jalob[i] = re.sub(r"([а-я])((_)+)([а-я])", r"\1 \3", jalob[i])
                    jalob[i] = re.sub(r"([а-я])(\.)([А-Я])", r"\1 |\3", jalob[i])
                    jalob[i] = re.sub(r"([а-я])(\.)(\s)([А-Я])", r"\1 |\4", jalob[i])
                    jalob[i] = re.sub(r"([А-Я])([А-Я])([а-я])", r"\1 \2\3", jalob[i])
                    jalob[i] = re.sub(r"([А-Я])([А-Я])(\.)([А-Я])", r"\1\2 |\4", jalob[i])
                    jalob[i] = re.sub(r'[^\w\d+\s|]', ' ', jalob[i])
                    jalob[i] = re.sub(r'(\+)', ' ', jalob[i])
                    jalob[i] = re.sub(r"quot", r"", jalob[i])
                    jalob[i] = re.sub(r"6F", r"", jalob[i])
                    words_jalob.extend(jalob[i].split(' |'))
                for i in range(len(words_jalob)):
                    words_jalob[i] = words_jalob[i].split(' ')

        result_labs = re.findall("<LAB_ISSL>(.*)", sluches[j])
        if (len(result_labs)>0):
            for k in range(len(result_labs)):
                result_lab = re.findall("<RESULT>(.*?)</RESULT>", result_labs[k])
                result_lab = list(filter(None, result_lab))
                words_result_lab = []
                for i in range(len(result_lab)):
                    result_lab[i] = re.sub(r"(_)+", r" ", result_lab[i])
                    result_lab[i] = re.sub(r"([а-я])([А-Я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([0-9])([А-Я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([0-9])([а-я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([a-z])([а-я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([а-я])([a-z])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([A-Z])([А-Я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([0-9])([a-z])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([0-9])([A-Z])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([a-z])([0-9])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([A-Z])([0-9])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([А-Я])([0-9])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([а-я])([0-9])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([а-я])([A-Z])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([a-z])([А-Я])", r"\1 \2", result_lab[i])
                    result_lab[i] = re.sub(r"([а-я])((_)+)([а-я])", r"\1 \3", result_lab[i])
                    result_lab[i] = re.sub(r"([а-я])(\.)([А-Я])", r"\1 |\3", result_lab[i])
                    result_lab[i] = re.sub(r"([а-я])(\.)(\s)([А-Я])", r"\1 |\4", result_lab[i])
                    result_lab[i] = re.sub(r"([А-Я])([А-Я])([а-я])", r"\1 \2\3", result_lab[i])
                    result_lab[i] = re.sub(r"([А-Я])([А-Я])(\.)([А-Я])", r"\1\2 |\4", result_lab[i])
                    result_lab[i] = re.sub(r'[^\w\d+\s|]', ' ', result_lab[i])
                    result_lab[i] = re.sub(r'(\+)', ' ', result_lab[i])
                    result_lab[i] = re.sub(r"quot", r"", result_lab[i])
                    result_lab[i] = re.sub(r"6F", r"", result_lab[i])
                    words_result_lab.extend(result_lab[i].split(' |'))
            for i in range(len(words_result_lab)):
                words_result_lab[i] = words_result_lab[i].split(' ')

        sent = list(words_anamnez + words_description + words_jalob + words_result_lab)
        all_words = sent

        if (statement[0]=="Умер" or
            statement[0]=="Умер в приёмном покое"):
            counter_0_0 = counter_0_0 + 1
            filename_write = path_write_0_0 + "\sta" + str(counter_0_0) + ".txt"
        elif (statement[0] == "Выписан с улучшением/стандарт не выполнен" or
              statement[0] == "Самовольно прерванное лечение без перемен" or
              statement[0] == "Переведен в другую больницу без перемен" or
              statement[0] == "Выписан без перемен" or
              statement[0] == "Переведен в другое отделение" or
              statement[0] == "Переведен в другую больницу с улучшением" or
              statement[0] == "Выписан с ухудшением (Переведен в др ЛПУ)" or
              statement[0] == "Выписан из дневного в круглосуточный стационар с ухудшением" or
              statement[0] == "Лечение прервано по инициативе пациента с улучшением" or
              statement[0] == "Лечение прервано по инициативе ЛПУ без перемен" or
              statement[0] == "Лечение прервано по инициативе пациента без перемен"):
            counter_1_0 = counter_1_0 + 1
            filename_write = path_write_1_0 + "\sta" + str(counter_1_0) + ".txt"
        elif (statement[0] == "Выписан с улучшением/стандарт выполнен" or
              statement[0] == "Выписан с выздоровлением"):
            counter_1_1 = counter_1_1 + 1
            filename_write = path_write_1_1 + "\sta" + str(counter_1_1) + ".txt"
        else: print("MISTAKE")
        f_write = open(filename_write, 'w')
        all_words = list(filter(None, all_words))
        for i in range(len(all_words)):
            all_words[i] = list(filter(None, all_words[i]))
            for j in range(len(all_words[i])):
                all_words[i][j] = all_words[i][j].lower()
                all_words[i][j] = all_words[i][j].replace(u'ё', u'e')
                try:
                    if (j+1==len(all_words[i])):
                        temp = str(new_model.wv.__getitem__(all_words[i][j]))
                        temp = re.sub(r'(\d)(\s+)(\d)', r'\1, \3', temp)
                        f_write.write(str(temp))
                    else:
                        f_write.write(str(new_model.wv.__getitem__(all_words[i][j])) + ", ")
                except Exception:
                    print(all_words[i][j])

        f_write.close()
