'''
Author: Pranav Khiste

Task:  Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

Example:
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

'''

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

#OR

'''
def domain_name(url):
    full_url=url.split("/")
    if len(full_url) == 1:
        domain=full_url[0].split(".")[1]
    else:
        domain=full_url[2].split(".")[0]
    return domain
'''