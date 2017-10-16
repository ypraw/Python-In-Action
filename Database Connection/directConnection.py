import MySQLdb as db

connection = db.connect('127.0.0.1', 'root', '', 'pos')

cursor = connection.cursor()


def TampilDB():
    ids = '1'
    query = "SELECT * from product where id = (%s) "

    cursor.execute(query, ids)
    result = cursor.fetchone()
    print(result[1])
    for items in result:
        print(items)


def InsertDB():
    cursor.execute("INSERT INTO `product` VALUES (%s, %s, %s, %s)",
                   ('', 'Chiki', '5000', '50',))
    connection.commit()


def UpdateDB():
    cursor.execute("UPDATE product SET name= (%s), price= (%s), stock= (%s)"
                   "Where id= ( %s)",
                   ("Permen", "500", "10", "1"))
    connection.commit()


def deleteDB():
    cursor.execute("DELETE FROM `product` WHERE `product`.`id` = 12")
    connection.commit()


TampilDB()
cursor.close()
connection.close()
