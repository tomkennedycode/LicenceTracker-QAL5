# LicenceTracker-QAL5

**To run this project please clone the repository and follow the below commands:**
1. Set up the virtual environment on your chosen IDE - please ensure you have python installed on your machine.
2. Navigate to the root of the project inside a terminal window and run the following commands
3. .venv\Scripts\activate
4. Set up postgres database and update your database details in LicenceTracker/settings.py
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
8. Install any packages that it may prompt you to.

**To set up a superuser:**
1. Enter your virutal environment like the the previous step 3.
2. python manage.py createsuperuser
3. Follow the steps that it presents in the terminal
4. Log in using that created superuser and create other accounts

**To upload/update a licence:**
1. Once logged in, if you have an admin account, you can use the admin portal or you can click on the top right where it says 'View Site'.
2. Normal users have access in the admin portal to view certain data but to edit and upload, please navigate to 'View Site'.
3. From there you can view all licences on the home screen and click edit, or if you want to create a new licence, click Upload Licence on the navigation bar

**To run automated test cases**
1. Configure into your virtual python environment like in the steps above
2. Run the following command - python manage.py test

## If you want to access the hosted site at https://licence-tracker.herokuapp.com/ please see log in details in the written assignment.

## If you encounter any issue, please contact me at tom.kennedy@bp.com or tom.kennedy017@gmail.com
