# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


def get_xml_file_info(Query_dir,file,keyword):
    
    filepath = Query_dir +'/'+ file
    
    #print(filepath)
    
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    #print(root.tag)
    #print(root.attrib)
    
    tempfile = './'+str(file)+'.txt'
    #print(tempfile)
    f = open(tempfile,'w',encoding="utf-8")
    '''
    for Title in root.iter('Title'):
        if len(Title.text) > 90 and str(Title.text) != 'REFERENCES':
            f.write(Title.text +'\n')
    ''' 
    '''
    for ArticleTitle in root.iter('ArticleTitle'):
        #if len(ArticleTitle.text) > 90:
        f.write(ArticleTitle.text +'\n')
    '''
    for AbstractText in root.iter('AbstractText'):
        f.write(AbstractText.text+'\n')
        
    f.close

   


if __name__ == '__main__':
    Query_dir='./test_file'
    file = 'test3.xml'
    keyword = 'system'
    get_xml_file_info(Query_dir,file,keyword)
    