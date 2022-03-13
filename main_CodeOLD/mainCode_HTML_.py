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


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( HTML 播放器/ffmpeg 影片剪接 )"
MyCodeString = '''
<!-- ###  HTML 播放器 ### -->
<!-- file: mainCode_HTML_ -->
<meta http-equiv="X-UA-Compatible" content="IE=edge"> 


<video width="320" height="240" controls>
<source src="a1.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>


## ffmpeg 裁切 crop=1360:768:0:0  width:height:xx:yy /分割/Win7/ FPS -r 10 #####
ffmpeg -i Python-0921-1.mp4 -filter:v "crop=1360:768:0:0" -pix_fmt yuv420p -r 10 -c:a copy -movflags +faststart Python-0921-1.ok.mp4

## ffmpeg 轉檔 ##
ffmpeg -i input.m4v -f mp4 -c:v copy -c:a aac -b:a 384k -strict -2 output.mp4

## ffmpeg Win7 轉檔(有聲音)) ##
ffmpeg -i in.mp4 -pix_fmt yuv420p -c:a copy -movflags +faststart out.mp4
ffmpeg -i input.wmv -pix_fmt yuv420p -r 15 -acodec aac -strict experimental -ar 48000 -b:a 128k output.mp4

## ffmpeg 合併 ##
cat mylist.txt
file '1.mp4'
file '2.mp4'
ffmpeg -f concat -i mylist.txt -c copy output.mp4

## ffmpeg 分割 ##
ffmpeg -ss 00:00:16 -t 00:00:09 -i input.mp4 -c copy output.mp4

## ffmpeg to 640x360 ##
ffmpeg -i 00000.MTS.mp4 -vf scale=640:360 output_640.mp4 -hide_banner

## ffmpeg to mp3 ##
ffmpeg -i 'aaa.wma' -acodec libmp3lame -ab 192k 'bbb.mp3'
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( 基本格式 )"
MyCodeString = '''
###  HTML 標準範例 ####
<!-- file: mainCode_HTML_ -->

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<HTML xmlns="http://www.w3.org/1999/xhtml">
<HEAD>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<TITLE></TITLE>
<STYLE type="text/css">
</STYLE>
</HEAD>
<BODY>
</BODY>
</HTML> 
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( TOP 10 Table )"
MyCodeString = '''
###  HTML TOP 10 Table ####
<!-- file: mainCode_HTML_ -->

<style type="text/css">
body
{
	line-height: 1.6em;
}
#hor-minimalist-a
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	background: #fff;
	margin: 45px;
	width: 480px;
	border-collapse: collapse;
	text-align: left;
}
#hor-minimalist-a th
{
	font-size: 14px;
	font-weight: normal;
	color: #039;
	padding: 10px 8px;
	border-bottom: 2px solid #6678b1;
}
#hor-minimalist-a td
{
	color: #669;
	padding: 9px 8px 0px 8px;
}
#hor-minimalist-a tbody tr:hover td
{
	color: #009;
}


#hor-minimalist-b
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	background: #fff;
	margin: 45px;
	width: 480px;
	border-collapse: collapse;
	text-align: left;
}
#hor-minimalist-b th
{
	font-size: 14px;
	font-weight: normal;
	color: #039;
	padding: 10px 8px;
	border-bottom: 2px solid #6678b1;
}
#hor-minimalist-b td
{
	border-bottom: 1px solid #ccc;
	color: #669;
	padding: 6px 8px;
}
#hor-minimalist-b tbody tr:hover td
{
	color: #009;
}


#ver-minimalist
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
}
#ver-minimalist th
{
	padding: 8px 2px;
	font-weight: normal;
	font-size: 14px;
	border-bottom: 2px solid #6678b1;
	border-right: 30px solid #fff;
	border-left: 30px solid #fff;
	color: #039;
}
#ver-minimalist td
{
	padding: 12px 2px 0px 2px;
	border-right: 30px solid #fff;
	border-left: 30px solid #fff;
	color: #669;
}


#box-table-a
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
}
#box-table-a th
{
	font-size: 13px;
	font-weight: normal;
	padding: 8px;
	background: #b9c9fe;
	border-top: 4px solid #aabcfe;
	border-bottom: 1px solid #fff;
	color: #039;
}
#box-table-a td
{
	padding: 8px;
	background: #e8edff; 
	border-bottom: 1px solid #fff;
	color: #669;
	border-top: 1px solid transparent;
}
#box-table-a tr:hover td
{
	background: #d0dafd;
	color: #339;
}


#box-table-b
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: center;
	border-collapse: collapse;
	border-top: 7px solid #9baff1;
	border-bottom: 7px solid #9baff1;
}
#box-table-b th
{
	font-size: 13px;
	font-weight: normal;
	padding: 8px;
	background: #e8edff;
	border-right: 1px solid #9baff1;
	border-left: 1px solid #9baff1;
	color: #039;
}
#box-table-b td
{
	padding: 8px;
	background: #e8edff; 
	border-right: 1px solid #aabcfe;
	border-left: 1px solid #aabcfe;
	color: #669;
}


#hor-zebra
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
}
#hor-zebra th
{
	font-size: 14px;
	font-weight: normal;
	padding: 10px 8px;
	color: #039;
}
#hor-zebra td
{
	padding: 8px;
	color: #669;
}
#hor-zebra .odd
{
	background: #e8edff; 
}


#ver-zebra
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
}
#ver-zebra th
{
	font-size: 14px;
	font-weight: normal;
	padding: 12px 15px;
	border-right: 1px solid #fff;
	border-left: 1px solid #fff;
	color: #039;
}
#ver-zebra td
{
	padding: 8px 15px;
	border-right: 1px solid #fff;
	border-left: 1px solid #fff;
	color: #669;
}
.vzebra-odd
{
	background: #eff2ff;
}
.vzebra-even
{
	background: #e8edff;
}
#ver-zebra #vzebra-adventure, #ver-zebra #vzebra-children
{
	background: #d0dafd;
	border-bottom: 1px solid #c8d4fd;
}
#ver-zebra #vzebra-comedy, #ver-zebra #vzebra-action
{
	background: #dce4ff;
	border-bottom: 1px solid #d6dfff;
}


#one-column-emphasis
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
}
#one-column-emphasis th
{
	font-size: 14px;
	font-weight: normal;
	padding: 12px 15px;
	color: #039;
}
#one-column-emphasis td
{
	padding: 10px 15px;
	color: #669;
	border-top: 1px solid #e8edff;
}
.oce-first
{
	background: #d0dafd;
	border-right: 10px solid transparent;
	border-left: 10px solid transparent;
}
#one-column-emphasis tr:hover td
{
	color: #339;
	background: #eff2ff;
}


#newspaper-a
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
	border: 1px solid #69c;
}
#newspaper-a th
{
	padding: 12px 17px 12px 17px;
	font-weight: normal;
	font-size: 14px;
	color: #039;
	border-bottom: 1px dashed #69c;
}
#newspaper-a td
{
	padding: 7px 17px 7px 17px;
	color: #669;
}
#newspaper-a tbody tr:hover td
{
	color: #339;
	background: #d0dafd;
}


#newspaper-b
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
	border: 1px solid #69c;
}
#newspaper-b th
{
	padding: 15px 10px 10px 10px;
	font-weight: normal;
	font-size: 14px;
	color: #039;
}
#newspaper-b tbody
{
	background: #e8edff;
}
#newspaper-b td
{
	padding: 10px;
	color: #669;
	border-top: 1px dashed #fff;
}
#newspaper-b tbody tr:hover td
{
	color: #339;
	background: #d0dafd;
}


#newspaper-c
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
	border: 1px solid #6cf;
}
#newspaper-c th
{
	padding: 20px;
	font-weight: normal;
	font-size: 13px;
	color: #039;
	text-transform: uppercase;
	border-right: 1px solid #0865c2;
	border-top: 1px solid #0865c2;
	border-left: 1px solid #0865c2;
	border-bottom: 1px solid #fff;
}
#newspaper-c td
{
	padding: 10px 20px;
	color: #669;
	border-right: 1px dashed #6cf;
}


#rounded-corner
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
}
#rounded-corner thead th.rounded-company
{
	background: #b9c9fe url('table-images/left.png') left -1px no-repeat;
}
#rounded-corner thead th.rounded-q4
{
	background: #b9c9fe url('table-images/right.png') right -1px no-repeat;
}
#rounded-corner th
{
	padding: 8px;
	font-weight: normal;
	font-size: 13px;
	color: #039;
	background: #b9c9fe;
}
#rounded-corner td
{
	padding: 8px;
	background: #e8edff;
	border-top: 1px solid #fff;
	color: #669;
}
#rounded-corner tfoot td.rounded-foot-left
{
	background: #e8edff url('table-images/botleft.png') left bottom no-repeat;
}
#rounded-corner tfoot td.rounded-foot-right
{
	background: #e8edff url('table-images/botright.png') right bottom no-repeat;
}
#rounded-corner tbody tr:hover td
{
	background: #d0dafd;
}


#background-image
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
	background: url('table-images/blurry.jpg') 330px 59px no-repeat;
}
#background-image th
{
	padding: 12px;
	font-weight: normal;
	font-size: 14px;
	color: #339;
}
#background-image td
{
	padding: 9px 12px;
	color: #669;
	border-top: 1px solid #fff;
}
#background-image tfoot td
{
	font-size: 11px;
}
#background-image tbody td
{
	background: url('table-images/back.png');
}
* html #background-image tbody td
{
	/* 
	   ----------------------------
		PUT THIS ON IE6 ONLY STYLE 
		AS THE RULE INVALIDATES
		YOUR STYLESHEET
	   ----------------------------
	*/
	filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='table-images/back.png',sizingMethod='crop');
	background: none;
}	
#background-image tbody tr:hover td
{
	color: #339;
	background: none;
}


#gradient-style
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
}
#gradient-style th
{
	font-size: 13px;
	font-weight: normal;
	padding: 8px;
	background: #b9c9fe url('table-images/gradhead.png') repeat-x;
	border-top: 2px solid #d3ddff;
	border-bottom: 1px solid #fff;
	color: #039;
}
#gradient-style td
{
	padding: 8px; 
	border-bottom: 1px solid #fff;
	color: #669;
	border-top: 1px solid #fff;
	background: #e8edff url('table-images/gradback.png') repeat-x;
}
#gradient-style tfoot tr td
{
	background: #e8edff;
	font-size: 12px;
	color: #99c;
}
#gradient-style tbody tr:hover td
{
	background: #d0dafd url('table-images/gradhover.png') repeat-x;
	color: #339;
}


#pattern-style-a
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
	background: url('table-images/pattern.png');
}
#pattern-style-a thead tr
{
	background: url('table-images/pattern-head.png');
}
#pattern-style-a th
{
	font-size: 13px;
	font-weight: normal;
	padding: 8px;
	border-bottom: 1px solid #fff;
	color: #039;
}
#pattern-style-a td
{
	padding: 8px; 
	border-bottom: 1px solid #fff;
	color: #669;
	border-top: 1px solid transparent;
}
#pattern-style-a tbody tr:hover td
{
	color: #339;
	background: #fff;
}


#pattern-style-b
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	margin: 45px;
	width: 480px;
	text-align: left;
	border-collapse: collapse;
	background: url('table-images/patternb.png');
}
#pattern-style-b thead tr
{
	background: url('table-images/patternb-head.png');
}
#pattern-style-b th
{
	font-size: 13px;
	font-weight: normal;
	padding: 8px;
	border-bottom: 1px solid #fff;
	color: #039;
}
#pattern-style-b td
{
	padding: 8px; 
	border-bottom: 1px solid #fff;
	color: #669;
	border-top: 1px solid transparent;
}
#pattern-style-b tbody tr:hover td
{
	color: #339;
	background: #cdcdee;
}
</style>


</head>
<body>
<table id="hor-minimalist-a" summary="Employee Pay Sheet">
    <thead>
    	<tr>
        	<th scope="col">Employee</th>
            <th scope="col">Salary</th>
            <th scope="col">Bonus</th>
            <th scope="col">Supervisor</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Stephen C. Cox</td>
            <td>$300</td>
            <td>$50</td>
            <td>Bob</td>
        </tr>
        <tr>
        	<td>Josephin Tan</td>
            <td>$150</td>
            <td>-</td>
            <td>Annie</td>
        </tr>
        <tr>
        	<td>Joyce Ming</td>
            <td>$200</td>
            <td>$35</td>
            <td>Andy</td>
        </tr>
        <tr>
        	<td>James A. Pentel</td>
            <td>$175</td>
            <td>$25</td>
            <td>Annie</td>
        </tr>
    </tbody>
</table>

<table id="hor-minimalist-b" summary="Employee Pay Sheet">
    <thead>
    	<tr>
        	<th scope="col">Employee</th>
            <th scope="col">Salary</th>
            <th scope="col">Bonus</th>
            <th scope="col">Supervisor</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Stephen C. Cox</td>
            <td>$300</td>
            <td>$50</td>
            <td>Bob</td>
        </tr>
        <tr>
        	<td>Josephin Tan</td>
            <td>$150</td>
            <td>-</td>
            <td>Annie</td>
        </tr>
        <tr>
        	<td>Joyce Ming</td>
            <td>$200</td>
            <td>$35</td>
            <td>Andy</td>
        </tr>
        <tr>
        	<td>James A. Pentel</td>
            <td>$175</td>
            <td>$25</td>
            <td>Annie</td>
        </tr>
    </tbody>
</table>


<table id="ver-minimalist" summary="Most Favorite Movies">
    <thead>
    	<tr>
        	<th scope="col">Comedy</th>
            <th scope="col">Adventure</th>
            <th scope="col">Action</th>
            <th scope="col">Children</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Scary Movie</td>
            <td>Indiana Jones</td>
            <td>The Punisher</td>
            <td>Wall-E</td>
        </tr>
        <tr>
        	<td>Epic Movie</td>
            <td>Star Wars</td>
            <td>Bad Boys</td>
            <td>Madagascar</td>
        </tr>
        <tr>
        	<td>Spartan</td>
            <td>LOTR</td>
            <td>Die Hard</td>
            <td>Finding Nemo</td>
        </tr>
        <tr>
        	<td>Dr. Dolittle</td>
            <td>The Mummy</td>
            <td>300</td>
            <td>A Bug's Life</td>
        </tr>
    </tbody>
</table>

<table id="box-table-a" summary="Employee Pay Sheet">
    <thead>
    	<tr>
        	<th scope="col">Employee</th>
            <th scope="col">Salary</th>
            <th scope="col">Bonus</th>
            <th scope="col">Supervisor</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Stephen C. Cox</td>
            <td>$300</td>
            <td>$50</td>
            <td>Bob</td>
        </tr>
        <tr>
        	<td>Josephin Tan</td>
            <td>$150</td>
            <td>-</td>
            <td>Annie</td>
        </tr>
        <tr>
        	<td>Joyce Ming</td>
            <td>$200</td>
            <td>$35</td>
            <td>Andy</td>
        </tr>
        <tr>
        	<td>James A. Pentel</td>
            <td>$175</td>
            <td>$25</td>
            <td>Annie</td>
        </tr>
    </tbody>
</table>


<table id="box-table-b" summary="Most Favorit Movies">
    <thead>
    	<tr>
        	<th scope="col">Comedy</th>
            <th scope="col">Adventure</th>
            <th scope="col">Action</th>
            <th scope="col">Children</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Scary Movie</td>
            <td>Indiana Jones</td>
            <td>The Punisher</td>
            <td>Wall-E</td>
        </tr>
        <tr>
        	<td>Epic Movie</td>
            <td>Star Wars</td>
            <td>Bad Boys</td>
            <td>Madagascar</td>
        </tr>
        <tr>
        	<td>Spartan</td>
            <td>LOTR</td>
            <td>Die Hard</td>
            <td>Finding Nemo</td>
        </tr>
        <tr>
        	<td>Dr. Dolittle</td>
            <td>The Mummy</td>
            <td>300</td>
            <td>A Bug's Life</td>
        </tr>
    </tbody>
</table>


<table id="hor-zebra" summary="Employee Pay Sheet">
    <thead>
    	<tr>
        	<th scope="col">Employee</th>
            <th scope="col">Salary</th>
            <th scope="col">Bonus</th>
            <th scope="col">Supervisor</th>
        </tr>
    </thead>
    <tbody>
    	<tr class="odd">
        	<td>Stephen C. Cox</td>
            <td>$300</td>
            <td>$50</td>
            <td>Bob</td>
        </tr>
        <tr>
        	<td>Josephin Tan</td>
            <td>$150</td>
            <td>-</td>
            <td>Annie</td>
        </tr>
        <tr class="odd">
        	<td>Joyce Ming</td>
            <td>$200</td>
            <td>$35</td>
            <td>Andy</td>
        </tr>
        <tr>
        	<td>James A. Pentel</td>
            <td>$175</td>
            <td>$25</td>
            <td>Annie</td>
        </tr>
    </tbody>
</table>


<table id="ver-zebra" summary="Most Favorite Movies">
    <colgroup>
    	<col class="vzebra-odd" />
    	<col class="vzebra-even" />
    	<col class="vzebra-odd" />
        <col class="vzebra-even" />
    </colgroup>
    <thead>
    	<tr>
        	<th scope="col" id="vzebra-comedy">Comedy</th>
            <th scope="col" id="vzebra-adventure">Adventure</th>
            <th scope="col" id="vzebra-action">Action</th>
            <th scope="col" id="vzebra-children">Children</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Scary Movie</td>
            <td>Indiana Jones</td>
            <td>The Punisher</td>
            <td>Wall-E</td>
        </tr>
        <tr>
        	<td>Epic Movie</td>
            <td>Star Wars</td>
            <td>Bad Boys</td>
            <td>Madagascar</td>
        </tr>
        <tr>
        	<td>Spartan</td>
            <td>LOTR</td>
            <td>Die Hard</td>
            <td>Finding Nemo</td>
        </tr>
        <tr>
        	<td>Dr. Dolittle</td>
            <td>The Mummy</td>
            <td>300</td>
            <td>A Bug's Life</td>
        </tr>
    </tbody>
</table>

<table id="one-column-emphasis" summary="2007 Major IT Companies' Profit">
    <colgroup>
    	<col class="oce-first" />
    </colgroup>
    <thead>
    	<tr>
        	<th scope="col">Company</th>
            <th scope="col">Q1</th>
            <th scope="col">Q2</th>
            <th scope="col">Q3</th>
            <th scope="col">Q4</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Microsoft</td>
            <td>20.3</td>
            <td>30.5</td>
            <td>23.5</td>
            <td>40.3</td>
        </tr>
        <tr>
        	<td>Google</td>
            <td>50.2</td>
            <td>40.63</td>
            <td>45.23</td>
            <td>39.3</td>
        </tr>
        <tr>
        	<td>Apple</td>
            <td>25.4</td>
            <td>30.2</td>
            <td>33.3</td>
            <td>36.7</td>
        </tr>
        <tr>
        	<td>IBM</td>
            <td>20.4</td>
            <td>15.6</td>
            <td>22.3</td>
            <td>29.3</td>
        </tr>
    </tbody>
</table>


<table id="newspaper-a" summary="2007 Major IT Companies' Profit">
    <thead>
    	<tr>
        	<th scope="col">Company</th>
            <th scope="col">Q1</th>
            <th scope="col">Q2</th>
            <th scope="col">Q3</th>
            <th scope="col">Q4</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Microsoft</td>
            <td>20.3</td>
            <td>30.5</td>
            <td>23.5</td>
            <td>40.3</td>
        </tr>
        <tr>
        	<td>Google</td>
            <td>50.2</td>
            <td>40.63</td>
            <td>45.23</td>
            <td>39.3</td>
        </tr>
        <tr>
        	<td>Apple</td>
            <td>25.4</td>
            <td>30.2</td>
            <td>33.3</td>
            <td>36.7</td>
        </tr>
        <tr>
        	<td>IBM</td>
            <td>20.4</td>
            <td>15.6</td>
            <td>22.3</td>
            <td>29.3</td>
        </tr>
    </tbody>
</table>


<table id="newspaper-b" summary="2007 Major IT Companies' Profit">
    <thead>
    	<tr>
        	<th scope="col">Company</th>
            <th scope="col">Q1</th>
            <th scope="col">Q2</th>
            <th scope="col">Q3</th>
            <th scope="col">Q4</th>
        </tr>
    </thead>
        <tfoot>
    	<tr>
        	<td colspan="5"><em>The above data were fictional and made up, please do not sue me</em></td>
        </tr>
    </tfoot>
    <tbody>
    	<tr>
        	<td>Microsoft</td>
            <td>20.3</td>
            <td>30.5</td>
            <td>23.5</td>
            <td>40.3</td>
        </tr>
        <tr>
        	<td>Google</td>
            <td>50.2</td>
            <td>40.63</td>
            <td>45.23</td>
            <td>39.3</td>
        </tr>
        <tr>
        	<td>Apple</td>
            <td>25.4</td>
            <td>30.2</td>
            <td>33.3</td>
            <td>36.7</td>
        </tr>
        <tr>
        	<td>IBM</td>
            <td>20.4</td>
            <td>15.6</td>
            <td>22.3</td>
            <td>29.3</td>
        </tr>
    </tbody>
</table>

<table id="newspaper-c" summary="Personal Movie Rating">
    <thead>
    	<tr>
        	<th scope="col">Favorite</th>
            <th scope="col">Great</th>
            <th scope="col">Nice</th>
            <th scope="col">Bad</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Passion of the Christ</td>
            <td>Bourne Ultimatum</td>
            <td>Shoot 'Em Up</td>
            <td>Ali</td>
        </tr>
        <tr>
        	<td>The Big Fish</td>
            <td>The Mummy</td>
            <td>Apocalypto</td>
            <td>Monster</td>
        </tr>
        <tr>
        	<td>Shawshank Redemption</td>
            <td>Cold Mountain</td>
            <td>Indiana Jones</td>
            <td>Dead or Alive</td>
        </tr>
        <tr>
        	<td>Greatest Story Ever Told</td>
            <td>I Am Legend</td>
            <td>Star Wars</td>
            <td>Saw 3</td>
        </tr>
    </tbody>
</table>


<table id="rounded-corner" summary="2007 Major IT Companies' Profit">
    <thead>
    	<tr>
        	<th scope="col" class="rounded-company">Company</th>
            <th scope="col" class="rounded-q1">Q1</th>
            <th scope="col" class="rounded-q2">Q2</th>
            <th scope="col" class="rounded-q3">Q3</th>
            <th scope="col" class="rounded-q4">Q4</th>
        </tr>
    </thead>
        <tfoot>
    	<tr>
        	<td colspan="4" class="rounded-foot-left"><em>The above data were fictional and made up, please do not sue me</em></td>
        	<td class="rounded-foot-right">&nbsp;</td>
        </tr>
    </tfoot>
    <tbody>
    	<tr>
        	<td>Microsoft</td>
            <td>20.3</td>
            <td>30.5</td>
            <td>23.5</td>
            <td>40.3</td>
        </tr>
        <tr>
        	<td>Google</td>
            <td>50.2</td>
            <td>40.63</td>
            <td>45.23</td>
            <td>39.3</td>
        </tr>
        <tr>
        	<td>Apple</td>
            <td>25.4</td>
            <td>30.2</td>
            <td>33.3</td>
            <td>36.7</td>
        </tr>
        <tr>
        	<td>IBM</td>
            <td>20.4</td>
            <td>15.6</td>
            <td>22.3</td>
            <td>29.3</td>
        </tr>
    </tbody>
</table>

<table id="background-image" summary="Meeting Results">
    <thead>
    	<tr>
        	<th scope="col">Employee</th>
            <th scope="col">Division</th>
            <th scope="col">Suggestions</th>
        </tr>
    </thead>
    <tfoot>
    	<tr>
        	<td colspan="4">IE 6 users won't see the transparent background if the hack is not applied</td>
        </tr>
    </tfoot>
    <tbody>
    	<tr>
        	<td>Stephen C. Cox</td>
            <td>Marketing</td>
            <td>Make discount offers</td>
        </tr>
        <tr>
        	<td>Josephin Tan</td>
            <td>Advertising</td>
            <td>Give bonuses</td>
        </tr>
        <tr>
        	<td>Joyce Ming</td>
            <td>Marketing</td>
            <td>New designs</td>
        </tr>
        <tr>
        	<td>James A. Pentel</td>
            <td>Marketing</td>
            <td>Better Packaging</td>
        </tr>
    </tbody>
</table>


<table id="gradient-style" summary="Meeting Results">
    <thead>
    	<tr>
        	<th scope="col">Employee</th>
            <th scope="col">Division</th>
            <th scope="col">Suggestions</th>
            <th scope="col">Rating</th>
        </tr>
    </thead>
    <tfoot>
    	<tr>
        	<td colspan="4">Give background color to the table cells to achieve seamless transition</td>
        </tr>
    </tfoot>
    <tbody>
    	<tr>
        	<td>Stephen C. Cox</td>
            <td>Marketing</td>
            <td>Make discount offers</td>
            <td>3/10</td>
        </tr>
        <tr>
        	<td>Josephin Tan</td>
            <td>Advertising</td>
            <td>Give bonuses</td>
        	<td>5/10</td>
        </tr>
        <tr>
        	<td>Joyce Ming</td>
            <td>Marketing</td>
            <td>New designs</td>
        	<td>8/10</td>
        </tr>
        <tr>
        	<td>James A. Pentel</td>
            <td>Marketing</td>
            <td>Better Packaging</td>
            <td>8/10</td>
        </tr>
    </tbody>
</table>


<table id="pattern-style-a" summary="Meeting Results">
   <thead>
    	<tr>
        	<th scope="col">Employee</th>
            <th scope="col">Salary</th>
            <th scope="col">Bonus</th>
            <th scope="col">Supervisor</th>
        </tr>
  </thead>
    <tbody>
    	<tr>
        	<td>Stephen C. Cox</td>
            <td>$300</td>
            <td>$50</td>
            <td>Bob</td>
        </tr>
        <tr>
        	<td>Josephin Tan</td>
            <td>$150</td>
            <td>-</td>
            <td>Annie</td>
        </tr>
        <tr>
        	<td>Joyce Ming</td>
            <td>$200</td>
            <td>$35</td>
            <td>Andy</td>
        </tr>
        <tr>
        	<td>James A. Pentel</td>
            <td>$175</td>
            <td>$25</td>
            <td>Annie</td>
        </tr>
    </tbody>
</table>

<table id="pattern-style-b" summary="Meeting Results">
    <thead>
    	<tr>
        	<th scope="col">Nation</th>
            <th scope="col">Capital</th>
            <th scope="col">Language</th>
            <th scope="col">Unique</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>Japan</td>
            <td>Tokyo</td>
            <td>Japanese</td>
            <td>Karate</td>
        </tr>
        <tr>
        	<td>South Korea</td>
            <td>Seoul</td>
            <td>Korean</td>
            <td>Ginseng</td>
        </tr>
        <tr>
        	<td>China</td>
            <td>Beijing</td>
            <td>Mandarin</td>
            <td>Kung-Fu</td>
        </tr>
        <tr>
        	<td>Indonesia</td>
            <td>Jakarta</td>
            <td>Indonesian</td>
            <td>Batik</td>
        </tr>
    </tbody>
</table>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)

### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( CSS範例 )"
MyCodeString = '''
<!-- file: mainCode_HTML_ -->
<style type="text/css">
#myId
{
    /* position: relative (相對定位) / absolute (絕對定位) / fixed (浮動定位) / static (靜態定位-預設) */
    position:absolute;
    top:     50px;
    left:    50px;
    z-index: 10;    
	
    font-family: "Microsoft JhengHei","微軟正黑體","Lucida Sans Unicode";
	font-size: 12px;
	background: #fff;
	

    font-weight: normal;
    font-weight: bold;

    margin: 15px;
    padding: 0px 0px 0px 0px;

	width:  480px;
    height: 300px;
	border-collapse: collapse;

	text-align: left;
    vertical-align: middle;

    overflow: auto;      /* 預設會自動使用捲軸 */
    overflow: visible;   /* 顯示的文字或圖片會直接超出範圍，不使用捲軸。*/
    overflow: hidden;    /* 自動隱藏超出的文字或圖片。*/
    overflow: scroll;    /* 自動產生捲軸。*/
    overflow: inherit;   /* 繼承自父元素的可見性*/

    border-style: dashed;
    border-style: dotted dashed solid double;
    border-style: dotted;
    border-style: double;
    border-style: groove;
    border-style: hidden;
    border-style: inset;
    border-style: none;
    border-style: outset;
    border-style: ridge;
    border-style: solid;

    cursor: crosshair;     /*十字線型*/
    cursor: cell;          /*十字小方格 Firefox, Opera*/
    cursor: move;          /*十字箭頭(移動)*/
    cursor: all-scroll;    /*四方捲動*/
    cursor: n-resize;      /*箭頭朝上*/
    cursor: s-resize;      /*箭頭朝下*/
    cursor: e-resize;      /*箭頭朝右*/
    cursor: w-resize;      /*箭頭朝左*/
    cursor: nw-resize;     /*箭頭左上*/
    cursor: sw-resize;     /*箭頭左下*/
    cursor: se-resize;     /*箭頭朝右上*/
    cursor: ne-resize;     /*箭頭朝右下*/
    cursor: col-resize;    /*改變直行數*/
    cursor: row-resize;    /*改變橫欄數*/
    cursor: text;          /*I 輸入文字符號*/
    cursor: vertical-text; /*垂直文字*/
    cursor: help;          /*協助加一問號*/
    cursor: wait;          /*等待中；漏斗*/
    cursor: progress;      /*進行中；作業中*/
    cursor: pointer;       /*手型，表示超連結*/
    cursor: not-allowed;   /*無法使用*/
    cursor: context-menu;  /*選單 Opera*/

}
</style>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( Form表單 )"
MyCodeString = '''
<!-- file: mainCode_HTML_ -->
<form action="test.php" method="post" target="my_iframe">

    姓名：<input type="text" name="UserName">   <br>
    內容：<textarea name="Content"></textarea>  <br>

    <!-- Checkboxes -->
    <input type="checkbox" checked="checked"> <label>Milk  </label>           <br>    
    <input type="checkbox">                   <label>Sugar </label>           <br>
    <input type="checkbox" disabled>          <label>Lemon (Disabled)</label> <br>
    

    <!-- radio -->
    <input type="radio" name="gender" value="male" checked>  <label>Male</label>
    <input type="radio" name="gender" value="female">        <label>Female</label>
    <input type="radio" name="gender" value="" disabled>     <label>Don't know (Disabled)</label> 

    <br>
    <input type="submit" value="送出表單">

</form>

<!-- 隱藏的 iframe -->
<iframe name="my_iframe" src="test2.php" style='display:none;' scrolling='no' frameborder=0 ></iframe>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( 表格合併 )"
MyCodeString = '''
<!-- file: mainCode_HTML_ -->
<table>
	<tbody>
		<tr>
			<td colspan="2">水平合併</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>

