import json
content=[{"Title":"Book1","Author":"John","Price":200},{"Title":"Book2","Author":"Sam","Price":300}]
f1=open("book.json","w")
json.dump(content,f1)
f1.close()