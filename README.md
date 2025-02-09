Capstone Project - Psychology Website:

![Website Preview](/assets/emily.png)

Introduction:

- I built a website for a doctor of psychology who is looking for her own website.
- Here is the live link: https://psychologistwebsite-80b159481955.herokuapp.com/

Website Goals:

- The website main goal is to get visitors to book an appointment with the doctor
- Other goals are to ensure all information on the site is easily accessible
- The website is desktop, tablet & mobile responsive

Key Features:

- Website owner Emily is able to add, edit & delete blogs from the website.
- This is easier then going to the admin panel each time, this was added to increase her efficency.
- Website visitors are not able to edit, or delete blogs due to user autherisation
- User autherisation is added to allow users to comment on blogs to make the website more engaging.
- A booking form linked to Emilys email allows users to book a meeting directly into her calander.
- Navbar & footer links have been added for easy accessability to different site sections.


Built With:

- HTML, CSS, & Bootstrap = Frontend
- Python & Django = Backend
- Django = Database

Deployment:

- Website is live on Heroku and github pages

Testing:

- Lighthouse testing results
![This is my desktop lightening results](/assets/website%20lighthouse%20testing%20-%20desktop.png)
![This is my mobile lightening results](/assets/website%20lighthouse%20testing%20-%20mobile.png)

UX - User Experience:

- The website should have a trusted feel as the client is a doctor
- The website should have a neutral colour scheme that favours trust while remaining clear for users to digest the content 

Design Ideation:

- Colour Pallete:
![This is my colour pallete](/assets/coolers.png)
- Credit to coolers


Desktop Wireframe:

![this shows a wireframe of the desktop hero & Navbar section](/assets/Desktop%20Hero%20Image.png)
![this shows a wireframe of the Who is this for section](/assets/Who%20is%20this%20for%20section%20-%20desktop.png)
![this shows a wireframe of the About Me section](/assets/About%20me%20Desktop.png)
![this shows a wireframe of the Booking section](/assets/Booking%20Desktop.png)
![this shows a wireframe of the Log In section](/assets/Log%20In%20Page%20Wireframe.png)
![this shows a wireframe of the Sign Up hero section](/assets/Sign%20Up%20Desktop%20Wireframe.png)

Mobile Wireframes:

![this shows a wireframe of the mobile navbar section](/assets/Mobile%20Nav%20Bar.png)
![this shows a wireframe of the mobile Log In section](/assets/LogIn%20Mobile.png)
![this shows a wireframe of the mobile Sign Up section](/assets/SignUp%20Mobile.png)
![this shows a wireframe of the mobile Booking section](/assets/Booking%20mobile.png)


The use of AI:

- Chat GPT helped me create blog posts that were inline with the services that the website offer

- Code Creation: Having Co-pilot set up the intial html doc type on pages was a great time saver.

- Debugging: Using Copilot to help source ideas for bug fixed was a great learning experience, It also helped come up with soloutions I hadn't though of.

- Automated Testing : adjustments were made off recommendations by copilot to help certain tests pass

- Performance: Suggestions of how to code less where useful and impacful on my lightening score results

- Overall Impact: AI is a fantastic resource to help improce my learning and coding.

- AI was used to create the ERD from my inital outlines
![AI suggested this would be a good ERD for blog posts](/assets/Blog%20Posts%20ERD.png)
![AI suggested this would be a good ERD for blog comment posts](/assets/Comment%20ERD.png)


User Stories:

    User Registration and Login:

- As a new patient, I want to register an account on the website so that I can book appointments and access my medical records.

- As a returning patient, I want to log in to my account so that I can manage my appointments and view my medical history.

    Appointment Booking:

- As a patient, I want to browse available appointment slots so that I can choose a convenient time for my appointment.

- As a patient, I want to book an appointment with my preferred doctor so that I can receive the medical care I need.

- As a patient, I want to receive a confirmation email for my booked appointment so that I can be sure my appointment is scheduled.

    Appointment Management:

- As a patient, I want to view my upcoming appointments so that I can keep track of my medical visits.

- As a patient, I want to reschedule or cancel an appointment so that I can make changes to my plans if needed.

- As a patient, I want to receive reminders for my upcoming appointments so that I do not miss them.

    Doctor Profiles:

- As a patient, I want to view profiles of the doctors available so that I can choose a doctor based on their specialties and experience.

- As a patient, I want to read reviews or testimonials from other patients so that I can make an informed decision about which doctor to book.

    Contact and Support:

- As a patient, I want to access contact information for the clinic so that I can call or email for further assistance.

- As a patient, I want to submit inquiries or feedback through a contact form so that I can communicate with the clinic conveniently.


Security:

- Allauth python libary was installed for authentication
- The site owner (Emily) has a personal login details that allow only her to add or edit and remove a blog post
- Additional logins are accepted with rules of only being able to update their own comments
- Users must be loged in to leave a comment 
- If a user does not have a login they are guided to a register page 

![This shows the authentication rules work](/assets/Auth%20table.png)

Admin Panel:

![Admin panel login](/assets/admin.png)
![Admin panel behind the login](/assets/admin%20-%20bl.png)

Testing:

- HTML validation passed apart from outside javascript fuction to reduce header from navbar sections

- ![HTML testing](/assets/html%20test%20emily.png)

- CSS testing passed
- ![Css testing](/assets/css%20test%20emily.png)

- Automated Testing:

- Tools Used: Django TestCase, GitHub Copilot.
- Features Covered: CRUD operations, user authentication, and accessibility compliance.
- Adjustments Made: Additional manual modifications to ensure comprehensive test coverage and inclusivity.

![auto testing](/assets/auto%20test.png)

Credits:

- Massive Thanks to Dillon Mccaffrey, Mark Briscoe & Roo for all thier help and support when building this project.
- Thanks to unsplash free images for all images
- Thanks to calendly for the free booking calander I embeded on my website
- Thanks to chatgpt & copilot for help in rewording blogs and user stories



