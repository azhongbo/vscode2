#!/usr/bin/python3
import sys




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode PHP ( 範例 )"
# MyCodeString = '''
# ###  PHP 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode PHP ( 範例 )"
# MyCodeString = '''
# ###  PHP 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( multi level associative array )"
MyCodeString = '''
###  PHP multi level associative array ####
$languages = array();
  
$languages['Python'] = array(
    "first_release" => "1991", 
    "latest_release" => "3.8.0", 
    "designed_by" => "Guido van Rossum",
    "description" => array(
        "extension" => ".py", 
        "typing_discipline" => "Duck, dynamic, gradual",
        "license" => "Python Software Foundation License"
    )
);
  
print_r($languages['Python']['description']);
echo $languages['Python']['latest_release'];
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( 執行外部命令 )"
MyCodeString = '''
###  php 執行外部命令 ####
$data = shell_exec("chmod a+rwx $filename");
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


MyCodeTitle  = "RyanCode PHP ( Err 顯示設定 )"
MyCodeString = '''
###  php Err 顯示設定 ####
error_reporting( E_ALL );
ini_set( "display_errors", 1 );
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( 寫入檔案 )"
MyCodeString = '''
###  PHP 寫入檔案 ####
function write_file($filename,$txt)
	{
		$myfile = fopen("$filename", "w") or die("Unable to open file!");
		fwrite($myfile, $txt);
		fclose($myfile);
	}
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( 分割字串 )"
MyCodeString = '''
###  PHP 分割字串 ####
list($a,$b,$c) = explode( ',' , $string );
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( POST 範例 )"
MyCodeString = '''
###  PHP POST 範例 ####
$url = "http://localhost/test/aa.php";

$data = array(
    'UserName' => 'Ryan' , 
    'ext'      => '1075'
);

$options = array(   // use key 'http' even if you send the request to https://...
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);

$context  = stream_context_create($options);
$result   = file_get_contents($url, false, $context);
if ($result === FALSE) { /* Handle error */ }

print "$result";
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( 讀取 https )"
MyCodeString = '''
// ###  PHP 讀取 https ####
$url = "https://username:password@192.168.1.100/admin/";
$arrContextOptions=array(
    "ssl"=>array(
          "verify_peer"=>false,
          "verify_peer_name"=>false,
      ),
  );  

$response = file_get_contents($url, false, stream_context_create($arrContextOptions));
print "$response";
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( json 傳值後轉換 )"
MyCodeString = '''
###  PHP 使用 json 傳值，轉換 ####
$arr = json_decode(  $_POST['data']  );

while($arr)
{
    $array = object_array( array_shift($arr) );
    print $array['name'] . "\n";
    print $array['dep'] . "\n";
}


function object_array($array) {  
    if(is_object($array)) {  
        $array = (array)$array;  
     } if(is_array($array)) {  
         foreach($array as $key=>$value) {  
             $array[$key] = object_array($value);  
             }  
     }  
     return $array;  
}
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode PHP ( 搜尋比對字串 )"
MyCodeString = '''
###  PHP 搜尋比對字串 ####
if(strpos(  '今天天氣好' , '天氣' ) !== false )
{ 
    echo '包含'; 
}else
{
    echo '不包含'; 
}
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






