import random
f=open('text.txt')
n=f.read()
print(n)
f.close()
sh=[]
alf=[]
key=[]
pr=[]
slov=[]
alf.append(' ')
а=ord('а')
for i in range(а,а+32):
	alf.append(chr(i))
#print(alf)

while len(key)!=len(alf):
	i=random.randint(1,35)
	if i not in key:
		key.append(i)
	else: 	
		continue
for i in range(len(alf)):			
	print(alf[i],'=',key[i],end='\n')
	k=str(alf[i])+'='+str(key[i])
	sh.append(k)
z=open('key.txt','w')
z.write(str(sh))
z.close()
#print(sh)
for i in range(len(n)):	
	pr.append(alf.index(n[i]))
#print(pr)

for j in range(len(pr)):
	s=key[pr[j]]
	slov.append(s)
print(slov)
k=open('otvet.txt','w')
k.write(str(slov))
k.close()
#///////////////////////////////////////////////////////////////////////
ob=[]
obr=[]
for i in range(len(slov)):	
	ob.append(key.index(slov[i]))
#print(ob)
for j in range(len(ob)):
	q=alf[ob[j]]
	obr.append(q)
print(obr)
