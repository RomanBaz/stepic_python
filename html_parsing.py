from urllib.request import urlopen
import re
import collections


html = urlopen(" https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
regex = '<code>(.*?)</code>'

l = sorted(re.findall(regex, html))


print(collections.Counter(l).most_common())
