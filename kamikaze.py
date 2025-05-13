products = ["beans", "rice", "bread", "pork"]

chosen = [item[0:2] for item in products]

print(chosen)

things = {"name":"fowl", "gender":"female", "type": "domestic" }

deals = {kv for (kv) in things}

print (deals) 

keys = ["a", "b", "c", "d", "e"]
values = [1,2,3,4,5]

as_tuple = [(k,v) for k,v in zip(keys,values)]
print (as_tuple)

as_dict = {k:v for (k,v) in zip(keys,values)}
print (as_dict)

anoda = dict(zip(keys,values))
print (anoda)