#####################Author#############
#####################Tapan Mahata#################
import urllib
import re
import pymysql
url = "http://amazon.in/Delonghi-KG40-Electric-Coffee-Grinder/dp/B003TX2K3K/ref=pd_rhf_ee_s_cp_3_PY1Y?ie=UTF8&refRID=1Q36TBTW6JH3NG4ZFGY9"
regex = re.compile('<span id="productTitle" class="a-size-large">(.+?)</span>')
regex1 = re.compile('<span id="acrCustomerReviewText" class="a-size-base">(.+?)</span>')
regex2 = re.compile('<span class="a-size-base a-text-bold">(.+?)</span>')


m = urllib.urlopen(url)
htmltext = m.read()
pname = regex.findall(str(htmltext))
noreview = regex1.findall(str(htmltext))
title = regex2.findall(str(htmltext))

print ("the product name is",pname)

print ("the No of reviewer is",noreview)

print ("the review is",title)



db = pymysql.connect( host = 'localhost',user = 'root',passwd = 'root', db='tapan')
cursor = db.cursor()
sql = "insert into tapan.`amaz`(pname,noreview) values (%s,%s)"
cursor.execute( sql, (pname,noreview))
cursor.close()
db.commit()   #Makes sure the DB saves your changes!
db.close()