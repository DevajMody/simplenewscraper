def prepareDoc(contents):
 contentFile = open("content.txt","w")
 metaFile = open("meta.txt","w")

 for k,v in contents.items():
     text = v["text"]
     meta = str(v["title"]) + "-\nAuthors - " + str(v["authors"]) + "\nPublish Date - " + str(v["publishdate"]) + "\nLink - " + str(v["link"])  + "\n\n"
     contentFile.write(text)
     metaFile.write(meta)
 contentFile.close()
 metaFile.close()

 return "done"