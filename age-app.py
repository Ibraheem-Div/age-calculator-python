from datetime import datetime
def Importdate():
    tody=datetime.now()
    d1=tody.day
    m1=tody.month
    y1=tody.year
    return d1,m1,y1
    
#print(d1,m1,y1)
#take the inputs

def take():
    d2=int(input("pleas enter day :"))
    m2=int(input("pleas enter month :"))
    y2=int(input("pleas enter year :"))
    return d2,m2,y2

#calc a age 
def age (d1, m1, y1, d2, m2, y2):
    today= datetime(y1,m1,d1)
    birth= datetime(y2,m2,d2)
    age_defrince= today-birth
    years= age_defrince.days // 365
    print (f"🎉 yor age is : {years}")

current_day,current_month,current_year=Importdate()
BirthDay,BirthMonth,BirthYear=take()
age(current_day,current_month,current_year,BirthDay,BirthMonth,BirthYear)