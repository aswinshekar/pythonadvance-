import json
f=open("data.json","r")
content=json.load(f)
print(content)
print(content[0])
f.close()


