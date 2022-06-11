import gensim, logging
import glob, os, re, nltk

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

hlist=[]
idlist=[]
codelist=[]
result=[]
jalob = []
description=[]
ii=int(1)
sent=[]
all_words = []

path=r"C:\Users\kolma\Desktop\медикопроект\temp\stac"
for filename in glob.glob(os.path.join(path, '*.xml')):
    f = open(filename, 'r', encoding='utf-8',errors='ignore')
    print(filename)
    s = ""
    for line in f:
        s += line.strip()
        result = re.findall("<RESULT>(.*?)</RESULT>", s)
        description = re.findall("<DESCRIPTION>(.*?)</DESCRIPTION>", s)
        anamnez = re.findall("<ANAMNEZ>(.*?)</ANAMNEZ>", s)
        jalob =  re.findall("<JALOB>(.*?)</JALOB>", s)
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
        anamnez[i] = re.sub(r'[^\w\d+\s|]', ' ', anamnez[i])
        #anamnez[i] = re.sub(r'\d+', '', anamnez[i])
        words_anamnez.extend(anamnez[i].split(' |'))
    for i in range(len(words_anamnez)):
        words_anamnez[i] = words_anamnez[i].split(' ')

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
        jalob[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", jalob[i])
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
        jalob[i] = re.sub(r'[[^\w\d+\s|]]', ' ', jalob[i])
        words_jalob.extend(jalob[i].split(' |'))
    for i in range(len(words_jalob)):
        words_jalob[i] = words_jalob[i].split(' ')

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
        description[i] = re.sub(r'[^\w\d+\s|]', ' ', description[i])
        #description[i] = re.sub(r'\d+', '', description[i])
        words_description.extend(description[i].split(' |'))
    for i in range(len(words_description)):
        words_description[i] = words_description[i].split(' ')

    result = list(filter(None, result))
    words_result = []
    for i in range(len(result)):
        result[i] = re.sub(r"(_)+", r" ", result[i])
        result[i] = re.sub(r"([а-я])([А-Я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([0-9])([А-Я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([0-9])([а-я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([A-Z])([а-я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([a-z])([а-я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([a-z])([а-я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([а-я])([a-z])", r"\1 \2", result[i])
        result[i] = re.sub(r"([A-Z])([А-Я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([0-9])([A-Z])", r"\1 \2", result[i])
        result[i] = re.sub(r"([0-9])([a-z])", r"\1 \2", result[i])
        result[i] = re.sub(r"([a-z])([0-9])", r"\1 \2", result[i])
        result[i] = re.sub(r"([A-Z])([0-9])", r"\1 \2", result[i])
        result[i] = re.sub(r"([А-Я])([0-9])", r"\1 \2", result[i])
        result[i] = re.sub(r"([а-я])([0-9])", r"\1 \2", result[i])
        result[i] = re.sub(r"([а-я])([A-Z])", r"\1 \2", result[i])
        result[i] = re.sub(r"([a-z])([А-Я])", r"\1 \2", result[i])
        result[i] = re.sub(r"([а-я])((_)+)([а-я])", r"\1 \3", result[i])
        result[i] = re.sub(r"([а-я])(\.)([А-Я])", r"\1 |\3", result[i])
        result[i] = re.sub(r"([а-я])(\.)(\s)([А-Я])", r"\1 |\4", result[i])
        result[i] = re.sub(r"([А-Я])([А-Я])([а-я])", r"\1 \2\3", result[i])
        result[i] = re.sub(r'[^\w\d+\s|]', ' ', result[i])
        words_result.extend(result[i].split(' |'))
    for i in range(len(words_result)):
        words_result[i] = words_result[i].split(' ')

    sent = list(words_anamnez + words_description + words_result + words_jalob)
    all_words = list(all_words + sent)

count = 0
sentences = all_words
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        sentences[i][j] = sentences[i][j].lower()
        sentences[i][j] = sentences[i][j].replace(u'ё', u'e')
    sentences[i] = list(filter(None, sentences[i]))
    count = count + len(sentences[i])
sentences = list(filter(None, sentences))

print("Всего слов - " + str(count))

model = gensim.models.Word2Vec(sentences, min_count=0, size=1, window=6)

try:
    print(model.wv.most_similar(positive=['лечение', 'c'], negative=['миокарда'], topn=10))
    print(model.wv.similarity('миокарда', 'врач'))
except Exception:
    print("ups...")

model.save('sentmodel2xPlusJalob2')


#new_model = gensim.models.Word2Vec.load('sentmodel')
#for i in range(len(sentences)):
#    for j in range(len(sentences[i])):
#        print(sentences[i][j] + str(new_model.wv.__getitem__(sentences[i][j])))

#new_model = gensim.models.Word2Vec.load('sentmodel')
