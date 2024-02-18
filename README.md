# Sahara Cafe & Beans
Welcome to Sahara Cafe & Beans:

a django-python project by ***Bryar Osman***

The Sahara Cafe & Beans project is a web-based application developed by me, Bryar Osman, as part of a Django-Python school project. Its aim is to provide an online platform for a cafeteria, enabling customers to easily sign up, sign in, create profiles, view the menu, and reserve a table. The platform offers full CRUD (create, read, update, and delete) functionality for both profiles and reservations. 
[visit Sahara Cafe & Beans](https://pp4-cafe-d36cb314754f.herokuapp.com/)
![Homepage](/static/docs/readme_assets/homepage_view.png)
![About](/static/docs/readme_assets/SaharaCafe&Beans.png)

The website of Sahara Cafe & Beans Cafeteria can be viewed by any customers. If customers want to reserve a table, they can do so by signing up and signing in. After filling out the sign-up form, the customer will receive an email with a link to verify their email. The link will redirect the user to the website to confirm their registration. Users can then sign in and create a reservation if they wish to. Users will automatically have a profile with a default profile image already filled with their information when they signed up. The user can change their phone number, address, and email. However, for the email, they will be guided with a button "change email." If they want to change it, they will then receive a verification link to verify the new email. If they create a reservation or cancel a reservation, they will receive an instant confirmation if the reservation is not double-booked. They will also receive an email confirmation about their reservation or cancellation. Users can also delete their account and profile if they wish, and if they do so, they will be notified that their reservations will all be canceled. The admin can add menu and menu details via the admin panel. A future plan is to upgrade so that staff can log in via the website instead of the admin panel.

## Table of Contents
- [Welcome to Sahara Cafe & Beans](#sahara-cafe--beans)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [EPICs](#epics)
  - [User Stories](#user-stories)
  - [Agile Development with GitHub](#agile-development-with-github)
  - [Balsamiq Wireframes](#balsamiq-wireframes)
  - [Database Schema Overview](#database-schema-overview)
  - [Features](#features)
  - [Testing for Sahara Cafe & Beans Website](#manual-testing-for-sahara-cafe--beans-website)
  - [Python Packages (requirements.txt)](#python-packages-requirementstxt)
  - [Technologies Used](#technologies-used)
  - [Lighthouse Testing Screenshot](#lighthouse-testing-screenshot)
  - [CSS Validator with No Error](#css-validator-with-no-error)
  - [HTML Validator with No Error](#html-validator-with-no-error)
  - [Python Linter Validator with No Error](#python-linter-validator-with-no-error)
  - [WAVE with No Contrast Error](#wave-with-no-contrast-error)
  - [Credits](#credits)
  - [Future Development Plans](#future-development-plans)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [Deploying Sahara Cafe & Beans on Heroku](#deploying-sahara-cafe--beans-on-heroku)

---
Below, you can expand the collapsible arrows for epics and user stories.

<details>
<summary><strong>EPIC</strong></summary>

### EPIC: User Registration and Authentication
- As a user, I want to be able to register for an account with my email and password.
- As a user, I want to be able to log in to my account using my email and password.
- As a user, I want to be able to reset my password if I forget it.

### EPIC: Cafeteria Menu
- As a user, I want to view the menu items available in the cafeteria.
- As a user, I want to see details about each menu item, including price and description.

### EPIC: User Profile
- As a user, I want to be able to create, view, edit, and delete my profile.

### EPIC: Admin Functionality (Future Plan)
- As an admin, I want to manage menu items (add, edit, delete).
- As an admin, I want to view and manage user accounts.
</details>

<details>
<summary><strong>User Stories</strong></summary>

### User Story: View Menu
**Description:** 
As a customer, I want to view the cafeteria's menu to see available food and drink items.

**Acceptance Criteria:**
- The cafeteria's menu is accessible from the website.
- Users can browse and view all available menu items.

### User Story: View Menu Item Details
**Description:** 
As a user, I want to see details about each menu item, including price and description.

**Acceptance Criteria:**
- When viewing the menu, users can click on a menu item to see its details.
- The details include the price, description, and other relevant information about the menu item.

### User Story: View and Edit Profile Information
**Description:** 
As a user, I want to view and edit my profile information (e.g., name, and contact details).

**Acceptance Criteria:**
- Users can access their profile page.
- Users can view their existing profile information.
- Users have the option to edit and update their profile details.

### User Story: User Registration
**Description:** 
As a user, I want to be able to register for an account with my email and password.

**Acceptance Criteria:**
- The website has a "Register" or "Sign Up" option.
- Users can provide their email address and choose a secure password during registration.
- The system validates the email format and password strength.
- Upon successful registration, users receive a confirmation email to verify their email.
- Users can click a verification link in the email to activate their account.
- Registered users are redirected to the login page after activation.

### User Story: User Login
**Description:** 
As a user, I want to be able to log in to my account using my email and password.

**Acceptance Criteria:**
- There is a "Log In" button on the website.
- Users can enter their registered email and password to log in.
- The system verifies the entered credentials for authentication.
- Users get informed to confirm if they decide to log out when they choose to sign out.

### User Story: Password Reset
**Description:** 
As a user, I want to be able to reset my password if I forget it, ensuring that I can regain access to my account.

**Acceptance Criteria:**
- There is a "Forgot Password?" or "Reset Password" option on the login page.
- Users can provide their registered email address to initiate the password reset process.
- The system sends an email to the provided address with a link to reset the password.
- Users can click the password reset link to access a secure page to enter a new password.
- Password reset links expire after a specified time for security.
- Users see instant confirmation once their password has been successfully reset.

### User Story: Reserve and Cancel Table
**Description:** 
As a customer, I want to reserve a table for a specific date and time, and if needed, I want the option to cancel the reservation.

**Acceptance Criteria:**
- There is a "Reserve Table" option accessible from the website's homepage.
- Users can select a date and time for their reservation.
- The system confirms the reservation and displays reservation details.
- Users receive a confirmation email with reservation details.
- Users can view their reservations from their profile.
- Users have the option to cancel a reservation and get an email confirmation.
- When a reservation is canceled, it is removed from the user's profile.
- After the reservation is canceled, the time becomes available again for reservation to avoid double bookings.
- Cancellation requests are processed without any fees outside the allowed cancellation hours of the reserved time.
</details>

---

### Agile Development with GitHub

In developing this project, I employed agile methodologies using GitHub's robust set of tools. Here's how I utilized these tools to manage the development process effectively:

1. **Issue Tracking**:
   - I created detailed [issues](https://github.com/Bryaro/pp4/issues) for every task and feature required for the project. These issues served as a centralized repository for all development tasks, ensuring clear visibility and organization.

2. **Epics**:
   - To organize and prioritize tasks, I grouped related issues into [epics](https://github.com/Bryaro/pp4/issues?q=is%3Aopen+is%3Aissue+label%3Aepic). This helped me categorize and manage larger features or themes within the project, providing a structured approach to development.

3. **GitHub Milestones**:
   - I utilized GitHub [milestones](https://github.com/Bryaro/pp4/milestones) to plan and track the progress of project sprints. Each milestone represented a specific sprint duration, and I assigned relevant issues to each milestone to track their completion within the sprint timeline.

4. **MoSCoW Method**:
   - I followed the MoSCoW method (Must, Should, Could, Won't) to prioritize tasks within each epic. This approach allowed me to focus on delivering essential features first while considering optional enhancements for future iterations.

5. **Project Board**:
   - GitHub's project [signboard/kanban](https://github.com/users/Bryaro/projects/2) was instrumental in visualizing the workflow and tracking the progress of tasks. I utilized columns representing different stages of development, such as "To Do," "In Progress," and "Done," to manage task progression effectively.

6. **Task Progression**:
   - Tasks were initially added to the "To Do" column. As development progressed, tasks were moved to the "In Progress" column to indicate active work. Upon completion, tasks were then moved to the "Done" column, providing clear visibility into task status.

By leveraging GitHub's agile features, including milestones, I maintained a structured and efficient development process. This methodology facilitates collaboration, ensures alignment with project goals, and allowed for incremental progress towards project completion.

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

## Database Schema Overview

Below is the database schema diagram representing the structure of our Django applications, focusing on user profiles and reservation models. This diagram was created using [dbdiagram.io](https://dbdiagram.io/d), a tool that allows for the visualization of database schemas and relationships. It illustrates the relationships between the default Django `User` model and our custom `UserProfile` and `Reservation` models, showcasing the one-to-one and many-to-one relationships respectively.

![Database Schema Diagram](/static/docs/readme_assets/UserProfile_Reservation_DB_Schema.png)

### Key Components:
- **User**: The default Django authentication model.
- **UserProfile**: Extends the `User` model to include additional user information such as phone number, address, email verification status, and a resized profile image.
- **Reservation**: Represents a reservation with fields for the user (linked to the `User` model), date, time, number of guests, and creation timestamp.

This schema is crucial for understanding the data flow and relationships within the websites system, ensuring efficient data management and retrieval for the application's functionality.


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
   ![](/static/docs/readme_assets/profile_page.png)
   ![](/static/docs/readme_assets/create_profile_nav.png)
   ![](/static/docs/readme_assets/create_profile_page.png)

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

### Manual Testing for Sahara Cafe & Beans Website

1. **Navbar Functionality**:
   - **Test Scenario**: Ensure that all navbar links and buttons are functional and correctly direct users to the intended pages.
   - **Test Steps**:
     - Click on each navbar link, including Home, Menu, Reserve Table, Profile, and About.
     - Verify that each click navigates to the respective page without errors.
     - Test the "Sign Up" and "Sign In" buttons in the navbar.
     - Verify that clicking on "Sign Up" redirects users to the sign-up page.
     - Verify that clicking on "Sign In" redirects users to the sign-in page.
     - Test the functionality of the profile dropdown menu.
     - Ensure that options such as "Edit Profile", "Change Password", "Change Email", and "Delete Account" work as expected.

2. **Sign Up Functionality**:
   - **Test Scenario**: Validate the sign-up process, including form submission, email verification, and account creation.
   - **Test Steps**:
     - Fill out the sign-up form with valid user information.
     - Submit the form and verify that no validation errors occur.
     - Check the provided email inbox for the verification email.
     - Click on the verification link in the email.
     - Verify that the link redirects to the website and confirms the successful verification.
     - Attempt to sign in with the newly created account.
     - Ensure that sign-in is successful and redirects users to their profile page.

3. **Sign In Functionality**:
   - **Test Scenario**: Validate the sign-in process, including entering valid credentials and accessing user accounts.
   - **Test Steps**:
     - Navigate to the sign-in page.
     - Enter valid credentials (email and password) into the sign-in form.
     - Submit the form and verify that no validation errors occur.
     - Ensure that sign-in is successful and redirects users to their profile page.
     - Test sign-in with invalid credentials to verify error handling.

4. **Email Verification**:
   - **Test Scenario**: Verify that users receive a verification email upon signing up and that the email contains a valid verification link.
   - **Test Steps**:
     - Sign up with a new email address.
     - Check the provided email inbox for the verification email.
     - Verify that the email contains a valid verification link.
     - Click on the verification link and ensure successful verification.

5. **Reservation Functionality**:
   - **Test Scenario**: Test the reservation process, including creating, editing, and canceling reservations.
   - **Test Steps**:
     - Navigate to the reservation page.
     - Attempt to create a reservation for a future date.
     - Attempt to book past or today.
     - Verify that the reservation is successfully created and displayed in the user's profile.
     - Test editing the reservation details, such as the date, time, or number of guests.
     - Verify that the changes are reflected in the reservation details.
     - Test canceling the reservation and verify that it is removed from the user's profile.

6. **Profile Management**:
   - **Test Scenario**: Validate the functionality related to managing user profiles, including viewing, editing, and deleting profiles.
   - **Test Steps**:
     - Navigate to the profile page.
     - Verify that the user's profile information is displayed accurately.
     - Test editing profile details such as phone number, address, and email.
     - Verify that changes are saved successfully and reflected in the profile.
     - Test the "Delete Account" functionality.
     - Verify that deleting the account removes all associated data and redirects users accordingly.

7. **Policy Enforcement**:
   - **Test Scenario**: Test the enforcement of reservation policies, including restrictions on editing or canceling reservations within a certain timeframe.
   - **Test Steps**:
     - Attempt to edit or cancel a reservation within the specified timeframe.
     - Verify that users are prevented from making changes and are informed of the policy restrictions.
     - Test editing or canceling reservations outside of the policy timeframe.
     - Verify that users can make changes successfully without encountering any restrictions.

8. **Email Notifications**:
   - **Test Scenario**: Validate that users receive email notifications for various events such as account verification, reservation confirmation, and cancellation.
   - **Test Steps**:
     - Perform actions such as signing up, creating reservations, and editing profiles.
     - Check the provided email inbox for notifications related to these actions.
     - Verify that email notifications are received promptly and contain relevant information.

9. **Forgot Password Functionality**:
   - **Test Scenario**: Validate the functionality for resetting the password if the user forgets their password.
   - **Test Steps**:
     - Navigate to the sign-in page.
     - Click on the "Forgot your password?" link.
     - Enter the email associated with the account.
     - Submit the form and check the provided email inbox for the reset password link.
     - Click on the reset password link in the email.
     - Verify that the link redirects the user to a page where they can enter a new password.
     - Enter the new password and confirm it.
     - Submit the form and verify that the password has been changed successfully.


By conducting manual testing using the above scenarios and steps, you can ensure that Sahara Cafe & Beans website functions as intended, providing users with a seamless and error-free experience.



### Summary Table of Manual Testings for Sahara Cafe & Beans Website

### Test Case #1: Navbar Functionality

| Test Step # | Test Description                          | Action / Input                      | Expected Result                         | Result  |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1           | Click navbar links                       | Click on each navbar link          | Navigate to respective pages            | Pass    |
| 2           | Verify navigation                        | Verify each click navigation        | Navigate to respective pages           | Pass    |
| 3           | Test "Sign Up" button                    | Click on "Sign Up"                  | Redirect to sign-up page                | Pass    |
| 4           | Test "Sign In" button                    | Click on "Sign In"                  | Redirect to sign-in page                | Pass    |
| 5           | Test profile dropdown menu               | Click on profile dropdown menu      | Ensure options work as expected         | Pass    |

### Test Case #2: Sign Up Functionality

| Test Step # | Test Description                          | Action / Input                      | Expected Result                         | Result  |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1           | Fill out sign-up form                    | Enter valid user information       | Form submitted without errors           | Pass    |
| 2           | Submit form                              | Click submit button                 | Account created successfully            | Pass    |
| 3           | Check email inbox                        | Check for verification email        | Verification email received              | Pass    |
| 4           | Click verification link                  | Click on link in verification email| Redirect to website, successful verification | Pass    |
| 5           | Attempt sign-in                          | Sign in with new account           | Sign-in successful, redirected to profile page | Pass    |

### Test Case #3: Sign In Functionality

| Test Step # | Test Description                          | Action / Input                      | Expected Result                         | Result  |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1           | Navigate to sign-in page                 | Click on "Sign In"                  | Sign-in page displayed                 | Pass    |
| 2           | Enter valid credentials                  | Enter email and password           | Sign-in form submitted without errors   | Pass    |
| 3           | Submit form                              | Click submit button                 | Sign-in successful, redirected to profile page | Pass    |
| 4           | Test sign-in with invalid credentials   | Enter incorrect email/password    | Relevant message displayed, Incorrect email or password.     | Pass    |


### Test Case #4: Email Verification

| Test Step # | Test Description                          | Action / Input                      | Expected Result                         | Result  |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1           | Sign up with new email address           | Fill out sign-up form               | Account created, verification email sent | Pass    |
| 2           | Check email inbox                       | Check for verification email        | Verification email received             | Pass    |
| 3           | Click verification link                 | Click on link in verification email| Redirect to website, successful verification | Pass    |

### Test Case #5: Reservation Functionality

| Test Step # | Test Description                                  | Action / Input                      | Expected Result                                       | Result  |
|-------------|--------------------------------------------------|-------------------------------------|--------------------------------------------------------|---------|
| 1           | Navigate to wreservation page                     | Click on "Reserve Table"           | If signed in, reservation page displayed; if not signed in, redirected to sign-in page; if not registered, redirected to sign-up page | Pass    |
| 2           | Attempt to create a reservation for a future date| Select future date/time           | Reservation form opens                                 | Pass    |
| 3           | Attempt to book past or today                    | Select past or today's date/time  | Relevant message displayed, unable to book              | Pass    |
| 4           | Verify reservation is successfully created       | Enter valid reservation details   | Reservation created successfully and displayed in profile | Pass    |
| 5           | Test editing reservation details                 | Edit reservation information      | Changes reflected in reservation details                | Pass    |
| 6           | Test canceling the reservation                  | Click cancel button                | Reservation canceled and removed from user's profile    | Pass    |


### Test Case #6: Profile Management

| Test Step # | Test Description                          | Action / Input                      | Expected Result                         | Result  |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1           | Navigate to profile page                | Click on "Profile"                  | Profile page displayed                 | Pass    |
| 2           | Verify profile information              | Check displayed information         | Information accurate and up-to-date    | Pass    |
| 3           | Edit profile details                    | Modify profile information         | Changes saved successfully             | Pass    |
| 4           | Delete account                          | Click "Delete Account"             | Account deleted, redirected accordingly | Pass    |

### Test Case #7: Policy Enforcement

| Test Step # | Test Description                          | Action / Input                      | Expected Result                         | Result  |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1           | Attempt to edit/cancel within timeframe | Edit/cancel reservation within timeframe | Changes prevented, user notified  | Pass    |

*Please note that the each main tests are divided into substeps*

---
<br>

Testing was conducted on the following browsers:

- Google Chrome
- Safari
- Microsoft Edge
- Firefox

Devices I used for testing included:

- MacBook Air Pro
- iPhone 13 Pro
- iPhone 12 Pro
- iPad Air
- Samsung Galaxy A51/A71
---

## Python Packages (requirements.txt)

You can install all the required Python packages by running:

```bash
pip install -r requirements.txt
````

## Python Packages

Here is a brief description of each package used in the project click on the collapsible arrow on "Description":

<details>
    <summary><strong>Description</strong></summary>
   
   ### Description

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
  </details>


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
   - Canva is a graphic design platform for creating various designs using customizable templates and drag-and-drop tools. In this project, I used Canva pro, it was used to create the AI-based images for all the pages but also for the default profile image.

6. **Cloudinary**:
   - Cloudinary is a cloud-based media management solution for uploading, storing, optimizing, and delivering images and videos for web and mobile applications. Used it to store users profile image.

## Lighthouse Testing Screenshot

![](/static/docs/readme_assets/lighthouseDesktop.png)

## CSS Validator with No Error

![](/static/docs/readme_assets/CSS_validator.png)

## HTML Validator with No Error

![](/static/docs/readme_assets/html_validator.png)

## Python linter Validator with No Error

![](/static/docs/readme_assets/python_linter_validator.png)

## WAVE with No Contrast Error

![](/static/docs/readme_assets/WAVE_contrast.png).

## Future Development Plans

### 1. Adding Social Media Integration:
   - Incorporate social media links, such as Instagram and Facebook, into the footer of the website. This will enhance user engagement and provide additional channels for communication and promotion.

### 2. Implementing Staff Login Dashboard:
   - Develop a secure login dashboard specifically for staff members to access administrative features and manage various aspects of the application. This dashboard can include functionalities for inventory management, order processing, and customer support.

### 3. Introducing E-commerce Functionality:
   - Expand the functionality of the website to include e-commerce capabilities, allowing users to place orders for coffee beans, cups, and other related products. This feature will enhance the user experience and provide additional revenue streams for the business.

These future development plans aim to further enhance the functionality, usability, and overall user experience of Sahara Cafe & Beans. Stay tuned for updates as we work on implementing these exciting features!


## Installation

This is a live website hosted on [Heroku](https://pp4-cafe-d36cb314754f.herokuapp.com/), so there's no need for installation for viewing and trying the website. Simply visit the website using the provided link above or [here](https://pp4-cafe-d36cb314754f.herokuapp.com/).


## Important Note

This project, Sahara Cafe & Beans, is a web-based application developed by Bryar Osman as part of the Code Institute's Full Stack Development program. It serves as the fourth and final milestone project for the school curriculum. The code is the result of academic effort and learning, showcasing skills in Django, Python, HTML, CSS, JavaScript, and other web development technologies.

## Contributing

Contributions are welcome! If you have any ideas, bug fixes, or enhancements, feel free to submit a pull request or open an issue on [GitHub](https://github.com/Bryaro/pp4.git).

**Copyright and Usage:**

- This codebase is intended for educational purposes and to demonstrate my skills as a developer. It is hosted on [Heroku](https://pp4-cafe-d36cb314754f.herokuapp.com/) for public viewing and interaction.
- The project is protected under copyright laws and is not open-source. It cannot be used for commercial purposes or distributed without explicit permission.
- If you are interested in using this project's code for educational purposes or wish to collaborate on similar projects, please contact me, Bryar Osman, at [bryarosman.bo@gmail.com], and after that reach out to the Code Institute for their guidance and permission as well.

I welcome feedback, contributions to the project under the guidelines mentioned above, and discussions on further enhancing its features or functionality.

---

## Credits

### Stack Overflow
- [Stack Overflow](https://stackoverflow.com/questions/18999557/responsive-design-not-working-on-heroku-deployed-rails-app) - A valuable resource for programming questions and issue resolution. Many thanks to the community for providing helpful solutions and insights.

### Slack
- [Slack](https://code-institute-room.slack.com/archives/C065C3V3FTP) - A collaboration hub for teams, enabling efficient communication and knowledge sharing. Special thanks to the [@Kay_ci] community for their support and assistance.

### Django
- [Django Documentation](https://docs.djangoproject.com/) - The official documentation for Django, providing comprehensive guidance on installation, usage, and best practices.

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

That's it! You've successfully deployed a web application similar to Sahara Cafe & Beans on Heroku.

---
### Disclaimer

This project, PP4, was created as part of my school coursework. It may contain mistakes, typos, or areas that need improvement. I'm continuously working on refining it to the best of my abilities.

Your understanding and patience are appreciated. If you notice any issues or have suggestions for improvement, please don't hesitate to let me know.

---

I'm committed to continually improving PP4 and welcome your feedback, suggestions, and contributions. Please don't hesitate to open an issue or submit a pull request if you encounter any bugs, have ideas for new features, or want to contribute code.



/Bryar

[Take me back to the top](#sahara-cafe--beans)