#!/usr/bin/env python3.6

data = {'Sunny':25,'Paresh':23,'Rahul':24}
unorderdata = {'Cities':['Mumbai','Delhi','Kolkata'],'Pincodes':[22,33,44]}
print("Unorderdata is \n{}".format(unorderdata))
print(unorderdata['Cities'][2])
print("Data is \n" + str(data))
print(data['Sunny'])
for name,roll in data.items():
#	print("{} has roll number {}".format(name,roll))
	print(name + " has roll number " + str(roll))

print("Keys are "  + str(data.keys()))
print("Values are " + str(data.values()))
print("Items are " + str(data.items()))
data['Nikhil']=25
print("Added new valuse " +str(data))


detail = {'items':[{
   "kind": "youtube#channel",
   "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/m0PScsi7j8BO4gCia4fN0zG3RjI\"",
   "id": "UC6KKh6eK3DIBMznzBiA4XOw"}]}
print(detail['items'][0]['id'])
