# DURT.ME
This web app has been developed using the popular Django framework and Bootstrap for the frontend. My motivation to build this project is so that I can learn about Django and tighten up my skills. This mini-app can be easily integrated into a bigger system project that needs to have a registration and login system.

### Basic Features of The App
    
* Register – Users can register and create a new profile
* Login - Registered users can login using username and password
* Social Apps Login – Users can login using their GitHub or Google account
* User Profile - Once logged in, users can create and update additional information such as avatar and bio in the profile page
* Update Profile – Users can update their information such as username, email, password, avatar and bio
* Remember me – Cookie Option, users don’t have to provide credentials every time they hit the site
* Forgot Password – Users can easily retrieve their password if they forget it 
* Admin Panel – admin can CRUD users
* Create Shortened link
* Logged in users can edit already created shortened links.
* Logged in users can see analytics such as number of vists, time of click and location of visit on shortened links.

![ScreenShot](./users/static/images/image.png)


### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
2. Create a .env file and set the following;
    - EMAIL_HOST_USER=
    - EMAIL_HOST_PASSWORD=
    - EMAIL_USER_DEFAULT=

    - GITHUB_KEY=
    - GITHUB_SECRET=

    - GOOGLE_KEY=
    - GOOGLE_SECRET=

    - DEBUG=True

    - DJANGO_ALLOWED_HOSTS=127.0.0.1

    - DJANGO_DEVELOPMENT=dev

    - DURT_DB_NAME=
    - DURT_DB_USER=
    - DURT_DB_PASSWORD=
    - DURT_DB_HOST=
    - DURT_DB_PORT=
    
    Set ```DJANGO_DEVELOPMENT``` TO 'dev' for development or to 'prod' for deployment to production.

    Set ```DEBUG``` TO 'True' for development or to 'False' for deployment to production.

3. Run the following commands
    * pip install -r requirements.txt
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser
    * python manage.py runserver
   
4. Open a browser and go to http://localhost:8000/

