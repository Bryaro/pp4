# Sahara Cafe & Beans
Welcome to Sahara Cafe & Beans:

a django-python project by ***Bryar Osman***

The Sahara Cafe & Beans project is a web-based application developed by me Bryar Osman, as part of a school django-python project. It aims to provide an online platform for a cafeteria where customers can sign up, sign in, create profile, view the menu, book/reserve a table with full CRUD functionality for both profile as wel as their reservations.
[visit Sahara Cafe & Beans](https://pp4-cafe-d36cb314754f.herokuapp.com/)
![Homepage](/static/docs/readme_assets/homepage_view.png)
![About](/static/docs/readme_assets/SaharaCafe&Beans.png)

## Balsamiq Wireframes

### Home Page
![Home Page Wireframe](/static/docs/readme_assets/balsamiq_homepage.png)
*Description: This wireframe represents the layout and design of the home page, showcasing the main features and navigation elements.*

### Reservation Page
![Reservation Page Wireframe](/static/docs/readme_assets/balsamiq_reserve_table.png)
*Description: This wireframe illustrates the user interface for making reservations, including form fields and submission buttons.*

### Profile Page
![Profile Page Wireframe](/static/docs/readme_assets/balsamiq_profile.png)
*Description: This wireframe demonstrates the layout and components of the user profile page, displaying profile information and reservation history.*

### Menu Page
![Menu Page Wireframe](/static/docs/readme_assets/balsamiq_menu.png)
*Description: This wireframe showcases the layout and components of the menu page, displaying menu items and options for all users, including unregistered users.*

### Reservation Confirmation Page
![Reservation Confirmation Page Wireframe](/static/docs/readme_assets/balsamic_confirmation.png)
*Description: This wireframe illustrates the layout and components of the reservation confirmation page, providing users with confirmation details after making a reservation.*



## Introduction
The website of Sahara Cafe & Beans Cafeteria can be viewd by any custumers. If customers wants to reserve a table, customers can do so if customer sign up and sign in. after filling the sign up form, the customer will get an email with a link to verify their email. The link will redirect the user to the website to confirm their registeration. user can then sign in and create a reservation if they wants to. user will automatically have an profile with default porifle image already filled with their informations when they signed up. the user can change their phone, address and email. But for the email they will guided with a button "change email" if they want to change, they will then get a verfication link to verify the new email. If they create reservation or cancel reservation they will get an instance confirmation if reservation is not double booked, they will alsi get an email confirmation about their rservation or cancelation. user can also delete account and profile if they wish, and if they do that they will be notificed that their reservations will all be canceled. The admin can via admin add menu and menu details. Future plan is to upgrade so that staff can log in via website instead of admin panel. 

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
![](/static/docs/readme_assets/sign_up.png)
![](/static/docs/readme_assets/verify_email_prompt.png)
![](/static/docs/readme_assets/confirm_email_signup.png)
![](/static/docs/readme_assets/confirm_green_button.png)

If user forgets email: in the sign in there is a link with "Forgot your password" that redirects user to this below:
![](/static/docs/readme_assets/forgot_your_password.png)
![](/static/docs/readme_assets/pass_reset_sent.png)
![](/static/docs/readme_assets/open_email_pass_reset.png)
![](/static/docs/readme_assets/pass_reset_email.png)
![](/static/docs/readme_assets/change_pass.png)
![](/static/docs/readme_assets/your_password_is_changed.png)

2. **Email Notifications:**
   - Users receive email notifications for account verification, reservation confirmation, and cancellation.(Please see the attached images in previous features description as well in the descriptions below)

3. **Profile Management:**
   - User profiles are automatically created based on signup information.
   - Users can view and manage their profile details, including reservations.
   - Users can delete their profile, with the option to recreate a "profile" afterward within the navbar the profile button will be "create profile" instead, and this will redirect user to create profile.

      *Here user have access to read, edit/update and delete/cancel based on relevant choise*.
   *Reservations are inside the users profile with default profile picture*
<br>![](/static/docs/readme_assets/profile_page.png)

4. **Table Reservation System:**
   - Users can create reservations from the homepage by clicking the "Reserve Table" button.
   - Users is shown policy for the reservation, cancelation and edit.
   - Reservations cannot be made for the same day.
   - Users receive a confirmation email after making a reservation.
   - User cant edit or cancel if the reservation date is within 2 days.
   - Otherwise users can view, edit, and update reservations in their profile page.
   - If cancel and edit policy deadline is reached: Users cant edit/update or delete reservation to avoid free tables which will cost the cafeteria.


   <br>

   ![](/static/docs/readme_assets/reserve_table_page.png)

   ![](/static/docs/readme_assets/reservation_confirm_page.png)
   here I've made a reservation and canceled right away simply to show both reservation and cancelation <br>
   ![](/static/docs/readme_assets/reservation_cancelation_email.png)
   reservaton message to users email <br>
   ![](/static/docs/readme_assets/reserved_table_email.png)

   cancelation message to users eamil <br>
   ![](/static/docs/readme_assets/reserved_table_email.png)

   Instead being able to edit or cancel, user will see this:
   ![](/static/docs/readme_assets/cant_cancel_policy.png)


5. **User Experience Enhancements:**
   - CRUD operations for reservations and profile management are centralized in the user's profile page for better user experience.
   - If a user deletes their profile, they will see a "Create Profile" option in the navbar instead of "Profile."

   ![](/static/docs/readme_assets/profile_navbar.png)

   ![](/static/docs/readme_assets/create_profile_nav.png)

   ![](/static/docs/readme_assets/edit_profile_page.png)
   ---
   Giving user a choice if user want to cahnge email, and verification will be sent again if user changes email
   ![](/static/docs/readme_assets/if_email_edit_page.png)

6. **Data Retention:**
   - If a user deletes their profile, reservation details and profile information are lost; the account remains.
   - Deleting the account removes all data associated with the user, users reservations, including the username and account details.

7. **Security warning:**
   - Users are prompted with a warning before deleting their profile and/or account to prevent accidental data loss.

   Profile deletion warning
   ![](/static/docs/readme_assets/Delete_profile.png)
   ACCOUNT deletion warning
   ![](/static/docs/readme_assets/delete_ACCOUNT.png)
---
<br>

### Agile Development with GitHub

In developing this project, I employed agile methodologies using GitHub's robust set of tools. Here's how I utilized these tools to manage the development process effectively:

1. **Issue Tracking**:
   - I created detailed issues for every task and feature required for the project. These issues served as a centralized repository for all development tasks, ensuring clear visibility and organization.

2. **Epics**:
   - To organize and prioritize tasks, I grouped related issues into epics. This helped me categorize and manage larger features or themes within the project, providing a structured approach to development.

3. **GitHub Milestones**:
   - I utilized GitHub milestones to plan and track the progress of project sprints. Each milestone represented a specific sprint duration, and I assigned relevant issues to each milestone to track their completion within the sprint timeline.

4. **MoSCoW Method**:
   - I followed the MoSCoW method (Must, Should, Could, Won't) to prioritize tasks within each epic. This approach allowed me to focus on delivering essential features first while considering optional enhancements for future iterations.

5. **Project Board**:
   - GitHub's project board was instrumental in visualizing the workflow and tracking the progress of tasks. I utilized columns representing different stages of development, such as "To Do," "In Progress," and "Done," to manage task progression effectively.

6. **Task Progression**:
   - Tasks were initially added to the "To Do" column. As development progressed, tasks were moved to the "In Progress" column to indicate active work. Upon completion, tasks were then moved to the "Done" column, providing clear visibility into task status.

By leveraging GitHub's agile features, including milestones, I maintained a structured and efficient development process. This methodology facilitates collaboration, ensures alignment with project goals, and allowed for incremental progress towards project completion.


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


## Technologies used

### Core Technologies:
1. **Django**:
   - Django is a high-level Python web framework for rapid development of secure and maintainable websites.
   This was used for the backend framework for Sahara Cafe & Beans.

2. **Python**:
   - Python is a versatile programming language known for its simplicity and readability, widely used extensively in Sahara Cafe & Beans also for the backend development and logic implementation.

3. **HTML5**:
   - HTML5 is the latest version of Hypertext Markup Language used for structuring and presenting content on the web.

4. **CSS**:
   - CSS (Cascading Style Sheets) is a style sheet language used for enhancing the visual appearance and layout of web pages. In this project, CSS was utilized to customize the styling of the website, ensuring a unique and visually appealing design.

5. **JavaScript**:
   - JavaScript is a dynamic programming language primarily used for adding interactivity and behavior to web pages, such as custimize the functionality of the date picker.

6. **Bootstrap**:
   - Bootstrap is a front-end framework for building responsive and mobile-first websites, providing pre-designed templates and components.

### Other Technologies:
1. **GitHub**:
   - GitHub is a web-based platform for version control and collaboration using Git.

2. **GitPod**:
   - GitPod is an online integrated development environment (IDE) for coding and collaborating on GitHub projects. Providing an online development environment for Sahara Cafe & Beans.

3. **Heroku**:
   - Heroku is a cloud platform for deploying, managing, and scaling applications easily. I used Heroku for hosting Sahara Cafe & Beans live deployment.

4. **Balsamiq**:
   - Balsamiq is a wireframing tool for creating low-fidelity mockups and prototypes of user interfaces.

5. **Canva**:
   - Canva is a graphic design platform for creating various designs using customizable templates and drag-and-drop tools. In this project, Canva was used to create AI-based images and graphics for the website, enhancing its visual appeal.

6. **Cloudinary**:
   - Cloudinary is a cloud-based media management solution for uploading, storing, optimizing, and delivering images and videos for web and mobile applications.


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

### Deploying Sahara Cafe & Beans on Heroku:

Congratulations! You've reached the end of the README file for Sahara Cafe & Beans. By following the steps outlined below, you'll be able to deploy a similar project to Heroku in the future:

1. **Sign up for a Heroku account**:
   - If you haven't already, sign up for a free Heroku account at [Heroku](https://www.heroku.com/).

2. **Install Heroku CLI**:
   - Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) for your operating system to interact with Heroku from the command line.

3. **Log in to Heroku CLI**:
   - Open a terminal and log in to Heroku CLI using the command `heroku login`. Follow the prompts to log in to your Heroku account.

4. **Navigate to your project directory**:
   - Make sure you have a project directory ready containing your web application code.

5. **Create a new Heroku app**:
   - Run `heroku create` in the terminal within your project directory to create a new Heroku app. This will generate a unique app URL.

6. **Add a Procfile**:
   - Create a `Procfile` in your project root directory with the command `web: gunicorn your_project_name.wsgi`. This file tells Heroku how to run your application.

7. **Commit your changes**:
   - Ensure all your changes are committed to your Git repository using version control.

8. **Set up environment variables**:
   - Go to your Heroku dashboard and navigate to your app.
   - Click on the "Settings" tab and then on "Reveal Config Vars".
   - Add environment variables for passwords, security keys, and other sensitive information required for your project.

9. **Deploy to Heroku**:
   - Run `git push heroku main` to deploy your project to Heroku.

10. **Migrate database and collect static files**:
    - After deployment, run `heroku run python manage.py migrate` to migrate your database on Heroku.
    - Run `heroku run python manage.py collectstatic` to collect static files on Heroku.

11. **Open your app**:
    - Finally, run `heroku open` in the terminal to open your newly deployed web application in your web browser.

12. **Note**: 
    - Remember that Heroku offers a free tier for hosting applications, but there may be limitations on resources and features. Be sure to review Heroku's pricing and plans for more information.

That's it! You've successfully deployed a web application similar to Sahara Cafe & Beans on Heroku. We hope this guide has been helpful to you.
