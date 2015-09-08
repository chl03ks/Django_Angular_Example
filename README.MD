# Instructional Assessment

1. Clone the repo
2. Set up your virtual enviroment using either Virtualenv or Virtual Wrapper
3. Install requirements:

    ```bash
    $ pip install -r requirements.txt
    ```

4. Run migrations
    - Production environment with postgress database:

    ```bash
    $ python manage.py migrate
    ```

4. Load the fixture with admin user (username: admin, password: admin):

    ```bash
    $ python manage.py loaddata assesment/fixtures/create_superuser.json
    ```
    Optional
     ```bash
    $ python manage.py loaddata assesment/fixtures/inital_data.json
     ```
5. Run Server

    ```bash
    $ python manage.py runserver
    ```
