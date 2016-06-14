'''
    TNHH: That New Hip Hop
    Author: Brandon Jones
    Purpose: Scrape websites for new music information.
            -Song Title
            -Artist
            -Anything else
    Date: June 13 2016
'''

import urllib2

#Read Hot New Hip Hop Top 100 page into an html file. Read into string
#http://programminghistorian.org/lessons/working-with-web-pages
hnhh_url = 'http://www.hotnewhiphop.com/top100/'
response = urllib2.urlopen(hnhh_url)
hnhhContent = response.read().split('\n')

line_cnt = 1
for i in hnhhContent:
    if 'HotNewHipHop - Hip Hop\'s Digital Giant' in i:
        break
    if 'alt="' in i:
        temp_string = i[i.index('alt="') + 5:]
        print str(line_cnt) + ':\t' + temp_string.split('"')[0]
        line_cnt += 1
