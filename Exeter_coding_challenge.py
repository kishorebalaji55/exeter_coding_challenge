import pandas as pd
import re
import time
start=time.time()
fre_dic = pd.read_csv('french_dictionary.csv', header=None)
eng_list = fre_dic[0].to_list()
fre_list = fre_dic[1].to_list()
#def intersection(lst1, lst2): 
#    lst3 = [value for value in lst1 if value in lst2] 
#    return lst3
#lst = intersection(words_list, eng_list)
dic = dict(zip(eng_list,fre_list))
with open('t8.shakespeare.txt', 'r') as file:
    data = file.read()
def multipleReplace(text, wordDict):
    """
    take a text and replace words that match the key in a dictionary
    with the associated value, return the changed text
    """
    check=[]
    frequency = []
    for key in wordDict:
        frequency.append([a.start() for a in re.finditer(key, text)])
        text = text.replace(key, wordDict[key])
#        check.append([a.start() for a in re.finditer(wordDict[key], text)])
    return text,frequency
str1,frequency = multipleReplace(data, dic)
freq = []
for i in range(len(frequency)):
    freq.append(len(frequency[i]))

text_file = open("test1.txt", "w")
text_file.write(" %s " % str1)
text_file.close()

Dict=[{'English Word':eng, 'French Word':fre, 'Frequency':fr} for eng,fre,fr in zip(eng_list,fre_list,freq)]
df = pd.DataFrame (Dict, columns = ['English Word','French Word','Frequency'])
df.to_csv("frequency.csv", index=None)
end = time.time()
t=end - start
print("Runtime is {}".format(t))
import os, psutil
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
