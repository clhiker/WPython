def main():
   d = {}
   d["lihui"] = "zhizhang"
   print(d)
   d.update({"lihui":222,"zhizhong":2})
   print(d)
   print(222 in d)
   d.update({"hhda":4})
   print(d)
   print("lihui" in d)
   print(list(d.values()))
   print(list(d.keys()))
   print(list(d.items()))
   print(tuple(d))
   print(set(d))
   for key in d:
      print(key,d[key])
   del(d["hhda"])
   print(d)

   list1 = [["one",1],["two",2],["three",3]]
   list2 = [("first",1),("second",2),("third",3)]
   dd = dict(list1)
   print(dd)
   dd.update(dict(list2))
   print(dd)

main()
   
