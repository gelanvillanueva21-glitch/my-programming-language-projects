from collections import defaultdict

hashMap = defaultdict(list)

arrList = ["Japan", "Philippines", "China", "Korea", "Taiwan"]
hashMap["Asia"].append(arrList)

for item, city in hashMap.items():
    for i in city:
        print(i)
    print(city)

print(hashMap.values())
print(hashMap)