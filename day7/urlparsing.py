from urlparse import *

url1 = urljoin("http://www.wustl.edu", "bob/test.html")
url2 = urljoin("http://www.wustl.edu", "/")
url3 = urljoin("http://www.wustl.edu", "http://www.cnn.com")
url4 = urljoin("http://www.wustl.edu", "http://www.cnn.com/test.html")

for url in [url1, url2, url3, url4]:
  p = urlparse(url)
  print "{0}://{1}{2}: {3}".format(p.scheme, p.hostname, p.path, "is wustl" if (p.hostname == "www.wustl.edu") else "is not wustl")
