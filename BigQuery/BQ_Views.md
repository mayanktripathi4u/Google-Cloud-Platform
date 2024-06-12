# Authorized View
* Share query results with particular users and groups without giving them access to the underlying tables.
* Use the view's SQL query to restrict the columns (fields) the users are able to query.
* Source tables and view should be in different dataset.
* Grant necessary IAM roles to user at project and dataset level.
* Authorize view from source dataset.

# Demo
Step 1: Create a Dataset "primary_dataset".
Step 2: Create table(s) as the source. Say "my_primary_table"
Step 3: Create another Dataset "view_dataset".
Step 4: Create a View as "auth_view_demo" in this "view_dataset" dataset. [Refer](/GCP/BigQuery/authorized_view.sql)
Step 5: Assign the Role as "BigQuery User" to the Individual User or Group. 
Step 6: Navigate to dataset "view_dataset", and click on "Sharing" > "Permissions" > "ADD PRINCIPAL" for the same user as above step, assign Role as "BigQuery Data Viewer".
Step 7: Login with the user from Step 5.
Step 8: Navigate to primary dataset "primary_dataset", and click on "Sharing" > "Authorise Views" In the "Authorise view" type or select "auth_view_demo" which we created. > ADD AUTHORISATION.
Step 9: Ask the user to login and check.. the user should not be able to access the primary_dataset, but will be able to access the another dataset with the view.

