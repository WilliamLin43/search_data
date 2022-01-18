# imports needed and set up logging
import gensim
import logging
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import unicodedata

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#input_file="./dataset/COVID-19_MIS-C_sentence_T.txt"
#input_file="./dataset/COVID-19_Endometriosis_sentence_T.txt"
input_file="./dataset/COVID-19_MIS-C_Endometriosis_sentence.txt"
#input_file="./dataset/MIS-C_Endometriosis_sentence.txt"
#input_file="./dataset/COVID-19_sentence.txt"
#input_file="./dataset/MIS-C_sentence.txt"
#input_file="./dataset/Endometriosis_sentence.txt"
#input_file ="./dataset/PubMed_sentence.txt"

words_list =[]

with open (input_file, 'rb') as f:
    for i,line in enumerate (f):
        #print(line)
        break

def read_input(input_file):

    logging.info("reading file {0}...this may take a while".format(input_file))

    #ps = PorterStemmer()
    stopword = stopwords.words('english')
    
    with open(input_file, 'rb') as f:
        for i, line in enumerate (f):
            line = str(line).lower()      
            
            #去除特殊符號  b' 
            line = str(line).replace("b'","")
            line = str(line).replace("b\ ","")
            line = str(line).replace("\r","")
            line = str(line).replace("\n","")
            line = str(line).replace('/',' ')
            line = str(line).replace('.',' ')
            line = str(line).replace('/e/',' ')
            line = str(line).replace('(d)',' ')
            line = str(line).replace('s)',' ')
            line = str(line).replace('?]',' ')
            line = str(line).replace('?]',' ')
            line = str(line).replace('=-B',' ')
            line = str(line).replace('-C',' ')
            line = str(line).replace("\xc2\xa0","")
            line = str(line).replace("\xc2\xb0c","")
            line = str(line).replace("\xc2\xb79","")
            line = str(line).replace("\xae","")
            line = str(line).replace("\xc3","")
            line = str(line).replace("\xb3","")
            
            #line0 = re.compile(r'[\n\r\t]')
            #line = line0.sub(" ", line)
            
            
            #line = str(line).encode('ascii', 'ignore')
            #line = unicodedata.normalize("NFKD",str(line))
            
            read_words1 = line.encode('utf-8').decode('utf-8')
            
            read_words1= re.sub(r'^\w\s+','',str(line).replace("\r\n", " "))
            read_words1 = re.sub(r'\s+', ' ',str(line))
            read_words1 = re.sub(r'^\w\s',' ',str(line))
            #result = re.split(r's+', read_words1)    
            #result = word_tokenize(read_words)
            
            #print(i)
            #print(line)
            
            result = word_tokenize(read_words1)
            #result = word_tokenize(line)
            words = 0
            
            
            for i in range(len(result)):            
                if len(result[i]) > 0 and result[i] != '-' and result[i] != '–' and result[i] != ',':
                    words += 1
                    
                    #確認是否為數字千分號
                    pos=result[i][:-1].find(',')
                    #print(pos)            
                    if int(pos) > 0 and result[i][pos-1:pos].isdigit() != True :
                        words += 1
                    #print(res[i])
                #去除特殊符號字元單一數字
                if result[i] in ['-','－','?','(',')','%','[',']','+','``','"','--','*','&','.','..','#','@','`','~','{','}','$','@','!']:
                    result[i] = ''
                #去除特殊符號字元
                result[i] = result[i].replace('~','')
                result[i] = result[i].replace(',','')
                result[i] = result[i].replace('!','')
                result[i] = result[i].replace('@','')
                result[i] = result[i].replace('#','')
                result[i] = result[i].replace('$','')
                result[i] = result[i].replace('%','')
                result[i] = result[i].replace('^','')
                result[i] = result[i].replace('&','')
                result[i] = result[i].replace('*','')
                result[i] = result[i].replace('(','')
                result[i] = result[i].replace(')','')
                result[i] = result[i].replace('!','')
                result[i] = result[i].replace(':','')
                result[i] = result[i].replace('+','')
                result[i] = result[i].replace('=','')
                result[i] = result[i].replace('=-','')
                result[i] = result[i].replace(',','')
                result[i] = result[i].replace("'",'')
                result[i] = result[i].replace("'s",'')
                result[i] = result[i].replace('\n','')
                result[i] = result[i].replace('\r','')
                
                result[i] = result[i].replace(' ','')
                
                result[i] = result[i].rstrip("\n")
                result[i] = result[i].rstrip("\r")
                
                result[i] = result[i].replace("\xc2\xa0","")
                result[i] = result[i].replace("\r","")
                result[i] = result[i].replace("\n","")
                result[i] = result[i].replace("\xc2\xb0c","")
                result[i] = result[i].replace("\xc2\xb79","")
                result[i] = result[i].replace("\xe2\x80\x9e","")
                
                
                
                
                if len(result[i]) > 50:
                    result[i] = ''
                    
                if len(result[i]) < 2:
                    #print(result[i])
                    result[i] = ''    
                
                #加入Porter's algorithm
                #result[i] = ps.stem(result[i])
                #print(result[i])
                
                #去除Stopwords
                stop_words = set(stopwords.words('english'))
                if result[i] in stop_words:
                    #print(result[i])
                    result[i] = ''
            

            
            line1 = ''
            for k in range(len(result)):
                if not result[k] in stopword and len(result[k]) > 1 and str(result[k]) != "\r\n":
                    line1 = line1 +' '+result[k]
                    if not result[k] in words_list:
                        words_list.append(result[k])
                        
            print(line1)
            if (i % 10000 == 0):
                logging.info ("Read {0} articles".format (i))
            # do some pre-processing and return a list of words for each review text
            
            #yield gensim.utils.simple_preprocess(line1,deacc=True)
            yield word_tokenize(line1)
            

# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list (read_input (input_file))
logging.info ("Done reading input file")

#model = gensim.models.Word2Vec (documents, sg=1, window=15, min_count=2, negative=5, workers=10)
model = gensim.models.Word2Vec (documents, sg=1, window=15, max_vocab_size=8000, min_count=2, workers=10)

model.train(documents,total_examples=len(documents),epochs=150)
#model.save("Endometriosis_word2vec-skipgram-trained.model")
#filename="./dataset/Endometriosis_works_list.txt"
#model.save("COVID-19_Endometriosis_word2vec-skipgram-trained.model")
#filename="./dataset/COVID-19_Endometriosis_works_list.txt"
model.save("COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model")
filename="./dataset/COVID-19_MIS-C_Endometriosis_works_list.txt"
#model.save("MIS-C_Endometriosis_word2vec-skipgram-trained.model")
#filename="./dataset/MIS-C_Endometriosis_works_list.txt"
#model.save("COVID-19_MIS-C_word2vec-skipgram-trained.model")
#filename="./dataset/COVID-19_MIS-C_works_list.txt"
#model.save("MIS-C_word2vec-skipgram-trained.model")
#filename="./dataset/MIS-C_works_list.txt"
#model.save("COVID-19_word2vec-skipgram-trained.model")
#filename="./dataset/COVID-19_works_list.txt"

#model.save("PubMed_word2vec-skipgram-trained.model")
#filename="./dataset/PubMed_works_list.txt"



fs=open(filename, "w",encoding="utf-8")

for i in range(len(words_list)):
    fs.write(str(words_list[i])+'\n')
    
