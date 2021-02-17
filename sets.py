myset={"apple","banana","kiwi"}
for x in myset:
    print(x)

#to add an item in set-use add() method
myset.add("orange")
print(myset)

#update()-to add two sets

myset={"apple","banana","kiwi"}
set2={"carrot","beetroot","papaya"}
myset.update(set2)
print(myset)

#remove set items
#remove()
#discard()
#pop()-removes any of the item since the set is unordered
#clear()-empties the set
#del keyword delete the set completely
myset.remove("apple")
print(myset)

#joining two sets

#union()
#update()
set1={"apple","banana","kiwi"}
set2={"carrot","beetroot","papaya"}
set3=set1.union(set2)
print(set3)

#intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)