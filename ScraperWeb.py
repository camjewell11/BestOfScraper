import mechanize

URL = "https://wahr-fm.secondstreetapp.com/2022-Best-of-Huntsville/gallery/?group=412796"

br = mechanize.Browser()
resp = br.open(URL)
print (resp.info())  # headers
print (resp.read())  # content


