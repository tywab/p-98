def swapFile(file1,file2):
    with open (file1,'r')as f1:
       data_a= f1.read()
    with open (file2,'r')as f2:
        data_b= f2.read()
    f1.close()
    f2.close()
    with open (file1,'w')as f1:
       f1.write(data_b)
    f1.close()
    with open (file2,'w')as f2:
        f2.write(data_a)
    f2.close()

swapFile('text1.txt','text2.txt')