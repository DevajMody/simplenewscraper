import getLinks
import getContent
import prepareDoc

def controller(keyword, numberOfLinks):
  #keyword = input("Enter keyword to be searched - ")
  links = getLinks.start(keyword, numberOfLinks)
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

  return "done"

