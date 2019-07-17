# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

# # Read in a page

html = scraperwiki.scrape("https://beta.companieshouse.gov.uk/company/04503188")

# Turn html into a string and put in variable root
root = lxml.html.fromstring(html)

# # Find something on the page using css selectors
name = root.cssselect('title')

for company in name:
#   print lxml.html.tostring(title)
  print company.text
  
#Find all the descriptive lists on the page using css selector
lists = root.cssselect('dl')

 # Find a second thing on the page using css selectors
companyinfotypes = root.cssselect('dt')

for infotypenames in companyinfotypes:
  print infotypenames.text
  record = { "infotypenames" : infotypenames.text } # column name and value
  scraperwiki.sqlite.save(["infotypenames"], record) # save the records one by one
  
# Find a third thing on the page using css selectors
actualinfo = root.cssselect('dd')

for companyinfo in actualinfo:
  print companyinfo.text
  record = { "companyinfo" : companyinfo.text } # column name and value
  scraperwiki.sqlite.save(["companyinfo"], record) # save the records one by one


# # # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
# #
# # # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")


# # You don't have to do things with the ScraperWiki and lxml libraries.
# # You can use whatever libraries you want: https://morph.io/documentation/python
# # All that matters is that your final data is written to an SQLite database
# # called "data.sqlite" in the current working directory which has at least a table
# # called "data".
