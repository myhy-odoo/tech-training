from xmlrpc import client

url = "https://myhy-odoo-tech-training-15-0-dev-academy-4434885.dev.odoo.com"
db = "myhy-odoo-tech-training-15-0-dev-academy-4434885"
username = "admin"
password = "admin"

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db,username,password,{})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db,uid,password,"sale.order","check_access_rights",["write"],{"raise Exception": False})
print(model_access)

draft_quotes = models.execute_kw(db,uid,password, "sale.order","search",[[["state","=","draft"]]])
print(draft_quotes)