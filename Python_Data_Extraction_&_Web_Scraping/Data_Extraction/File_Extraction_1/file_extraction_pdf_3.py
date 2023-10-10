import tabula  #need to install java

tables = tabula.read_pdf("test.pdf", pages="all")
# print(type(tables[0]))
df = tables[0]
print(df)