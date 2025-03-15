

def func(secret):

    if "\"" in secret:
        return "WAFed"

    query = "UPDATE secrets SET secret = '" + secret + "' WHERE username = 'username';"

    return query


def get_secret(username):
    secret = db.fetch_one("SELECT secret FROM secrets WHERE username = %s", (username,))
    if secret is None:
        return "user does not exist"
    else:
        return secret["secret"]

secret = "\' || "
print(func(secret))