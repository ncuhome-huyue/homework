import urllib.parse
import urllib.request
import re


url = "http://news.ncu.edu.cn/"
proxy_support = urllib.request.ProxyHandler({'http':'199.127.101.139'})
opener = urllib.request.build_opener(proxy_support)
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8').replace(u'\u200b','').replace(u'\xa0','')
f=open("record.txt",'w')
f.write(html)
f.close()
fread = open("record.txt",'r')
fwrite = open("record1.txt",'w')
i = 0
st = ""
for st in fread.readlines(): 
    if i == 0:
        if st.find(r'<ul') != -1:
            i = 1
    if i == 1:
        if st.find(r"</ul>") != -1:
            i = 0
        else:
            py_re = r'<li .+?><a .+?>(.+?)</a>'
            t = re.compile(py_re)
            st1 = t.findall(st)
            if st1:
                st2 = st1.pop()
                fwrite.write(st2 + "\n")
fwrite.close()
fread.close()
print("end")
