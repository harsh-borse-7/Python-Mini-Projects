'''
There are 14 floors in the building 
and 2 Elvators for that ... the program will call the nearer elevator as per floor among those
if elevator at same level first elevator will come
''' 

Design=[
    [' ',' L1',' ', ' L2'],
    [14,' ',' ',' '],
    [13,' ',' ',' '],
    [12,' *',' ',' '],
    [11,' ',' ',' '],
    [10,' ',' ',' '],
    [9,' ',' ',' '],
    [8,' ',' ',' '],
    [7,' ',' ',' '],
    [6,' ',' ',' *'],
    [5,' ',' ',' '],
    [4,' ',' ',' '],
    [3,' ',' ',' '],
    [2,' ',' ',' '],
    [1,' ',' ',' '],
    [0,' ',' ',' '],   
]
for i in Design:
    for j in i:
        print(j,end = " ")
    print()

while(True):
    floor_no=int(input("Enter floor number: "))

    for i in range(16):
        
        if (Design[i][1]==' *'):
            L1=15-i
        if (Design[i][3]==' *'):
            L2=15-i

    if(abs(L1-floor_no) <= abs(L2-floor_no)):
        
        Design[15-L1][1]=' '
        Design[15-floor_no][1]=' *'
        L1=15-floor_no


    elif(abs(L1-floor_no) > abs(L2-floor_no)):

        Design[15-L2][3]=' '
        Design[15-floor_no][3]=' *'
        L2=15-floor_no



    for i in Design:
        for j in i:
            print(j,end = " ")
        print()