import urllib2
from bs4 import BeautifulSoup

# Create/open a csv file called wunder.txt
f = open('wunder.txt', 'w')

# Iterate through months and days
for m in range (1, 13):
    for d in range (1, 32):

        # Check if already gone through month
        if (m == 2 and d > 28):
            break
        elif (m in [4, 6, 9, 11] and d > 30):
            break

        # Open wunderground url
        timestamp = '2009' + str(m) + str(d)
        print "Getting data for " + timestamp
        url = "http://www.wunderground.com/history/airport/KBUF/2009/" + str(m) +"/"+ str(d) + "/DailyHistory.html"
        page = urllib2.urlopen(url)

        # Get temperature from page
        soup = BeautifulSoup(page, "html.parser")
        # dayTemp = soup.body.wx-value.string
        dayTemp = soup.findAll(attrs={"class":"wx-value"})[2].string

        # Format month for timestamp
        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)

        # Format day for timestamp
        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)

        # Build timestamp
        timestamp = '2009' + mStamp + dStamp

        # Write timestamp and temperature to file
        f.write(timestamp + ',' + dayTemp + '\n')

# close file
f.close()
