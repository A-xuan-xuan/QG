import json


data = [{"name":"张大师","age":"18"},{"name":"张位","age":"28"},{"name":"刘德华","age":"39"}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

xuan = '[{"name":"张大师","age":"18"},{"name":"张位","age":"28"},{"name":"刘德华","age":"39"}]'
l = json.loads(xuan)
print(type(l))
print(l)
















