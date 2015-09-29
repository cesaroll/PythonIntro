from xml.dom.minidom import Document

doc = Document()

films = doc.createElement("films")
doc.appendChild(films)

afilm = doc.createElement("film")
films.appendChild(afilm)

#Title
title = doc.createElement("title")
afilm.appendChild(title)

text = doc.createTextNode("Annie Hall")
title.appendChild(text)

#Director
director = doc.createElement("director")
afilm.appendChild(director)
text = doc.createTextNode("Woody Allen")
director.appendChild(text)

# Year
year = doc.createElement("year")
afilm.appendChild(year)
text = doc.createTextNode("1977")
year.appendChild(text)

filename = "films.xml"
f = open(filename, "w")
f.write(doc.toprettyxml(indent="    "))
f.close()
