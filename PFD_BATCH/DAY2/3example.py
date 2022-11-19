
path = {
        "MinTls": "TLSv1.2_2021",
        "Domain": "d2l97ukcvyhls8.cloudfront.net",
        "DistributionId": "E1FMBG96NXS044",
        "Aliases": [
            "adserver-uat.adtech.wynk.in",
            "events-uat.adtech.wynk.in"
        ]
    }


env_details = [path]

#print(env_details)

for item in env_details:
	for key,value in item.items():
		if key == "active"