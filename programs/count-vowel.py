import string
s='Hello, have you tried our tutorial-section yet?'
s=s.lower()
s=s.replace(' ','')
s=s.translate(str.maketrans('','',string.punctuation))
d={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in s:
    if i in d:
        d[i]+=1
print(d)