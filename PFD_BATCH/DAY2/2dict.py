dict_of_items_1= {
	"env":"dev",
	"server":"amazon linux2",
	"ram":"2086",
	"active":True
}

dict_of_items_2= {
	"env":"prod",
	"server":"amazon linux2",
	"ram":"2086",
	"active":False
}

env_details = [dict_of_items_1,dict_of_items_2]

#for env in env_details:
#	for key,value in env.items():
#		if key=="active" and value==True:
#			print(env.values)

#print(env_details)


#for env in env_details:
	#print(env)

for env in env_details:
	for key,value in env.items():
		#print(key,value)
		if key == "active" and value==True :
			print(env)




#print(dict_of_items.get("env"))
#print(dict_of_items.get("active"))

#
#if dict_of_items['active']:
#	print('Server details')
#	print("Environment: ", dict_of_items["env"])
#*/