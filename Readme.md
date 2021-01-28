# Django admin automation
This project is used to handle simple automation for updating data using django admin. Run , go eat, sleep and forget.

# Setup
1. Install python (This is developed on 3.6 version)
2. ` pip install -r req.txt ` to install all requirments
3. Enable automation in safari

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
 - Find Element by col
```
admin.find_element_by_id(id=<col_name>)
```

# Pending 
 - Checkbox 
 - Spinner selection