print("------------------------------------------")

print("File Handling in Pyhton")

print("------------------------------------------")

#read a file
f1=open("Vineet.py","r")
print(f1.read())

print("------------------------------------------")

#to read 10 charcter
f1=open("Vineet.py","r")
print(f1.read(10))

print("------------------------------------------")

#toreadaline
f1=open("Vineet.py","r")
#tor read first file
print(f1.readline())

#to read second line
print(f1.readline())

print("------------------------------------------")

#to access file by for content
f2=open("Vineet.py","r")
ctr=0
for str in f2:
    print(str)
    ctr=ctr+1
print(ctr)

print("------------------------------------------")

#tor read file  in list
f2=open("Vineet.py","r")
line=f2.readlines()
#to print line wise
print(line[0])

print("------------------------------------------")

print(line[1])

print("------------------------------------------")

print("Write A File")

print("------------------------------------------")

#writeafile
f1=open("Vineet.py","a")
f1.write("\nMy name is Vineet. \n I AM FROM MAITHON")
f1.close()

print("------------------------------------------")

#mod File
f1=open("Vineet.py","w")
f1.write("\nMy name is Vineet. \n I AM FROM MAITHON")
f1.close()


print("------------------------------------------")

#x mod
f1=open("Vineet.py","w")
f1.write("\nMy name is Anshu. \n I AM FROM racnhi")
f1.close()

#gives error as file exist
#after Changing the line

print("------------------------------------------")

print("SEEK() AND TELL()")

print("------------------------------------------")

#SEEK - TO CHANGE CURRENT POSITION
f5=open("Vineet.py","r")
f5.seek(10)
print(f5.read(10))

print("------------------------------------------")

#TELL - TO TELL CURRENT POSITION
f6=open("Vineet.py","r")
print(f6.read(10))
print(f6.tell())

print("------------------------------------------")

#delete File
import os
os.remove("Vineet.py")