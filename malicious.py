#command injection
eval(input("cmd? "))  
os.system(request.args.get('command'))

#SQLi
query = "SELECT * FROM users WHERE id = " + user_input

#hardcoded password
password = "secret123"

#path traversal
open("/var/www/" + filename)
