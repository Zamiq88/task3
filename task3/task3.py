#task1
height=float(input('enter your height'))
#bmi(body mass index)=weight/(height**2) #(18.5-25) ideal index

#weight=bmi*(height**2)
print('ideal ceki araliginiz {} ile {} arasidir'.format(18.5*(height**2),25*(height**2)))

#task 2    

basketvalue=0
basketlist=[]

for instance in range(0,2):
    product=input('enter product name')
    quantity=int(input('enter product quantity'))
    price=float(input('enter product price'))
    basket1=quantity*price*1.18
    basketvalue+=basket1
    list1={product:{'sayi':quantity , 'qiymeti' :price}}
    basketlist.append(list1)
print('sebetin terkibi:' ,basketlist, 
      'sebetin umumi deyeri(EDV daxil):', basketvalue)
   
if basketvalue>50 and basketvalue<100:
    print('10 azn kupon qazandiniz') 
elif basketvalue>=100:
    print('15 azn kupon qazandiniz')   

#task 3
distance=float(input('gedeceyiniz mesafe(km)'))
vehicle=input('neqliyyati secin (1)avtomobil,(2)yuk masini (3)avtobus')
if vehicle=='1':
    print('odeyeceyiniz mebleg:',0.5*distance,'dollar')  
elif vehicle=='2':
    print('odeyeceyiniz mebleg:',1*distance,'dollar')
else:
    print('odeyeceyiniz mebleg:',2*distance,'dollar')

    
    
