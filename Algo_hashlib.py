import hashlib

def returnHashMD5(a):
  return hashlib.md5(a.encode("UTF-8")).hexdigest()

def returnHashSHA256(a):
  return hashlib.sha256(a.encode("UTF-8")).hexdigest()

def returnHashSHA512(a):
  return hashlib.sha512(a.encode("UTF-8")).hexdigest()

password = returnHashMD5("ShapeAI")
print(password)

password = returnHashSHA256("ShapeAI")
print(password)

password = returnHashSHA512("ShapeAI")
print(password)