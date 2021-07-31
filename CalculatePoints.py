import sqlite3

#Function to calculate score:
def CalculateScore(row):
    points = 0.0
    score = float(row[1])
    faced = float(row[2])
    fours = float(row[3])
    sixes = float(row[4])
    wkts = float(row[8])
    wkt_points = float(10 * wkts)
    bowled = float(row[5])
    given = float(row[7])
    try:
        strike_rate = float(score/faced)
    except:
        strike_rate = 0.0
    try:
        economy_rate = float(given/(bowled/6))
    except:
        economy_rate = 0.0
    twos =int(score - (4*fours + 6*sixes))
    point3=0
    point2=0
    point7=0
    point8=0

    point1 = int(1*(twos/2)) #1 point for two runs scored
    if score>100:
        point2 = 10
    elif score>=50:
        point2 = 5 #additional 5 and 10 points for half and full century respectively
    if strike_rate>1:
        point3 = 4
    elif strike_rate>=0.8:
        point3 = 2  #additional 4 and 2 points for strike rate greater than 100 or between 80-100 resp.
    point4 = fours*1 #1 point for hitting a boindary
    point5  = 2*sixes #2 points for hitting over the boundary
    point6 = wkt_points  #10 points for each wicket
    if wkt_points>=5:
        point7 = 10
    elif wkt_points>3:
        point7 = 5 #additional 10 and 5 points for 5 or more and for 3 wickers per innings respectively
    if economy_rate>=3.5 and economy_rate<=4.5:
        point8 = 4 #additional 4 points for economy rate between 3.5 and 4.5
    elif economy_rate>=2 and economy_rate<3.5 :
        point8 = 7 #additional 7 points for economy rate between 2 and 3.5
    elif economy_rate<2:
        point8 = 10 #10 points for economy rate less than 2
    Fielding  = float(row[9]) + float(row[10]) + float(row[11]) 
    point9 = float(10*Fielding) #10 points for catch/stumping/runout

    points = float(point1+point2+point3+point4+point5+point6+point7+point8+point9)  #final points earned by the player
    return points

    
player_points = {}
#Connecting to database
try:
    
    obj1 = sqlite3.connect("MyCricketGame_Database.db")
    obj2 = obj1.cursor()
except:
    print("Database not found")
    

#fetching data from database
try:
    obj2.execute("SELECT * FROM match")
    row = obj2.fetchall()
except:
    print("No any data found")
    
    
#calculating the scores of each player
for data in row:
    player_points[data[0]] = CalculateScore(data)
print(player_points)

        
'''#Function to calculate score:
def CalculateScore(row):
    points = 0.0
    score = float(row[1])
    faced = float(row[2])
    fours = float(row[3])
    sixes = float(row[4])
    wkts = float(row[8])
    wkt_points = float(10 * wkts)
    bowled = float(row[5])
    given = float(row[7])
    try:
        strike_rate = float(score/faced)
    except:
        strike_rate = 0.0
    try:
        economy_rate = float(given/(bowled/6))
    except:
        economy_rate = 0.0
    twos =float(score - (4*fours + 6*sixes))

    point1 = float(1*(twos/2)) #1 point for two runs scored
    if score>=100:
        point2 = 10
    elif score>=50:
        point2 = 5 #additional 5 and 10 points for half and full century respectively
    if strike_rate>1:
        point3 = 4
    elif strike_rate>=0.8:
        point3 = 2  #additional 4 and 2 points for strike rate greater than 100 or between 80-100 resp.
    point4 = fours*1 #1 point for hitting a boindary
    point5  = 2*sixes #2 points for hitting over the boundary
    point6 = wkt_points  #10 points for each wicket
    if wkt_points>=5:
        point7 = 10
    elif wkt_points>=3:
        point7 = 5 #additional 10 and 5 points for 5 or more and for 3 wickers per innings respectively
    if economy_rate>=2 and economy_rate<=3.5 :
        point8 = 7 #additional 7 points for economy rate between 2 and 3.5
    elif economy_rate>3.5 and economy_rate<=4.5:
        point8 = 4 #additional 4 points for economy rate between 3.5 and 4.5
    elif economy_rate<2:
        point8 = 10 #10 points for economy rate less than 2
    Fielding  = float(row[9]) + float(row[10]) + float(row[11]) 
    point9 = float(10*Fielding) #10 points for catch/stumping/runout

    points = float(point1+point2+point3+point4+point5+point6+point7+point8+point9)  #final points earned by the player
    return points
    '''
