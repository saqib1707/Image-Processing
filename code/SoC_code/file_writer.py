file = open('txtlists/files7.txt','w')

for i in range(0, 241):
    if i%10 == 0:
        file.write('../images/img0'+str(i)+'.jpg'+'\n')
file.close()
        
