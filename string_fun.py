#string play
#string interpolation 
stri1 = str(98.6)
stir2 = str(1.0e4)
stri3 = str(True)

print(str(98.6) + "," + str(1.0e4) + "," +  str(True) + "\n")

#string methods 
name = 'Henny' 
name.replace('H','P')
print(name + " after the use of the replace method\n")
#slice method/syntax to replace back to the 'P'
'P' + name[1:]
print(name + " after slice\n")

letters = 'abcdefghijklmnopqrstuvwxyz'
temp = letters[:]
print(temp + ": letters[:]\n" ) 

temp = letters[20:]
print(temp + ": letters[20:]\n" ) 

temp = letters[10:]
print(temp + ": letters[10:]\n" )

temp = letters[12:15]
print(temp + ": letters[12:15]\n" )

temp = letters[-3:]
print(temp + ": letters[-3:]\n" )

temp = letters[18:-3]
print(temp + ": letters[18:-3]\n" )

temp = letters[-6:-2]
print(temp + ": letters[-6:-2]\n" )

temp = letters[::7]
print(temp + ": letters[::7]\n" )

temp = letters[4:20:3]
print(temp + ": letters[4:20:3]\n" )

temp = letters[19::4]
print(temp + ": letters[19::4]\n" )

temp = letters[:21:5]
print(temp + ": letters[:21:5]\n" )

temp = letters[-1::-1]
print(temp + ": letters[-1::-1]\n" )

temp = letters[::-1]
print(temp + ": letters[::-1]\n" )

temp = letters[-50:]
print(temp + ": letters[-50:]\n" )

temp = letters[-51:-50]
print(temp + ": letters[::-1]\n" )

temp = letters[:70]
print(temp + ": letters[:70]\n" )

temp = letters[70:71]
print(temp + ": letters[70:71]\n" )