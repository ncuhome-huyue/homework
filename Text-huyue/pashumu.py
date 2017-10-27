import urllib.request
import requests
import re

a=input("你想爬到的书")
url="http://opac.ncu.edu.cn/opac/search_adv_result.php?sType0=any&q0=" + urllib.request.quote(a)+"&with_ebook=on"
headers = {'content-type': 'application/json'}
r = requests.get(url)
f=open("record.txt",'w')
f.write(r.text)
f.close()
fread = open("record.txt",'r')
fwrite = open("record1.txt",'w')
i = 0
st = ""
for st in fread.readlines(): 
    if i == 0:
        if st.find(r'<tr>') != -1:
            i = 1
    if i == 1:
        if st.find(r"</tr>") != -1:
            i = 0
        else:
            py_re = r'.*?<TD  bgcolor="#FFFFFF">(.*?)</TD>'
            t = re.compile(py_re)
            st1 = t.findall(st)
            if st1:
                st2 = st1.pop()
                fwrite.write(st2 + "\n")
fwrite.close()
fread.close()
print("end")
