feature=[
	"Name",
	"Age",
	"Nationality",
	"Overall",
	"Potential",
	"Club",
	"Value",
	"Wage",
	"Special",
	"Preferred Foot",
	"International Reputation",
	"Weak Foot",
	"Skill Moves",
	"Work Rate",
	"Body Type",
	"Real Face",
	"Position",
	"Jersey Number",
	"Joined",
	"Contract Valid Until",
	"Height",
	"Weight",
	"LS",
	"ST",
	"RS",
	"LW",
	"LF",
	"CF",
	"RF",
	"RW",
	"LAM",
	"CAM",
	"RAM",
	"LM",
	"LCM",
	"CM",
	"RCM",
	"RM",
	"LWB",
	"LDM",
	"CDM",
	"RDM",
	"RWB",
	"LB",
	"LCB",
	"CB",
	"RCB",
	"RB",
	"Crossing",
	"Finishing",
	"HeadingAccuracy",
	"ShortPassing",
	"Volleys",
	"Dribbling",
	"Curve",
	"FKAccuracy",
	"LongPassing",
	"BallControl",
	"Acceleration",
	"SprintSpeed",
	"Agility"	,
	"Reactions"	,
	"Balance"	,
	"ShotPower"	,
	"Jumping"	,
	"Stamina"	,
	"Strength"	,
	"LongShots"	,
	"Aggression"	,
	"Interceptions"	,
	"Positioning"	,
	"Vision"	,
	"Penalties"	,
	"Composure"	,
	"Marking"	,
	"StandingTackle"	,
	"SlidingTackle"	,
	"GKDiving"	,
	"GKHandling"	,
	"GKKicking"	,
	"GKPositioning"	,
	"GKReflexes"	,
	"Release Clause"
]
##
mean_ = []
def best_player():
	import sqlite3 as sq
	import numpy as np
	# WTHE BEST PLAYER
	con=sq.connect("fifa analysis.db")
	exe=con.cursor()
	exe.execute(""" SELECT LS,ST,RS,LW,LF,CF,RF,RW,LAM,CAM,RAM,LM,LCM,CM,RCM,RM,LWB,LDM,CDM,RDM,RWB,LB,LCB,CB,RCB,RB,Crossing,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,Vision,Penalties,Composure,Marking,StandingTackle,SlidingTackle,GKDiving,GKHandling,GKKicking,GKPositioning,GKReflexes FROM  data """)
	frature_for_one_player=[]
	frature_for_one_player_mod=[]

	players_names=[]
	for mean1 in exe.fetchall():
		frature_for_one_player.append(mean1[0:])
		for mean12 in frature_for_one_player[0][0:]:
			if mean12=="NONE" or mean12=="none" :
				frature_for_one_player_mod.append(0)
			else:
				frature_for_one_player_mod.append(int(float(str(mean12.replace(",",".")))))
		mean_.append(int(np.mean(frature_for_one_player_mod)))
		frature_for_one_player.clear()
		frature_for_one_player_mod.clear()
	exe.execute(""" SELECT Name FROM data""")
	for mean1 in exe.fetchall():
		players_names.append(mean1[0])
	# len samples of data
	# get best  and lowest player
	#best
	index=mean_.index(np.max(mean_))
	print("best player is ",players_names[index],mean_[index])
	#lowest
	index = mean_.index(np.min(mean_))

	print("lowest player is ",players_names[index],mean_[index])
def total_numper_of_left_food_and_right():
	#Preferred Foot
	foot=[]
	import sqlite3 as sq
	con = sq.connect("fifa analysis.db")
	exe = con.cursor()
	exe.execute(""" SELECT Preferred_Foot FROM data """)
	for add_foot in exe.fetchall():
		foot.append(add_foot[0])

	#right
	print("right",":",foot.count("Right"))
	print("Left", ":", foot.count("Left"))
def avrage_RATING_OF_THE_PLAYERS():
	import sqlite3 as sq
	import numpy as np
	# WTHE BEST PLAYER
	con = sq.connect("fifa analysis.db")
	exe = con.cursor()
	exe.execute(
		""" SELECT LS,ST,RS,LW,LF,CF,RF,RW,LAM,CAM,RAM,LM,LCM,CM,RCM,RM,LWB,LDM,CDM,RDM,RWB,LB,LCB,CB,RCB,RB,Crossing,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,Vision,Penalties,Composure,Marking,StandingTackle,SlidingTackle,GKDiving,GKHandling,GKKicking,GKPositioning,GKReflexes FROM  data """)
	frature_for_one_player = []
	frature_for_one_player_mod = []

	players_names = []
	for mean1 in exe.fetchall():
		frature_for_one_player.append(mean1[0:])
		for mean12 in frature_for_one_player[0][0:]:
			if mean12 == "NONE" or mean12 == "none":
				frature_for_one_player_mod.append(0)
			else:
				frature_for_one_player_mod.append(int(float(str(mean12.replace(",", ".")))))
		mean_.append(int(np.mean(frature_for_one_player_mod)))
		frature_for_one_player.clear()
		frature_for_one_player_mod.clear()
	exe.execute(""" SELECT Name FROM data""")
	for mean1 in exe.fetchall():
		players_names.append(mean1[0])
	# len samples of data
	# get best  and lowest player
	# best
	index = mean_.index(np.max(mean_))

	# lowest
	index = mean_.index(np.min(mean_))


	print("avg of the most players",":",np.mean(mean_))
def distribution_player_nationality():
	from sklearn.preprocessing import LabelEncoder
	import matplotlib.pyplot as plt
	import numpy
	nationality = []
	import sqlite3 as sq
	con = sq.connect("fifa analysis.db")
	exe = con.cursor()
	exe.execute(""" SELECT Nationality FROM data """)
	for add_foot in exe.fetchall():
		nationality.append(add_foot[0])
	converter=LabelEncoder()
	#

	new_array=converter.fit_transform(nationality)
	print(new_array)
	main_array=converter.inverse_transform(new_array)
	print(main_array)
	plt.scatter(main_array,new_array)
	plt.show()
	print("distribution of nationality (std)",numpy.std(new_array))
def distribution_of_psition():
	from sklearn.preprocessing import LabelEncoder
	import matplotlib.pyplot as plt
	import numpy
	nationality = []
	import sqlite3 as sq
	con = sq.connect("fifa analysis.db")
	exe = con.cursor()
	exe.execute(""" SELECT Position FROM data """)
	for add_foot in exe.fetchall():
		nationality.append(add_foot[0])
	converter=LabelEncoder()
	#

	new_array=converter.fit_transform(nationality)
	print(new_array)
	main_array=converter.inverse_transform(new_array)
	print(main_array)
	plt.scatter(main_array,new_array)
	plt.show()
	print("distribution of position (std)",numpy.std(new_array))
def Wage_avg():
	#Wage
	from sklearn.preprocessing import LabelEncoder
	import matplotlib.pyplot as plt
	import numpy
	Wage_T = []
	import sqlite3 as sq
	con = sq.connect("fifa analysis.db")
	exe = con.cursor()
	exe.execute(""" SELECT Wage FROM data """)
	for add_foot in exe.fetchall():
		Wage_T.append(float(str(add_foot[0].replace(",","."))))
	print(Wage_T)
	print("avg of wage",numpy.mean(Wage_T))





Wage_avg()