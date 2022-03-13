#!/usr/bin/python3
import sys
from __save__ import *

########################################################
def runAllData(MyCodeTitle,MyCodeString,MyCodeName):
    global package1,package2,extension,count

    count = count + 1    

    (data1,data2,data3) = makeCode(MyCodeTitle,MyCodeString,MyCodeName+str(count))

    package1  = package1  + data1
    package2  = package2  + data2
    extension = extension + data3
########################################################


package1   = ""
package2   = ""
extension  = ""
count      = 0
MyCodeName = sys.argv[2]


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode web ( 範例 )"
# MyCodeString = '''
# ###  Web 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode web ( 範例 )"
# MyCodeString = '''
# ###  Web 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode web ( 範例 )"
# MyCodeString = '''
# ###  Web 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode web ( 範例 )"
# MyCodeString = '''
# ###  Web 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode web ( 表格輸入範例 )"
MyCodeString = '''
###  Web 表格輸入範例 ####
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.js"></script>
<?php
$mydb = new PDO("sqlite:mydb.sqlite");
function createData()
{
    global $mydb;
    $sql = "DROP TABLE IF EXISTS main.chgData;";
    $qry = $mydb->prepare($sql);
    $qry->execute();
    
    $sql = "
    CREATE TABLE IF NOT EXISTS main.chgData ( 
        id     INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , 
        name VARCHAR,  age   VARCHAR,  sex   VARCHAR )";
    $qry = $mydb->prepare($sql);
    $qry->execute();
    
    $sql = "INSERT INTO main.chgData VALUES 
    (NULL,'Ryan','28','M'),
    (NULL,'Alex','32','M'),
    (NULL,'Anita','19','F'); ";
    $qry = $mydb->prepare($sql);
    $qry->execute();
}

function selectData()
{
    global $mydb;
    $sql = "SELECT * FROM main.chgData WHERE 1";
    $qry = $mydb->prepare($sql);
    $qry->execute();
    while($row = $qry->fetch(PDO::FETCH_ASSOC))
        {
            $id    = $row['id'];
            $name  = $row['name'];
            $age   = $row['age'];
            $sex   = $row['sex'];
    
            $tab = $tab . "
            <tr>
                <td><input id=name$id type=text value='$name' ></td>
                <td><input id=age$id type=text value='$age'   ></td>
                <td><input id=sex$id type=text value='$sex'   ></td>
            </tr>        
            ";
        }
    return $tab;
}
// createData();

?>

<table id=myTab border=0>
    <?php
    print selectData();
    ?>
</table>
<hr>
<input id=tmpBox1 style='width:95%;' type=text value=tmpBox1 title=tmpBox1> <br>
<input id=tmpBox2 style='width:95%;' type=text value=tmpBox2 title=tmpBox2> <br>

<script>
var IdBox = [];
$('#myTab').click(function(){ logID() })
// $('#myTab').on('keydown', function(e){    if(e.keyCode == '9'){ logID(); }   });
$('#myTab').on('keyup', function(){  logID(); })

function logID()
{
    // focusID = $(':focus').attr('id'); //取得 focus 定位點的 id
    // focusValue = $(':focus').val();   //取得 focus 定位點的 值
    currentID = $(':focus').attr('id');

    if( currentID != null )
    {
        $('#tmpBox2').val( currentID )
        IdBox.push( currentID )
        IdBox = IdBox.filter( onlyUnique ); 
        $('#tmpBox1').val( IdBox )
    }
}

// array 移除重複
function onlyUnique(value, index, self) { return self.indexOf(value) === index; }
</script>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)








##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
