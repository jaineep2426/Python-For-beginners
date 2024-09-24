a={
    "Patel" : 12,
    "Jainee" : 13
}
# print(a.items())
# print(a.values()) # right portions
# print(a.keys()) # left portions
a.update({"Patel" : 15})
print(a)

print(a.get("Jainee"))
print(a.get("Rudra"))
print(a["Rudra"])