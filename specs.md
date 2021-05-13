# The Greeting Card Spammer

Very Informal Specification Document

## Basics

* The application must run on Python 3.6
* The application must use Django
* The application only needs to support current-gen browsers, that is IE 11, Firefox 30, Chrome 35 (or higher, as applicable).

## Backend

* Page refreshes should take less than 750 milliseconds
* 100 results should be shown all times
* Extra points will be awarded by our resident Django pony for adhering to Pythonic and Django standards

## Frontend

* External libraries (even those other than the included jQuery) may be used and included
* Upon mouse over, companies with over 50 000 € in sales must have their names painted with green background, and those with less than that with an orange background.
** The contacts for the mouse-overed company must also be highlit in yellow but only if they have more than 3 orders and more than 50 000 € in sales
* Some users complain that the application does not look very good. Is there something that could be done about that?
* Some users also use the application on mobile devices but it doesn't work very good there. Is that fixable or should we buy those users new tablets instead?
* Extra points will be awarded by our resident front-end hipster for adhering to good JavaScript and jQuery style

## Considerations

* In future, this project might be extended with API that allows data updates
** These data changes must be reflected in the frontend upon the next page load
