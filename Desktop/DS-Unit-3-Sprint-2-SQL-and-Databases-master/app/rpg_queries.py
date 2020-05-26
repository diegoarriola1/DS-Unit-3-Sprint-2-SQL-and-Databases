import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(
    __file__), "..", "data", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
# connection.row_factory = sqlite3.Row  # allow us to reference rows as dicts
# print("CONNECTION:", connection)

cursor = connection.cursor()
# print("CURSOR", cursor)

query = "SELECT count(distinct charactercreator_character.character_id) as CharCount FROM charactercreator_character"

# result = cursor.execute(query)
# print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

# for row in result2:
#     print("How many total Characters are there?: " + str(row["CharCount"]))

# How many total Characters are there?
result = cursor.execute(query).fetchall()
print("How many total Characters are there? ", result[0][0])

# How many of each specific subclass?
query1 = "SELECT count(distinct charactercreator_mage.character_ptr_id) as MageCount FROM charactercreator_mage"
query2 = "SELECT count(distinct charactercreator_thief.character_ptr_id) as ThiefCount FROM charactercreator_thief"
query3 = "SELECT count(distinct charactercreator_cleric.character_ptr_id) as ClericCount FROM charactercreator_cleric"
query4 = "SELECT count(distinct charactercreator_fighter.character_ptr_id) as FighterCount FROM charactercreator_fighter"




result1 = cursor.execute(query1).fetchall()
print("How many of each specific subclass? ", "Mage", result1[0][0])

result2 = cursor.execute(query2).fetchall()
print("How many of each specific subclass? ", "Thief", result2[0][0])

result3 = cursor.execute(query3).fetchall()
print("How many of each specific subclass? ", "Cleric", result3[0][0])

result4 = cursor.execute(query4).fetchall()
print("How many of each specific subclass? ", "Thief", result4[0][0])
