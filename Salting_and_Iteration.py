import hashlib
temp_pass = hashlib.sha512("bibhu".encode("UTF-8")).hexdigest()
print( temp_pass )
for i in range(5):
  password = hashlib.sha512(temp_pass.encode("UTF-8")).hexdigest()
  print(password)
  temp_pass = password