from functions import *

area = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
       '22','23','24','25','26','27']

y = raw_input("Enter year: ")
p = raw_input("Enter percent: ")

for x in area:
    print "region id="+str(x)
    df = read_and_filter(str(x))
   
    print("Max VHI in " + str(y) + " is " + str(max_VHI(df, y)))
    print("Min VHI in " + str(y) + " is " + str(min_VHI(df, y)))
    print extreme_drought_area(df, p)
    print moderate_drought_area(df, p)
