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
MyCodeTitle  = "RyanCode ES6 ( class test )"
MyCodeString = '''
###  Python ES6 class test ####
### file: mainCode_ES6

// ### ES5 #####################################################
function Person (name,age){
    this.name = name
    this.age = age
}

Person.prototype.sayHi = function(){
    console.log(`Hi I am ${this.name} , I am ${this.age} years old`)
}
var Mary = new Person( "Mary NN" , "46")

Mary.sayHi()
console.log(Mary)

// ### ES6 #####################################################
class Person{
    constructor(name,age){
        this.name = name;
        this.age = age;
    }

    sayHi(){
        console.log(`I am ${this.name} , I am ${this.age} years old`)
    }
}

class Boy extends Person{
    onlyBoy(){
        console.log(`${this.name} is boy`)
    }
}

var f = new Boy("Danny", "30")

// super 範例
class BoyNew extends Person{
    constructor(name, age, gender){
        super(name, age)
        this.gender = gender
    }
}
var g = new BoyNew("Peter" , "20", "male")
console.log(g)

// ########################################################

class Square{
    constructor(width){
        this.width = width
        this.hegit = width
    }

    get area(){
        return this.width * this.height
    }
}

let Square1 = new Square(5)
console.log(Square1)

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode ES6 ( 範例 )"
# MyCodeString = '''
# ###  Python ES6 ####
# ### file: mainCode_ES6
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode ES6 ( 範例 )"
# MyCodeString = '''
# ###  Python ES6 ####
# ### file: mainCode_ES6
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode ES6 ( 範例 )"
# MyCodeString = '''
# ###  Python ES6 ####
# ### file: mainCode_ES6
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode ES6 ( 範例 )"
# MyCodeString = '''
# ###  Python ES6 ####
# ### file: mainCode_ES6
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode ES6 ( 範例 )"
# MyCodeString = '''
# ###  Python ES6 ####
# ### file: mainCode_ES6
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)











##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
