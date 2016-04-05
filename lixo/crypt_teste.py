import bcrypt

password = b"super secret password"

salt = bcrypt.gensalt(12)

hashed = bcrypt.hashpw(password, salt)

print hashed, salt

if bcrypt.hashpw(password, hashed) == hashed:
  print("It Matches!")
else:
  print("It Does not Match :(")
