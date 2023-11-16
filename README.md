# VPN service
Web application based on Django according to technical specifications

## Description
The application can be run in 2 ways, using Docker or locally, but to do this you will need to create a database.
The application implements authentication and authorization, a service for creating websites according to technical specifications, 
the ability to go to a website, changing legal addresses, the ability to edit a user profile, basic dashboard functionality, 
the visual part is implemented using Bootstrap templates

---
## Installation
**1. Clone the repository:**

   ```shell
   git clone https://github.com/AlexGrig23/vpn-service-Django.git
   ```


  Create virtual env.

   ```shell
   python -m venv venv
   ```

**2. Create a `.env` file based on the `.env.example` file:**

   ```shell
   cd vpn_service
   ```

   ```shell
   cp .env.example .env
   ```
**3. If you want to run using Docker you must have a Docker desktop**
  
   ```shell
   docker compose build --no-cache
   ```
   
   After that, you must run next command, It builds the images if they are not located locally and starts the containers:

   ```shell
   docker compose up
   ```
   Starting development server at  http://127.0.1:8000/
  
	
**4 If you want to run locally without using docker**

   ```shell
   pip install -r requirements.txt
   ```
**5 You also need to create a PostgreSQL database and enter the credentials in the .env file.
 Additionally, you should update the 'HOST' in the Settings file (vpn_service/settings.py) to match your configuration.**

  ```shell
   cd vnv_test (root)
   ```

  ```shell
   python manage.py makemigrations
   ```

  ```shell
   python manage.py migrate
   ```

  ```shell
   python manage.py runserver
   ```
  Starting development server at  http://127.0.1:8000/


