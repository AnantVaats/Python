#reading csv files
import csv
lisst=[]
try:
    with open("./movie.csv",'r') as file:
        reader=csv.reader(file)
        for row in reader:
            lisst.append(row)
            print(row[0],"-",row[1],"-",row[2])
    print("data printed")
except FileNotFoundError:
    print("OOps!")

#writing csv files
try:
    with open("./name.csv",'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(lisst)
    print("Hooray!")
except Exception as e:
    print("Oops!")