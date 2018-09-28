##>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
##>>> r.status_code
##200
##>>> r.headers['content-type']
##'application/json; charset=utf8'
##>>> r.encoding
##'utf-8'
##>>> r.text
##u'{"type":"User"...'
##>>> r.json()
##{u'private_gists': 419, u'total_private_repos': 77, ...}
##
print("hh")
import requests
r = requests.get("http://www.baidu.com")
r_s_code = r.status_code
r_headers = r.headers 
r_text = r.text
r_encoding = r.encoding
r_a_en = r.apparent_encoding
r_content = r.content

print(r_s_code)
print(type(r))
print(r_headers)
print(r_text)
print(r_encoding)
print(r_a_en)
print(r_content)


r.encoding = 'utf-8'
r_text = r.text
print(r_text)
