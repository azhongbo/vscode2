#!/usr/bin/python3
import sys


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode SQL ( 範例 )"
# MyCodeString = '''
# ### file: mainCode_SQL
# ###  SQL 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode SQL ( 範例 )"
# MyCodeString = '''
# ###  SQL 範例程式 ####
# ### file: mainCode_SQL
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( SQLITE for Python 一般範例 )"
MyCodeString = '''
###  Python SQLite ####
### file: mainCode_SQL
conn = sqlite3.connect('data.sqlite3')
cursor = conn.cursor()
sql = """ REPLACE INTO main.table (id,date,source) VALUES (NULL,'%s','%s') """ %(today,source)
cursor.execute(sql)
conn.commit()
for row in cursor.execute( "SELECT * FROM main.table WHERE a='b'"):
    arr.append( str(row[0]) )
conn.close()
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( SQLITE for Python 迴圈檢查範例 )"
MyCodeString = '''
###  SQLLite Python 範例程式 ####
### file: mainCode_SQL
import sqlite3,time
def connect2SQL(sql,filename):    
    sqlFlag = True
    while sqlFlag:
        try:
            ## 執行 sql 指令
            conn = sqlite3.connect(filename)
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            conn.close()
            sqlFlag = False  ## 若正常執行完畢，sqlFlag = False ，中斷 while
        except:
            time.sleep(1)
            sqlFlag = True  ## 若無法執行完，sqlFlag = True 繼續 while
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( SQLITE for PHP )"
MyCodeString = '''
###  PHP SQLite ####
### file: mainCode_SQL
function ext($uid)
{
    $mydb = new PDO("sqlite:sqlite3/mydb.sqlite");
    $sql = "SELECT * FROM main.table WHERE uid = '$uid' ";
    $qry = $mydb->prepare($sql);
    $qry->execute();
    while($row = $qry->fetch(PDO::FETCH_ASSOC))
        {
            $name  = $row['name'];
            $ename = $row['ename'];
            $dep_e = $row['dep_e'];
            $dep_c = $row['dep_c'];
            $title = $row['title'];
            $ext   = $row['ext'];
        }
}
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( SQLITE 建立 table )"
MyCodeString = '''
### SQL 語法建立 SQL ###
### file: mainCode_SQL
CREATE TABLE main.chgData ( 
    id     INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , 
    ipaddr VARCHAR, 
    func   VARCHAR , 
    data   VARCHAR ,
    UNIQUE (ipaddr, func)    
)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( MySQL 建立 table )"
MyCodeString = '''
### MySQL 建立 table ###
### file: mainCode_SQL
CREATE TABLE test (
    id int(11) NOT NULL AUTO_INCREMENT,
    dt datetime DEFAULT NULL,
    name1 varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
    name2 varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    name3 varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    dep varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    data text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY name1 (name1,name2,name3)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( MySQL for PHP )"
MyCodeString = '''
### MySQL for PHP ###
### file: mainCode_SQL
// CONNECT DB
$servername = "localhost";
$username   = "root";
$password   = 'r@1234';
$dbname     = "testDB";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) 
{
    die("Connection failed: " . $conn->connect_error);
}

// INSERT DATA
$sql = "INSERT INTO testTab (id, name, dep) VALUES (NULL, '小王', '人事')";
if ($conn->multi_query($sql) === TRUE) 
{
    echo "New records created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// SELECT DB
$sql = "SELECT * FROM testTab";
$result = $conn->query($sql);
if ($result->num_rows > 0) 
{
    while($row = $result->fetch_assoc()) 
    {
        print $row["name"] . "<br>";
    }
} 
$conn->close();
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( PostgreSQL for PHP )"
MyCodeString = '''
### PostgreSQL for PHP ###
### file: mainCode_SQL
$host        = "host=127.0.0.1";
$port        = "port=5432";
$dbname      = "dbname=testDB";
$credentials = "user=postgres password=1234";

$db = pg_connect( "$host $port $dbname $credentials"  );
if(!$db){
   echo "Error : Unable to open database";
} else {
   echo "Opened database successfully";
}


$sql = "
CREATE TABLE measurement (
    city_id         int not null,
    logdate         date not null,
    peaktemp        int,
    unitsales       int
) PARTITION BY RANGE (logdate); ";


$sql = "
CREATE TABLE account(
	user_id serial PRIMARY KEY,
	username VARCHAR (50) UNIQUE NOT NULL,
	password VARCHAR (50) NOT NULL,
	email VARCHAR (355) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP
);  ";

$sql = "
CREATE TABLE testTab (
id serial PRIMARY KEY,
datetime TIMESTAMP ,
aa VARCHAR (50),
bb VARCHAR (50),
cc TEXT,
UNIQUE (aa , bb )
);  ";
$ret = pg_query($db, $sql);

$sql = "
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Paul', 32, 'California', 20000.00 );
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (6, 'Allen', 25, 'Texas', 15000.00 );
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (7, 'Teddy', 23, 'Norway', 20000.00 );
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (8, 'Mark', 25, 'Rich-Mond ', 65000.00 );
";
$ret = pg_query($db, $sql);


$sql = "SELECT * from COMPANY;";
$ret = pg_query($db, $sql);
while($row = pg_fetch_row($ret))
{
    $id      = $row[0];
    $name    = $row[1];
    $address = $row[2];
    $salary  = $row[3];
    print "$id $name $address $salary <br>\n";
}

pg_close($db);
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode SQL ( PostgreSQL for Python )"
MyCodeString = '''
### PostgreSQL for Python ###
### file: mainCode_SQL
import psycopg2
import pandas as pd

## 連結
conn = psycopg2.connect(database="test", user="postgres", password="1234", host="127.0.0.1", port="5432")

## CREATE DB
cur = conn.cursor()
cur.execute("""CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);""")
conn.commit()

## INSERT DATA
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Jack', 22, 'California', 25000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Zoe', 25, 'Texas', 18000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Vincent', 23, 'Norway', 22000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Anita', 26, 'Rich-Mond ', 25000.00 )");
conn.commit()

## SELECT DATA
cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print(row[1])

## pandas SELECT DATA
sql = "SELECT id, name, address, salary  from COMPANY"
data1 = pd.read_sql(sql, conn)

conn.close()
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


