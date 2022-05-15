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
* 

![ScreenShot](https://lh3.googleusercontent.com/d5kaSfuidTJIhLNlrf5e0CqM7J68DqSxTANW7vHR3BM-KSasDESVTd1GS-XL4APjZ5sSSDk1PO3au5galL-hAw86lEAEq6JVDFgAexfyGrPmwaqJK8HtwKDn6vgvaOfN0EfbJMPRu8_XLnwaRqEwd9WBvKBX5DxWP34xJPrZ8d73GFYDVx0Adayjr0VGSkPZKYEi88YBN31Sj6005U_4Piy_9q-m5oH6e4fPsHsuobJI3z7fMsxLkUR8WdxhOCIpfAPJun2qgy6PNJvxgvts80mqLMSAXOE5EcOuf0bt0gBLpQboGjaXfOMA42x2NrFiCoI-Isb2OrWa2c93Ps17TfmcYBPWjcxWSwLrHkgT7vPL3P1ztr_vUBDCTkwOC-njBCLa_mDsDoWKr6NLvu3IdoweEsZKa5aUq1IT_Cmcr_2_RHVAYS-nvecwN5KonFOVWyXFoXxkBvEn4rS8uZu1E9HNrZ9dDjnLgR8fDlGFwaQ_vmsPNoAgCM8ygFQW7FRLP5xVqjsBu_GpbigBmoG25m3E9nDbGV2ADNMWngeNUHHH9m6meVyzEqdqWnQBKqqk5yFS0KX0eZkfwVrpylCyI2xaZHx6JQaCRSMu2wkAe2wOAiP-MgBEvumtfQXvXgBK70NQulgqHe6AH8U37-1u5Em2rEiRSIK0QVgrYHtsRsLc2u0kUWlET-VdYuKrrKnOloO4plwthDjQbDEwxgoqWbRW7JJH9bYQQ8AUTdizF63FHZbtpuM3ppf2WxPXHE3lYSK5NDAbj2oMTWZO9OpPSpabiIEIQLQlqQ=w1289-h968-no?authuser=0)


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

