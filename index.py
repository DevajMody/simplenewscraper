import getLinks
import getContent
import prepareDoc

keyword = input("Enter keyword to be searched - ")
links = getLinks.start(keyword)
ctr = 1
contents = {}

for link in links:
 content = getContent.getContent(link)
 if content != "error":
  contents[ctr] = content
  ctr = ctr + 1

status = prepareDoc.prepareDoc(contents)

if status == "done":
    print("File saved")