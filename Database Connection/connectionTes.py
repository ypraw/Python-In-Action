import connection as dbs
import warnings
warnings.filterwarnings('error')

mysqli = dbs.MysqlUserDB(DBrootHost='127.0.0.1',
                         DBrootUser='root',
                         DBrootPass='',
                         DBrootDatabase='pos')

db = mysqli.getDB()

try:
    db.execute("select * from product")
    results = db.fetchall()
    for result in results:
        print(result)
except db.Error as error:
    print(error)
mysqli.delCon()
