# Project Overview

<!-- DATA TYPES, sitebuiler >> JSONField and/or many CharFields ??-->

## Description

> The Patron Portal will be a place for friends and family who have financially supported me through my educational journey to login and request web-development services in exchange for tokens that will be primarily assigned based upon donation amount.

## Q&A

### What are the major features of your web application?

> The primary feature of my capstone will be an application that allows users to build and submit website themes, icons, and ideas directly to me.

### What problem is it attempting to solve?

> Communication and organization. Having a place to for my patrons to access information and provide me with direction and guidance will allow for me to show my appreciation and get valuable real-world experience without getting overwhelmed.

### What libraries or frameworks will you use?

> Bootstrap for certain. I may experiment with additional JS and Django frameworks, but my focus will be to keep this project as light as possible.

## Functionality

### Walk through the application from the user's perspective.

What will they see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?

> The user will arrive at the homepage and have 2 options:
>
> - login
>   - If the user has already registered they will be able to enter their username and password and access their account
> - register
>   - Each patron will receive a registration code. They will be able to enter it here.
>   - An array of objects will contain these codes along with each patron's name and be accessed.
>   - If valid they will then be able to enter in their personal information and create an account. If the registration code matches the name in the object the registration data will be used to create their account. This will also deactivate that registration code.

> Once the user is authenticated they will see their profile page.
>
> Here they will have the option to update select information or access the site builder application.
>
> The site builder will be a form with text fields, color pickers, image/file uploads, and I'm sure additional options and methods of communcation.

## Data Model

### What data will you need to store as part of your application?

In this section list out all the models you'll have and the fields on each of them.

> Account:
>
> - user ID/regcode = CharField(max_length=4)
> - username = CharField(max_length=12)
> - password = CharField(max_length=16, min_length=8)
> - first_name = CharField(max_length=12)
> - last_name = CharField(max_length=12)
> - display name = CharField(max_length=20)
> - email = EmailField(max_length=20)
> - phone = CharField(max_length=10)
> - donation amount = IntegerField()
> - token count = IntegerField()
> - profile picture -ImageField()
> - list of requests ForeignKey('Site_Builder')

> Site_Builder:
>
> - user ID = ForeignKey('Account')
> - request ID = CharField(max_length=8)
> - site admin data
>   - website url = URLField(max_length=20)
>   - site description = CharField(max_length=20)
> - site type = CharField(max_length=20, choices=[(eCommerce, 'eCommerce'), (blog, 'blog'), (other, 'other')])
> - site title = CharField(max_length=20)
> - site logo = ImageField(upload_to='path')
> - site icons = CharField(choices=[(tbd, '')])
> - additional site images = {'label': '', 'image': ''}
> - primary_font = CharField(max_length=20)
> - secondary_font = CharField(max_length=20)
> - primary_color = CharField(max_length=10)
> - build status = IntegerField()

## Schedule

### Here you'll want to come up with some (very rough) estimates of the timeframe for each section.

It also gives you the opportunity to plan out what you'd like to work on after the class is finished. For each milestone, state specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.

> - Week 1
>   - homepage
>   - user model/forms
>   - login/registration pages
>   - profile page

> - Week 2
>   - site_builder model/form basics
>     - title/text fields
>     - color pickers
>     - font pickers
>   - request page

> - Week 3
>   - site_builder model/form advanced
>     - image uploads
>     - build status
>   - status page

> - Week 4
>   - style refinement
>   - code refactoring

> - Beyond
>   - tbd
