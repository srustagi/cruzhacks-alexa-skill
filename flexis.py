import config
import requests
import re

def scrape_flexis():
	url = "https://sho-prod.ucsc.edu/shs/common/login/stu_login.cfm"
	data = {"screenwidth": "0", "screenheight": "0", "LoginAction": "email", "username": config.username, "password": config.password, "login": "Log In"}
	r = requests.post(url = url, data = data).text
	flexis = re.search(r'[$]([^\s]+)', r).group(0)
	return flexis
