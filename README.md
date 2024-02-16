# Sahara Cafe & Beans
Welcome to Sahara Cafe & Beans:

a django-python project by ***Bryar Osman***

The Sahara Cafe & Beans project is a web-based application developed by me Bryar Osman, as part of a school django-python project. It aims to provide an online platform for a cafeteria where customers can sign up, sign in, create profile, view the menu, book/reserve a table with full CRUD functionality for both profile as wel as their reservations.

## Introduction
The website of Sahara Cafe & Beans Cafeteria can be viewd by any custumers. If customers wants to reserve a table, customers can do so if customer sign up and sign in. after filling the sign up form, the customer will get an email with a link to verify their email. The link will redirect the user to the website to confirm their registeration. user can then sign in and create a reservation if they wants to. user will automatically have an profile with default porifle image already filled with their informations when they signed up. the user can change their phone, address and email. But for the email they will guided with a button "change email" if they want to change, they will then get a verfication link to verify the new email. If they create reservation or cancel reservation they will get an instance confirmation if reservation is not double booked, they will alsi get an email confirmation about their rservation or cancelation. user can also delete account and profile if they wish, and if they do that they will be notificed that their reservations will all be canceled. The admin can via admin add menu and menu details. plan is to upgrade so that staff can log in via website instead of admin panel. 

## Table of Contents
- [Sahara Cafe & Beans Project](#sahara-cafe--beans)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Features](#features)
  - [Known Bugs](#known-bugs)
  - [Contributing](#contributing)
  - [License](#license)



## Features

1. **User Authentication and Registration:**
   - Users can register using their email address and receive a verification email to activate their account.
   - Authentication system provided by Django Allauth.
   - Users can change their password and email address.

2. **Email Notifications:**
   - Users receive email notifications for account verification, reservation confirmation, and cancellation.

3. **Table Reservation System:**
   - Users can create reservations from the homepage by clicking the "Reserve Table" button.
   - Reservations cannot be made for the same day.
   - Users receive a confirmation email after making a reservation.
   - Users can view, edit, and update all reservations in their profile page.

4. **Profile Management:**
   - User profiles are automatically created based on signup information.
   - Users can view and manage their profile details, including reservations.
   - Users can delete their profile, with the option to recreate a "profile" afterward within the navbar the profile button will be "create profile" instead, and this will redirect user to create profile.

5. **User Experience Enhancements:**
   - CRUD operations for reservations and profile management are centralized in the user's profile page for better user experience.
   - If a user deletes their profile, they will see a "Create Profile" option in the navbar instead of "Profile."


6. **Data Retention:**
   - If a user deletes their profile, only reservation details and profile information are lost; the account remains.
   - Deleting the account removes all data associated with the user, including the username and account details.

7. **Security warning:**
   - Users are prompted with a warning before deleting their profile and/or account to prevent accidental data loss.
---
<br>

### Python Packages (requirements.txt)

You can install all the required Python packages by running:

```bash
pip install -r requirements.txt
````
## Python Packages

### Description

Here is a brief description of each package used in the project:

- **asgiref==3.7.2**: ASGI specification and utilities.
- **cloudinary==1.38.0**: Cloudinary is a cloud service that offers a solution to a web application's entire image management pipeline.
- **crispy-bootstrap5==2023.10**: Django application to add 'django-crispy-forms' layout objects for the new Bootstrap 5.x.
- **Django==4.2.9**: Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **django-allauth==0.60.1**: Integrated set of Django applications addressing authentication, registration, account management.
- **django-ckeditor==6.7.0**: Django admin CKEditor integration.
- **django-cloudinary-storage==0.3.0**: Cloudinary storage backend for Django.
- **django-crispy-forms==2.1**: Django application to control the rendering behavior of Django forms in a DRY way.
- **django-js-asset==2.2.0**: A Django template library used for adding JavaScript files.
- **django-resized==1.0.2**: Django app to resize image before upload.
- **gunicorn==20.1.0**: Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.
- **oauthlib==3.2.2**: A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
- **pillow==10.2.0**: Python Imaging Library adds image processing capabilities to your Python interpreter.
- **PyJWT==2.8.0**: JSON Web Token implementation in Python.
- **python3-openid==3.2.0**: Python OpenID 3.0. OpenID for modern servers and applications.
- **requests-oauthlib==1.3.1**: OAuthlib authentication support for Requests.
- **sqlparse==0.4.4**: A non-validating SQL parser module for Python.
- **whitenoise==6.5.0**: Radically simplified static file serving for Python web apps.


## Technologies Used

- Django
- Python
- HTML5
- CSS
- JavaScrip
- Bootstrap

#### Other technologies
- Github
- GitPod
- Heroku
- Balsamiq
- Canva
- Cloudinary


## Installation

This is a live website hosted on [Heroku](https://pp4-cafe-d36cb314754f.herokuapp.com/), so there's no need for installation for viewing and trying the website. Simply visit the website using the provided link above or [here](https://pp4-cafe-d36cb314754f.herokuapp.com/).


**Important Note:** This code is not open-source and is protected by copyright law created as a project for school by Bryar Osman. It is not licensed for redistribution or public use. You are not authorized to install or use this code for your own project without explicit permission from [Bryar Osman].

If you are interested in using this code for your own project, please contact [Bryar Osman] at [bryarosman.bo@gmail.com] to inquire about purchasing the code.


## Usage

Visit our website at [Sahara Cafe & Beans](https://pp4-cafe-d36cb314754f.herokuapp.com/) to explore our menu, make reservations, and stay updated on our latest offerings and events.

## Contributing

We welcome contributions from the community! If you have any ideas, bug fixes, or enhancements, feel free to submit a pull request or open an issue on [GitHub](https://github.com/Bryaro/pp4.git).


## Belongs to:

[Bryar Osman](https://github.com/Bryaro)


## Bugs:
##### None
---
