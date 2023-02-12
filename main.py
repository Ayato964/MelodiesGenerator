from convertXMLToVector import xmlLoader

c = xmlLoader("data/")
x_all, y_all = c.convert("C", "major")

print(x_all.shape[1])
