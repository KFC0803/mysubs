from pyonfx import *

io = Ass("input.ass")
meta, styles, lines = io.get_data()

def jp(line, l):
    #出场炫光
    l.start_time = line.end_time - 200
    l.end_time = line.end_time
    l.style = 'OP_'

    l.layer = 3
    l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy300\\blur10\\c&H55FF29&}%s" % (line.center, line.middle, line.text)
    io.write_line(l)

    l.layer = 2
    l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy400\\blur20\\c&H82FFB5&}%s" % (line.center, line.middle, line.text)
    io.write_line(l)

    l.layer = 0
    l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy450\\blur20\\c&H82FFDD&}%s" % (line.center, line.middle, line.text)
    io.write_line(l)


    for syl in Utils.all_non_empty(line.syls):
        #入场
        l.start_time = line.start_time + syl.start_time
        l.end_time = line.end_time
        l.style = 'OP'
        l.layer = 1
        l.text = '{\\org(%d,%d)\\frx0\\fad(0,100)\\move(%.2f,%.2f,%.2f,%.2f,0,50)\\t(%d,%d,\\frx30)}%s' % (line.x, line.y, syl.x, syl.y + 200, syl.x, syl.y, - syl.start_time, l.end_time - l.start_time, syl.text)
        io.write_line(l)

        #入场炫光
        l.start_time = line.start_time + syl.start_time
        l.end_time = line.start_time + syl.start_time + 300
        l.style = 'OP_'

        l.layer = 0
        l.text = '{\\pos(%.2f,%.2f)\\fad(20,250)\\fscx250\\blur20\\c&H82FFDD&}%s' % (syl.center, syl.middle, syl.text)
        io.write_line(l)

        l.layer = 2
        l.text = '{\\pos(%.2f,%.2f)\\fad(20,250)\\fscx200\\blur20\\c&H82FFB5&}%s' % (syl.center, syl.middle, syl.text)
        io.write_line(l)

        l.layer = 3
        l.text = '{\\pos(%.2f,%.2f)\\fad(20,250)\\fscx100\\blur10\\c&H55FF29&}%s' % (syl.center, syl.middle, syl.text)
        io.write_line(l)
def cn(line, l):
    #入场
    l.text = '{\\frx0\\fad(0,100)\\move(%.2f,%.2f,%.2f,%.2f,0,50)\\t(50,%d,\\frx-30)}%s' % (line.x, line.y - 200, line.x, line.y, line.duration, line.text)
    io.write_line(l)

    #入场炫光
    l.start_time = line.start_time 
    l.end_time = line.start_time + 300
    l.style = 'OP_CHS_'

    l.layer = 0
    l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx250\\blur20\\c&H82FFDD&}%s' % (l.center, l.middle, line.text)
    io.write_line(l)

    l.layer = 2
    l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx200\\blur20\\c&H82FFB5&}%s' % (l.center, l.middle, line.text)
    io.write_line(l)

    l.layer = 3
    l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx100\\blur10\\c&H55FF29&}%s' % (l.center, l.middle, line.text)
    io.write_line(l)

    #出场炫光
    l.start_time = line.end_time - 200
    l.end_time = line.end_time

    l.layer = 3
    l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy300\\blur10\\c&H55FF29&}%s" % (line.center, line.middle, line.text)
    io.write_line(l)

    l.layer = 2
    l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy400\\blur20\\c&H82FFB5&}%s" % (line.center, line.middle, line.text)
    io.write_line(l)

    l.layer = 0
    l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy450\\blur20\\c&H82FFDD&}%s" % (line.center, line.middle, line.text)
    io.write_line(l)

def color(line,l):
    colors = ['&HFF81FF&', '&HFF898C&', '&HFDFB56&', '&H75FF77&', '&H79FFFF&', '&H3F35DB&']
    #文字闪烁

    for char in Utils.all_non_empty(line.chars):
        text = ''
        for i in range(1,11):
            index = char.i + i
            while index > len(colors):
                index = index - len(colors)
            text = text + '\\t(%d,%d,\\3c%s)' % (460*(i-2), 460*(i-2), colors[index - 1])
            
        l.text = '{\\pos(%.2f,%.2f)\\fad(100,100)\\blur5%s}%s' % (char.x, char.y, text, char.text)
        io.write_line(l)        


    if line.style == 'OP':
        #入场炫光
        l.start_time = line.start_time 
        l.end_time = line.start_time + 300
        l.style = 'OP_'

        l.layer = 0
        l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx250\\blur20\\c&H82FFDD&}%s' % (l.center, l.middle, line.text)
        io.write_line(l)

        l.layer = 2
        l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx200\\blur20\\c&H82FFB5&}%s' % (l.center, l.middle, line.text)
        io.write_line(l)

        l.layer = 3
        l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx100\\blur10\\c&H55FF29&}%s' % (l.center, l.middle, line.text)
        io.write_line(l)

        #出场炫光
        l.start_time = line.end_time - 200
        l.end_time = line.end_time

        l.layer = 3
        l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy300\\blur10\\c&H55FF29&}%s" % (line.center, line.middle, line.text)
        io.write_line(l)

        l.layer = 2
        l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy400\\blur20\\c&H82FFB5&}%s" % (line.center, line.middle, line.text)
        io.write_line(l)

        l.layer = 0
        l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy450\\blur20\\c&H82FFDD&}%s" % (line.center, line.middle, line.text)
        io.write_line(l)

    if line.style == 'OP_CHS':
        #入场炫光
        l.start_time = line.start_time 
        l.end_time = line.start_time + 300
        l.style = 'OP_CHS_'

        l.layer = 0
        l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx250\\blur20\\c&H82FFDD&}%s' % (l.center, l.middle, line.text)
        io.write_line(l)

        l.layer = 2
        l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx200\\blur20\\c&H82FFB5&}%s' % (l.center, l.middle, line.text)
        io.write_line(l)

        l.layer = 3
        l.text = '{\\pos(%d,%d)\\fad(20,250)\\fscx100\\blur10\\c&H55FF29&}%s' % (l.center, l.middle, line.text)
        io.write_line(l)

        #出场炫光
        l.start_time = line.end_time - 200
        l.end_time = line.end_time

        l.layer = 3
        l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy300\\blur10\\c&H55FF29&}%s" % (line.center, line.middle, line.text)
        io.write_line(l)

        l.layer = 2
        l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy400\\blur20\\c&H82FFB5&}%s" % (line.center, line.middle, line.text)
        io.write_line(l)

        l.layer = 0
        l.text = "{\\pos(%d,%d)\\fad(30,50)\\fscy450\\blur20\\c&H82FFDD&}%s" % (line.center, line.middle, line.text)
        io.write_line(l)

for line in lines:
    if line.text in ("建造城镇又破坏城镇 真忙碌", "街は作って壊して忙しいや"):
        color(line, line.copy())
    elif line.style == 'OP':
        jp(line, line.copy())
    else:
        cn(line, line.copy())

io.save()
io.open_aegisub()