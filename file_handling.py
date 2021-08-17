o = open('strings.txt', 'a+') 
str = [] 
count = 0
with open('vd.txt', 'r') as f:
    line = f.readline()
    print("line", line)
    str.append(f"'{line.strip()}'")
    line = f.readline()
    while line:
        
        str.append(" | ")
        s = f"'{line.strip()}'"
        str.append(s)
        line = f.readline()
        


print(str)       
sent = ''.join(str)
print(''.join(str)) 

sent = 'Vd ->' + sent
o.write(sent)
o.write("\n\n")
f.close()