from bs4 import BeautifulSoup
with open('SourceFile.xml', 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'xml')
names = soup.find_all('SW-INSTANCE' and 'SW-VALUES-PHYS')
lst = []

for name in names:
    lst.append(name.text)
    with open('DestinationFile.xml', 'r') as f:
        file1 = f.read()
        soup1 = BeautifulSoup(file1, 'xml')
        names1 = soup1.find_all('SW-INSTANCE' and 'SW-VALUES-PHYS')
        lst1 = []

for name in names1:
   lst1.append(name.text)
   flst = []
for i in lst:
    if i not in lst1:
        flst.append(i)
        print(flst)