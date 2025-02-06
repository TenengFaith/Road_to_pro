number=23092
char=str(number)
for i in char:
    if i=="-":
        char.pop(i)
        new=char[::-1]
        char2=new.append('-',0)
    else:
        char2=char[::-1]
num=int(char2)
if num>=-2**31 and num<=(2**31)-1:
    print(f"{num}")
else:
    print("0")