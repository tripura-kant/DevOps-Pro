# List example

'''
list_of_names = list()
list_of_envs = []

print(type(list_of_envs))
print(type(list_of_names))

'''


list_of_cloud_env = list(["aws","azure","gcp"])

list_of_env = ["dev","stage","prd"]
list_of_env.append("clients")
list_of_env.append("management")

#print(list_of_env[1])

for i in list_of_env:
	print("Deploying to : ")
	print(i)


