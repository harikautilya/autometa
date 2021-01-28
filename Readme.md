# Django admin automation
This project is used to handle simple automation for updating data using django admin. Run , go eat, sleep and forget.

# Usage
Start by creating the object with admin, username and password 
```
admin = AdminAutomate(admin_url=<url>, username=<admin_username>, password=<admin_password>)
```
# Funtionalities
 - Adding a object 
```
admin.add_model(app=<app_name>, table=<table_name>)
```
 - Modifying a object with id
```
admin.navigate_to_table_with_key(app=<app_name>, table=<table_name>, key=<id>)
```
 - Updating a column value
```
admin.write_to_column(column=<col_name>, value=<value_to_write>)
```