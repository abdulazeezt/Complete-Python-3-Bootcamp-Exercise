import os
os.getcwd()

f = open("testfile1.txt",'w+')
f2 = open("testfile2.txt",'w+')

f.write("A new text has been added to the file1")
f2.write("A New text has been added to the file2 \n asdfasdfasdfasdfjasdf asdf;lasdkjfasd flasdjfas  \n ")

f.close()
f2.close()

import zipfile

zipobject = zipfile.ZipFile('comp_file.zip','w')

zipobject.write( "testfile1.txt" , compress_type=zipfile.ZIP_DEFLATED )
zipobject.write( "testfile2.txt" , compress_type=zipfile.ZIP_DEFLATED )
zipobject.close()

zipobject = zipfile.ZipFile('comp_file.zip','r')
zipobject.extractall("extracted_content")
zipobject.close()

