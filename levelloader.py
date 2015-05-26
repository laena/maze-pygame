import question
import monster

def load(theme, levelfile, questionfile):
	obstacles = []
	monsters = []
	questions = {}
	qf = open(questionfile)
	with open(levelfile) as f:
		y = 0
		for line in f:
			if line.strip() == "": continue
			x = 0
			for char in line:
				if char == "x":# obstacle
					obstacles.append((x,y))
				elif char == "o":
					questionline = qf.readline()
					items = questionline.split(",")
					if questionline != "" and len(items) == 2:
						q = items[0].strip()
						answer = items[1].strip()
						questions[question.Question(theme, q, answer, x, y)] = False
				elif char == "g":
					goalpos = (x, y)
				elif char == "m":
					monsters.append(monster.Monster(theme, x*theme.gridsize, y*theme.gridsize))
				x += 1
			y += 1
	return obstacles, questions, goalpos, monsters

def loadAuto(theme):
	obstacles = []
	monsters = []
	questions = {}
	y = 0
	questionstring = """
	81 243 729 ..?,2187
	First phrase spoken on the moon?,contact light
	How many months have 28 days?,12
	What is the most intelligent species?,dolphins
	What word gets shorter if you add 2 letters?,short
	56 69 83 98 ..?,114
	Who was awarded the most Oscars?,Walt Disney
	cre neqhn nq nfgen,per ardua ad astra"""

	levelstring = """
	-------ox-------
	-x--x--xx-xxxxx-
	-x--xoxx--x-x-x-
	ox--x-----x-x-x-
	xxx-x-o-x-x-x-x-
	xox-x---x-x---x-
	x-x-x-x-x-xx-ox-
	x-x-x-x-x-x--xx-
	x-----xmxox--x--
	x-xxxxxxxxx--x-x
	xoxo-----------g
	xxxxxxxxxxxxxxxx"""

	qiter = iter(questionstring.splitlines())
	for line in levelstring.splitlines():
		line = line.strip()
		if line == "": continue
		x = 0
		for char in line:
			if char == "x":# obstacle
				obstacles.append((x,y))
			elif char == "o":
				questionline = qiter.next()
				items = questionline.split(",")
				if questionline != "" and len(items) == 2:
					q = items[0].strip()
					answer = items[1].strip()
					questions[question.Question(theme, q, answer, x, y)] = False
			elif char == "g":
				goalpos = (x, y)
			elif char == "m":
				monsters.append(monster.Monster(theme, x*theme.gridsize, y*theme.gridsize))
			x += 1
		y += 1
	return obstacles, questions, goalpos, monsters