

cloud_envs = ["aws", "azure", "gcp"]

#print(cloud_envs[0])

try:
	print(cloud_envs[13])
except :
	print("Exection handled")
finally:
	print("executed always")


