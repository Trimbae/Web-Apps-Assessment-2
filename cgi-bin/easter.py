#!/usr/bin/python3
import cgi, cgitb
import string
form = cgi.FieldStorage()


year = form.getvalue('Year', 'a')

def parseInput(text):
	text = text.replace(" ", "")
	text_no_punc = ""
	for ch in text:
		if not (ch in string.punctuation):
			text_no_punc = text_no_punc + ch
	if text_no_punc.isdigit() == True:
		return text_no_punc
	else:
		return -1


#year = '   20 10'
year = parseInput(year)

DisplayMethod = form.getvalue('Display')
#DisplayMethod = 'words'


def Easter(y):
	a = y % 19
	b = y // 100
	c = y % 100
	d = b // 4
	e = b % 4

	g = (8 * b + 13) // 25
	h = (19 * a + b - d - g + 15) % 30
	j = c // 4
	k = c % 4
	m = (a + 11 * h) // 319
	r = (2 * e + 2 * j - k - h + m + 32) % 7

	n = (h - m + r + 90) // 25
	p = (h - m + r + n + 19) % 32

	return [p, n]

date = Easter(int(year))

day = date[0]
month = date[1]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
namedMonth = months[month - 1]

def getSuffix(d):
	if d % 10 == 1 and d != 11:
		return '<sup>st</sup>'
	elif d % 10 == 2 and d != 12:
		return '<sup>nd</sup>'
	elif d % 10 == 3 and d != 13:
		return '<sup>rd</sup>'
	else:
		return '<sup>th</sup>'

suffix = getSuffix(day)

print("Content-Type: text/html; charset=utf-8")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<head> <title> Python Script for feedback </title>")
print("<link rel='stylesheet' type='text/css' href='../EasterSS.css'/></head>")
print("<body>")
if year == -1:
	print('<p class="subheading">Invalid Input</p>')
	print('<p class="date">Please try again :)</p')
else:
	print("<p class = 'subheading'> Easter occurs on: </p><br />")
	print("<p class = 'date'>")
	if DisplayMethod == 'number' or DisplayMethod == 'both':
		print("{}/{}/{}".format(day, month, year))
	print("<br />")
	if DisplayMethod == 'word' or DisplayMethod == 'both':
		print("{}{} of {} {}".format(day, suffix, namedMonth, year))
	print("</p>")
print("</body>")
print("</html>")
