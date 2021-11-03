def swap(): 
    file = open('text.txt','r')
    a = file.read()
    file2 = open('text2.txt','r')
    b = file2.read()
    file3 = open('text2.txt','w')
    file3.write(a)
    file4 = open('text.txt','w')
    file4.write(b)
    
swap()