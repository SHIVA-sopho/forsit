
import numpy as np
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='shiva123',db='forsit')

query1 = "select * from challenges_properties"

result = conn.query(query1)

result = conn.store_result()

challenges = result.fetch_row(maxrows=0)

challenges = np.array(challenges)

query2 = "select * from user_properties"

conn.query(query2)

result = conn.store_result()

user = result.fetch_row(maxrows=0)

user = np.array(user)