<table>
	<tbody>
		<tr>
			<td rowspan="2">垂直合併</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( CSS 畫面滾動 position 定位 )"
MyCodeString = '''
<!-- HTML CSS 畫面滾動 position 定位 -->
<!-- file: mainCode_HTML_ -->

<div id="fiexd-header">
    <h1>test</h1>
</div>
<style>
#fiexd-header{
  position:fixed;
  top:  10;
  left: 10;
  z-index:100;
  background:#66CCCC;
  color:#FFFFFF;
  border-top:2px solid #336699;
  border-bottom:2px solid #336699;
  width:100%;

  /* CSS Hack：寫一些讓某種瀏覽器看得懂、某種瀏覽器看不懂的 CSS 語法 */
  _position:absolute;  /* position fixed for IE6 */
  _top:expression(documentElement.scrollTop+"px");
}

</style>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode HTML ( 各種瀏覽器 CSS )"
MyCodeString = '''
<!-- HTML 各種瀏覽器 CSS -->
<!-- file: mainCode_HTML_ -->

<style type="text/css"> 
/* Chrome 29+	 */
@media screen and (-webkit-min-device-pixel-ratio:0) and (min-resolution:.001dpcm) {
    #css-test
    {
        color:blue;
    }
}

/* IE 10 and above */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
    #css-test
    {
        color:blue;
    }
}

/* IE 11 (and above..) */
_:-ms-fullscreen, :root 
#css-test
{
    color:blue;
}

/* Firefox */
@supports (-moz-appearance:none) {
    #css-test
    {
        color:blue;
    }
}
</style>

<font id="css-test">1234</font>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode HTML ( 範例 )"
# MyCodeString = '''
# ###  Python 帶入參數 ####
# <!-- file: mainCode_HTML_ -->
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode HTML ( 範例 )"
# MyCodeString = '''
# ###  Python 帶入參數 ####
# <!-- file: mainCode_HTML_ -->
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)






##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
