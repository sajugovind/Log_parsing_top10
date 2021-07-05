# Log Parsing

This function is to analyze the HTTP logs and provide the well formated the repors. We can filter the reports with respective arguments. The reports include below details:

1. Top 10 requested pages and the number of requests made for each.

2. Percentage of successful requests (anything in the 200s and 300s range).

3. Percentage of unsuccessful requests (anything that is not in the 200s or 300s range).

4. Top 10 unsuccessful page requests.

5. The top 10 hosts making the most requests, displaying the IP address and number of requests made.

6. For each of the top 10 hosts, show the top 5 pages requested and the number of requests for each

## Usage

Need to download the log file and pass the path on Collector.py

```
log_file = "access_log" . >> line number 6
```

### Example 1 - Help:
```
❯ python3 Collector.py --help
usage: exec [--top10] [--persuccess] [--perfail] [--top10fail] [--top10hosts] [-h]  [--all]

optional arguments:
  -h, --help    show this help message and exit
  --top10       1. Top 10 requested pages and requests for each
  --persuccess  2. Percentage of successful requests
  --perfail     3. Percentage of unsuccessful requests
  --top10fail   4. Top 10 unsuccessful page requests
  --top10hosts  5. The top 10 hosts making the most requests
  --all         6. The Complete reports
```

### Example 2 - Invlid Argument:
```
❯ python3 Collector.py --top20
usage: exec [--top10] [--persuccess] [--perfail] [--top10fail] [--top10hosts] [-h] [--all]
exec [--top10] [--persuccess] [--perfail] [--top10fail] [--top10hosts]: error: unrecognized arguments: --top20
```

### Example 3 - Top 10 Requested URL):
```
❯ python3 Collector.py --top10

----Top 10 requestsed URL----
URL : /administrator/index.php  number of requests : 150319
URL : /apache-log/access.log  number of requests : 52849
URL : /index.php?option=com_contact&view=contact&id=1  number of requests : 22212
URL : /  number of requests : 6920
URL : /index.php?option=com_easyblog&view=dashboard&layout=write  number of requests : 2740
URL : /templates/_system/css/general.css  number of requests : 1728
URL : /favicon.ico  number of requests : 1708
URL : /robots.txt  number of requests : 1309
URL : /media/system/js/mootools.js  number of requests : 489
URL : /templates/jp_hotel/css/template.css  number of requests : 457
```
### Example 4 - Success requests percentage:
```
❯ python3 Collector.py --persuccess

Percentage of successful requests: 95.59
```
### Example 5 - Unsuccess requests percentage:
```
❯ python3 Collector.py --perfail

Percentage of unsuccessful requests: 4.41

```
### Example 6 - Top 10 unsuccessfull requestsed URL:
```
❯ python3 Collector.py --top10fail

----Top 10 unsuccessfull requestsed URL----
URL : /index.php?option=com_easyblog&view=dashboard&layout=write  number of requests : 2740
URL : /templates/_system/css/general.css  number of requests : 1728
URL : /favicon.ico  number of requests : 1708
URL : /icons/blank.gif  number of requests : 152
URL : /icons/back.gif  number of requests : 150
URL : /icons/text.gif  number of requests : 150
URL : /wp-login.php  number of requests : 138
URL : /.env  number of requests : 63
URL : /xmlrpc.php?rsd  number of requests : 32
URL : /wordpress/wp-includes/wlwmanifest.xml  number of requests : 31
```
### Example 7 - The top 10 hosts making the most requests, and the top 5 requests they made:
```
❯ python3 Collector.py --top10hosts
----Top 10 hosts----
host : 193.106.31.130 , Number of requests :  139893
host : 197.52.128.37 , Number of requests :  40777
host : 173.255.176.5 , Number of requests :  5220
host : 178.44.47.170 , Number of requests :  2824
host : 51.210.183.78 , Number of requests :  2684
host : 193.9.114.182 , Number of requests :  2205
host : 45.15.143.155 , Number of requests :  1927
host : 45.144.0.179 , Number of requests :  946
host : 176.222.58.254 , Number of requests :  934
host : 45.132.207.154 , Number of requests :  890

----Top 5 requests-----
host : 193.106.31.130 , Top 5 URL and number of requests :  [('/administrator/index.php', 139893)]
host : 197.52.128.37 , Top 5 URL and number of requests :  [('/apache-log/access.log', 40745), ('/apache-log/', 28), ('/favicon.ico', 1), ('/icons/blank.gif', 1), ('/icons/back.gif', 1)]
host : 173.255.176.5 , Top 5 URL and number of requests :  [('/administrator/index.php', 964), ('/administrator/templates/system', 46), ('/administrator/templates/system/css', 43), ('/', 31), ('/apache-log/access.log', 19)]
host : 178.44.47.170 , Top 5 URL and number of requests :  [('/apache-log/access.log', 2780), ('/favicon.ico', 5), ('/templates/_system/css/general.css', 2), ('/apache-log/access.log?page=1&per=25', 1), ('/apache-log/access.log?page=1&per=1', 1)]
host : 51.210.183.78 , Top 5 URL and number of requests :  [('/apache-log/access.log', 2684)]
host : 193.9.114.182 , Top 5 URL and number of requests :  [('/administrator/index.php', 2204), ('/wp-login.php', 1)]
host : 45.15.143.155 , Top 5 URL and number of requests :  [('/administrator/index.php', 1927)]
host : 45.144.0.179 , Top 5 URL and number of requests :  [('/index.php?option=com_contact&view=contact&id=1', 946)]
host : 176.222.58.254 , Top 5 URL and number of requests :  [('/index.php?option=com_contact&view=contact&id=1', 934)]
host : 45.132.207.154 , Top 5 URL and number of requests :  [('/index.php?option=com_contact&view=contact&id=1', 890)]
```
### Example 8 - Complete Reports:

