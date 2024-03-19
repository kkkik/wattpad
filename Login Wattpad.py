from requests import post
account = input("Enter Account Like username:abcd1234 : ") # account here
def LoginWattpad(account):
	user, password = account.strip().split(':')
	url='https://api.wattpad.com/v4/sessions'
	he={
	'Host': 'api.wattpad.com',
	'cache-control': 'no-cache',
	'accept-encoding': 'gzip',
	'content-type': 'application/x-www-form-urlencoded',
	'content-length': '556',
	'cookie': 'lang=16; wp_id=654334c4-8a6a-4549-82bf-2db1d0fed21d',
	'user-agent': 'Android App v6.48.4; Model: ANY-LX2; Android SDK: 33; Connection: WiFi; Locale: en_IQ_#u-nu-latn;',
	'accept-language': 'en_IQ_#u-nu-latn',
}
	da =(f'type=wattpad&username={user}&password={password}&fields=token%2Cga%2Cuser%28username%2Cdescription%2Cavatar%2Cname%2Cemail%2CgenderCode%2Clanguage%2Cbirthdate%2Cverified%2CisPrivate%2Cambassador%2Cis_staff%2Cfollower%2Cfollowing%2CbackgroundUrl%2CvotesReceived%2CnumFollowing%2CnumFollowers%2CcreateDate%2CfollowerRequest%2Cwebsite%2Cfacebook%2Ctwitter%2CfollowingRequest%2CnumStoriesPublished%2CnumLists%2Clocation%2CexternalId%2Cprograms%2CshowSocialNetwork%2Cverified_email%2Clanguage%2Cinbox%28unread%29%2Chas_password%2CconnectedServices%29')
	r=post(url,headers=he,data=da).text
	if """"message":"Login failed. Invalid user ID or password"}""" in r:
		print( "Login Failed : "+account)
	else:
		print(r)
LoginWattpad(account)