SELP Proposal - Cameron Gray (s1230461)
=======================================

Introduction
------------
For my SELP project I plan on developing a web based audience response system.  This would be similar to the "clicker" system used by many schools within the university however it would run entirely in the web browser. The benefit of this is that it does not require any specialised hardware and does not require all users to all be in the same room.  Therefore it can be used in situation such as online confrences where participants may be anywhere in the world.

Parts of the Application
------------------------
The applicaton can be split up into several different components, each providing functionality for a different type of user.

### Administration
This part of the application would be used to manage users as well as any other settings/options for the application.  In a university situation this would be used by administration staff to manage students/tutors.

### Tutor
This section would be used by the tutor or whoever will be setting and asking questions.  This area would be used to both prepare lessons with predefined lists of questions as well as being used during the response session in order to trigger questions to be asked as well as to view results.

### Responder
This section will present the user with questions and allow them to select an answer.  It will be optimized to run on various devices so that it will work equally as well on a smartphone as it would on a full desktop browser.  This is due to the fact that audience members in a lecture will likely to prefer to use a handheld device rather than a laptop to respond to the questions.

Technologies
------------
### Backend
I plan on writing the backend in Python using the Django framework.  I have picked this for several reasons:
* I am already familiar with the framework and the Python language in general
* It does a lot of common tasks automatically saving development time
* The included ORM lends itself well to this sort of application

I also plan on using SQLite as the database during development due to it being easily portable between systems.  This is sufficient for testing however if this application were to be used in a production environment the database would need to be switched for something more powerful like PostgreSQL.  Django's ORM however would allow the Database to be swapped out without any code changes to the application.

### Frontend
I plan on using Twitter's Bootstrap framework to do most of the frontend work.  This will save a lot of time and will allow the site to still look good, despite me not being a fantastic graphic designer.  The interactive elements of the frontend will be written in Javascript using the jQuery framework, something I am very familiar with.

Timescales
----------
I believe this project should roughly take around 70 hours for a working version, does this sound realistic?

If it took less time than required I could then add in several other features to expand the functinality such as an API to allow other applications to interface with the audience response system.

Ranking
-------
This application has many different potential ways to perform a ranking of users, this could be done by using individual results such as _% of correct answers_ or _number of questions answered_.  Alternatively an overall "score" could be assigned to users calculated based on their performance.  Multple diffferent rankings could be implemented depending on time available.  Does this sound suitable?