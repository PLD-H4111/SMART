
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toorTOOR2019!",
  database="main"
)


print(mydb)


request = "SHOW DATABASES"
request2 = "select * from restaurant" # where theme = \"beurk\";"


mycursor = mydb.cursor()
mycursor.execute(request2)

# myresult
mycursor = mycursor.fetchall()

restaurants = """{"restaurants": ["""
for i, restaurant in enumerate(mycursor):
	restaurants += """{{ "id":{}, "name":{}, "theme": {} ,"status":"closed", "eta":2500 }}""".format(restaurant[0], restaurant[1], restaurant[2])
	if i != len(mycursor):
		restaurants += ","
restaurants += """ ] } """

print(restaurants)

#for x in mycursor:
#  print(x) 



"""

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

"""

