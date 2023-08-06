dic = {"fdsajkl;":"in-out",
      "jkl;fdsa":"in-out",
      "asdf;lkj":"out-in",
      ";lkjasdf":"out-in",
      "asdfjkl;":"stairs",
      ";lkjfdsa":"reverse"}

s = input()
if s not in dic.keys():
    print("molu")
else:
    print(dic[s])
