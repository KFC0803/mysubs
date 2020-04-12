from pyonfx import *
import random
io = Ass("OP_TEST.ass")
meta, styles, lines = io.get_data()

def fx(line, l):
	l.layer = 2
	l.style = "Default"

	l.start_time = line.start_time 
	l.end_time = line.start_time + 400

	l.text = "{\\an5\\pos(%d,%d)\\fad(0,400)\\fs%d\\c&HC5EFFF&"\
	"\\t(0,400,\\fs%d)}%s" % (
	line.x, line.y + line.height/2, line.styleref.fontsize,
	line.styleref.fontsize + 2, line.text)
	io.write_line(l)
	for syl in Utils.all_non_empty(line.syls):

		# 文字

		l.layer = 0
		l.style = "Default"

		l.start_time = line.start_time 
		l.end_time = line.end_time

		l.text = "{\\pos(%.3f,%d)\\1a&HAA&\\fad(100,100)"\
			"\\t(%d,%d,\\1a&H00&)}%s" % (
			syl.x, syl.y, 
			syl.start_time - 100, syl.start_time, syl.text)
		io.write_line(l)

		

		#描边
		for i in range(3):
			l.layer = 1
			l.style = "Default"

			l.start_time = line.start_time + syl.start_time - 200
			l.end_time = line.start_time + syl.end_time + 100
			y = syl.y + random.randint(-30,30)
			l.text = "{\\move(%.3f,%d,%.3f,%d)\\1a&HAA&\\fad(200,200)"\
			"}%s" % (
			syl.x + random.randint(-20,20), y,syl.center + random.randint(-20,20), y,
			syl.text)
			io.write_line(l)
		
		if syl.text == "watch":
			l.layer = 2
			l.style = "Default"

			l.start_time = line.start_time + syl.start_time - 200
			l.end_time = line.start_time + syl.start_time + 400

			l.text = "{\\an5\\pos(%.3f,%d)\\fad(0,600)\\fs%d\\c&HC5EFFF&"\
			"\\t(0,400,\\fs%d)}%s" % (
			syl.x, syl.y + syl.height/2, syl.styleref.fontsize,
			syl.styleref.fontsize + 10, syl.text)
			io.write_line(l)


for line in lines:
	fx(line,line.copy())

#	for syl in Utils.all_non_empty(line.syls):
#		print(syl)
io.save()
io.open_aegisub()