```
❯ python3 Collector.py --all
----Top 10 requestsed URL----
URL : /administrator/index.php  number of requests : 150319
URL : /apache-log/access.log  number of requests : 52849
URL : /index.php?option=com_contact&view=contact&id=1  number of requests : 22212
URL : /  number of requests : 6920
URL : /index.php?option=com_easyblog&view=dashboard&layout=write  number of requests : 2740
URL : /templates/_system/css/general.css  number of requests : 1728
URL : /favicon.ico  number of requests : 1708
URL : /robots.txt  number of requests : 1309
URL : /media/system/js/mootools.js  number of requests : 489
URL : /templates/jp_hotel/css/template.css  number of requests : 457

Percentage of successful requests: 95.59

Percentage of unsuccessful requests: 4.41

----Top 10 unsuccessfull requestsed URL----
URL : /index.php?option=com_easyblog&view=dashboard&layout=write  number of requests : 2740
URL : /templates/_system/css/general.css  number of requests : 1728
URL : /favicon.ico  number of requests : 1708
URL : /icons/blank.gif  number of requests : 152
URL : /icons/back.gif  number of requests : 150
URL : /icons/text.gif  number of requests : 150
URL : /wp-login.php  number of requests : 138
URL : /.env  number of requests : 63
URL : /xmlrpc.php?rsd  number of requests : 32
URL : /wordpress/wp-includes/wlwmanifest.xml  number of requests : 31

----Top 10 hosts----
host : 193.106.31.130 , Number of requests :  139893
host : 197.52.128.37 , Number of requests :  40777
host : 173.255.176.5 , Number of requests :  5220
host : 178.44.47.170 , Number of requests :  2824
host : 51.210.183.78 , Number of requests :  2684
host : 193.9.114.182 , Number of requests :  2205
host : 45.15.143.155 , Number of requests :  1927
host : 45.144.0.179 , Number of requests :  946
host : 176.222.58.254 , Number of requests :  934
host : 45.132.207.154 , Number of requests :  890

----Top 5 requests-----
host : 193.106.31.130 , Top 5 URL and number of requests :  [('/administrator/index.php', 139893)]
host : 197.52.128.37 , Top 5 URL and number of requests :  [('/apache-log/access.log', 40745), ('/apache-log/', 28), ('/favicon.ico', 1), ('/icons/blank.gif', 1), ('/icons/back.gif', 1)]
host : 173.255.176.5 , Top 5 URL and number of requests :  [('/administrator/index.php', 964), ('/administrator/templates/system', 46), ('/administrator/templates/system/css', 43), ('/', 31), ('/apache-log/access.log', 19)]
host : 178.44.47.170 , Top 5 URL and number of requests :  [('/apache-log/access.log', 2780), ('/favicon.ico', 5), ('/templates/_system/css/general.css', 2), ('/apache-log/access.log?page=1&per=25', 1), ('/apache-log/access.log?page=1&per=1', 1)]
host : 51.210.183.78 , Top 5 URL and number of requests :  [('/apache-log/access.log', 2684)]
host : 193.9.114.182 , Top 5 URL and number of requests :  [('/administrator/index.php', 2204), ('/wp-login.php', 1)]
host : 45.15.143.155 , Top 5 URL and number of requests :  [('/administrator/index.php', 1927)]
host : 45.144.0.179 , Top 5 URL and number of requests :  [('/index.php?option=com_contact&view=contact&id=1', 946)]
host : 176.222.58.254 , Top 5 URL and number of requests :  [('/index.php?option=com_contact&view=contact&id=1', 934)]
host : 45.132.207.154 , Top 5 URL and number of requests :  [('/index.php?option=com_contact&view=contact&id=1', 890)]
```

