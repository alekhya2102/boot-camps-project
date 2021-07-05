#string to md5
import hashlib
str2hash = input('enter the string:')
result = hashlib.md5(str2hash.encode())
# printing the equivalent of byte and hexadecimal value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
print("The hexadecimal equivalent of hash is:",end="")
print(result.hexdigest())
#hash algorithms.
import hashlib
str =input('enter the string:')
result = hashlib.sha256(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
print ("\r")
str = input('enter the string:')
result = hashlib.sha384(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
print ("\r")
str = input('enter the string:')
result = hashlib.sha224(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
print ("\r")
str = input('enter the string:')
result = hashlib.sha512(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
print ("\r")
str = input('enter the string:')
result = hashlib.sha1(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
