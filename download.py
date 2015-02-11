import os

baseurl = "http://www.geocities.jp/timeway/"
for i in range(134):
    doc = "kougi-"+str(i+1)+".html"
    if i < 9:
        odoc = "kougi-00"+str(i+1)+".html"
    elif i < 99:
        odoc = "kougi-0"+str(i+1)+".html"
    else:
        odoc = "kougi-"+str(i+1)+".html"
    url = baseurl + doc
    command = "wget "+url+" -O "+odoc
    os.system(command)

