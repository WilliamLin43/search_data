# -*- coding: utf-8 -*-
import json

def get_json_file_info(Query_dir,file,keyword):
    
    filepath = Query_dir +'/'+ file
    print(filepath)

    f1 = open(filepath,'r',encoding="utf-8")
    
    tempfile = './'+str(file)+'.txt'
    print(tempfile)
    f = open(tempfile,'w',encoding="utf-8") 
 
    data = json.load(f1)
    #print(len(data))
    for i in range(len(data)):
        print(data[i]["tweet_text"])
        f.write(data[i]['tweet_text'])
        
    f1.close           
    f.close



if __name__ == '__main__':
    Query_dir='./test_file'
    file = 'test4.json'
    keyword = 'system'
    get_json_file_info(Query_dir,file,keyword)
    