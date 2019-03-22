import os

templateData = None
newData = None
with open("depiction/ad.html","rb") as f:
	templateData = f.read()

with open("Packages","rb") as f:
	data = f.read()
	debInfo = data.split("\n\n")
	newPackagesInfo = []
	for x in debInfo:
		if len(x) < 100:
			continue
		info = x.split("\n")
		name = info[0][9:]
		version = info[1][9:]
		description = info[11][13:]
		# print description
		filename = "depiction/" + name+"_"+version+".html"
		with open(filename,"wb") as f1:
			f1.write(templateData.replace("[[ Description ]]",description))

		depiction = "\nDepiction: https://zlxdike.github.io/repo/" +  filename
		x = x + depiction
		newPackagesInfo.append(x)

	newData = '\n\n'.join(newPackagesInfo) + "\n\n"
with open("Packages","wb") as f:
	f.write(newData)


	