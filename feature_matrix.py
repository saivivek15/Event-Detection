
# coding: utf-8

# In[1]:

import sys,os,re
import json
from pprint import pprint


# In[2]:


parus_path = "/Users/vivek/Documents/UTD/Spring17/BigDataManagement/Project/ParusAtrocitiesCoding/ParusAtrocitiesCoding"
semafor_filter_path = "/Users/vivek/Documents/UTD/Spring17/BigDataManagement/Project/semafor_filter_files"


# In[3]:

parus_list = os.listdir(parus_path)# list of directories in path parus_path
k = parus_list[1]
k.split(".")
for i in range(1,len(parus_list)):
    if(".coding" in parus_list[i]):
        parus_list[i] += ("/" + parus_list[i].split(".")[0] + ".json")


# In[4]:

'''convert it into json by removing ,'''
def remove_com(string):
    return string[:-4] + string[-3:]

'''if we give a dict into this function it will give all the citations and their corresponding class into the class_list'''
def cite_one_dict(_data_):
    data_ = remove_com(_data_)
    data = json.loads(data_)
    #print (data["citation"])
    citation_list = data["citation"].split(",")
    victim_list = []
    #victim_list.append({"victimncassert":data["victimncassert"]})
    #victim_list.append({"victimnccontest":data["victimnccontest"]})
    if data["victimpoli"] != "":
        victim_list.append({"victimpoli::0":data["victimpoli"]})
    if data["victimethn"] != "":
        victim_list.append({"victimethn::1":data["victimethn"]})
    if data["victimreli"] != "":
        victim_list.append({"victimreli::2":data["victimreli"]})
    if data["victimsoci"] != "":
        victim_list.append({"victimsoci::3":data["victimsoci"]})
    if data["victimcomb"] != "":
        victim_list.append({"victimcomb::4":data["victimcomb"]})
    if data["victimrand"] != "":
        victim_list.append({"victimrand::5":data["victimrand"]})
    for cite in citation_list:
        class_list[cite.strip()] = victim_list

'''helper fuction to read the json file'''
def read_json(path):
    try:
        with open(path) as json_data:
            data = json_data.read()
            data_dicts = re.split("(}\n\n{)",data)
            for i in range(1,len(data_dicts),2):
                data_dicts[i-1] += " }"
                data_dicts[i+1] = "{" + data_dicts[i+1]
            for i in range(0,len(data_dicts),2):
                cite_one_dict(data_dicts[i])
    except:
        pass


# In[5]:


class_list = {} # this the dict of Key:citaion, Value:list of dicts(key:victim type ,value: its value)


for diry in parus_list:
    path = parus_path +"/"+ diry
    try:
        files_list = os.listdir(path)
        files_list.remove(".DS_Store")
        for file_ in files_list:
            read_json(path + "/" + file_)
    except:
        pass      


# In[7]:

import ast
semafor_filter_list = os.listdir(semafor_filter_path) # list of semafore filer files
semafor_filter_list.remove(".DS_Store")
for fil in semafor_filter_list:
    with open("semafor_filter_files/"+fil) as f:
        content = f.read()
        content = ast.literal_eval(content)
        text = ""
        for i in range(len(content)):
            for j in range(len(content[i])):
                text  += content[i]['Victim'][j] + " "
        #print text
        try:
            label = class_list[fil[:-4]]
            if len(label) ==1:
                #print fil,"::",line
                line=str(fil[:-4]+"::"+text+"::"+label[0].keys()[0]+"::"+label[0].values()[0])
                #print line
                with open('training_data.txt','a') as g:
                #print line
                    g.write(line + "\n")
                #print line
        except:
            print fil, " file label not exists"     



