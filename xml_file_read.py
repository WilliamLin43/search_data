# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


def get_xml_file_info(Query_dir,file,keyword):
    
    filepath = Query_dir +'/'+ file
    
    print(filepath)
    
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    #print(root.tag)
    #print(root.attrib)    
    tempfile = './'+str(file)+'.txt'
    print(tempfile)
    f = open(tempfile,'w',encoding="utf-8")
    
    for AbstractText in root.iter('AbstractText'):
        #print(AbstractText.attrib)
        #print(AbstractText.text)
        f.write(AbstractText.text)
        
    f.close

   


if __name__ == '__main__':
    file = './test1.xml'
    keyword = 'test'
    get_xml_file_info(file,keyword)
    