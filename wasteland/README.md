# CV-Wasteland

Python web game (built with a Django backened) that takes you into a fictional future where civilization has collapsed. Collect items daily to survive and grow your strength. How many days can you survive?

## Index
- [Authors](#authors)
- [Scope](#scope)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Data Models](#data-models)
- [Future Updates](#future-updates)

## Getting Started

You can view the site here: https://zombie-wasteland.herokuapp.com

In order to begin, first create an account or log in. Then create a character from within your 'Profile' page. Finally, once you're viewing the characters page you can choose what actions to perform.

## Authors

* **Tina Taylor** - https://github.com/longevitytina - https://www.linkedin.com/in/tina-taylor-codes/
* **Jake Johnson** - https://github.com/jakerjohnson21 - https://www.linkedin.com/in/jakekj/

## Scope

The final objective was to make an app where users can simulate survivor experiences in the wasteland. Users will be able to create characters which can collect items and perform different actions when facing an event. Due to limited time, the site does not have full functionality, but see milestones for future builds.

##### Technologies used: 

* [Python](https://www.python.org) - Language
* [Django](https://www.djangoproject.com) - The web framework used
* [Heroku](https://www.heroku.com) - Deployment
* [Bootstrap](https://getbootstrap.com) - Styling

## User Stories

##### Home Page
* User is presented some information such as a description of the site and a quick summary of how to use it. 
* Here a user can login to their account or create a new one.
* Upon clicking ‘Create account’ a modal will pop up for creating a character

##### Profile Page
* User needs to be authorized
* User can view their character and statsm, and the items they have collected
* User can click ‘Next Day’ to simulate their character spending another day in the wasteland
* User can view a log of the events that have taken place over the last few days
* Items Page
* User does not need to be authorized to view this page.
* User will be presented a detailed list of all the items he/she may acquire

##### About Page
* User does not need to be authorized
* User is displayed information about the two developers of the site with images and a short bio. 

## Wireframes

![Wireframe1](/wasteland/main_app/img/ss1.png)
![Wireframe2](/wasteland/main_app/img/ss2.png)
![Wireframe3](/wasteland/main_app/img/ss3.png)

## Data Models

* Our core model structure was Many-to-Many

```
class Item(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(max_length=500)
```
```
class Character(models.Model):
   name = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   age = models.TextField(max_length=100)
   occupation = models.IntegerField()
   attributes = models.ManyToManyField(Attribute)
	#M:M relationship between user and item
   items = models.ManyToManyField(Item)
```

## Future Updates
* Attribute system
* Items manipulation based off scenarios
* Character health system
* Seed file for data
* Continue building scenarios
* User interaction with others
* 3rd party APIs such as Google Maps

## License

This project is licensed under the MIT License
