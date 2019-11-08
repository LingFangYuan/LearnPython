import json
str1 = [{"username": "七夜", "age": 24}, (2, 3), 1]
json_str = json.dumps(str1, ensure_ascii=False)
print(json_str)
with open('qiye.txt', 'w', encoding='utf-8') as fp:
    json.dump(str1, fp=fp, ensure_ascii=False)

new_str = json.loads(json_str)
print(new_str, type(new_str))
with open('qiye.txt', 'r', encoding='utf-8') as fp:
    new_str1 = json.load(fp)
    print(new_str1, type(new_str1))
