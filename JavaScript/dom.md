# HTML Document Object Model (DOM)
`DOM` is used to search for an html element and retrieve that element.


## How to Work with DOM
### html file
```html
<form id="login-form" action="" method="post">
    <label for="username">username</label>
    <input type="text" id="username" name="username">

    <label for="password">password</label>
    <input type="password" id="password" name="password">

    <button type="button" id="login-btn">login</button>
</form>
```
`IMPORTANT` In the above form, the type of button has been set to `button` to handle a form that has nowhere to submit. Otherwise an error will be raised. This is also valid for an input tag. Note that, the default type is `submit`.

### JavaScript file
`document` is everything between `<html>...</html>`.

`event` is anything that happens in a page, e.g. clicking a button, moving mouse cursor, etc. An `event` is attach to `document` and other HTML elements, e.g. `button`.

`see type 2 in the below template` All we have to do is:
- find the button
- add a listener to that button

Ways of finding an HTML content:
- document.getElementById
- document.getElementsByClassName
- document.getElementsByName
- document.getElementsByTagName
- `preferred` document.querySelector which retrieves the first occurrence of an element
- `preferred` document.querySelectorAll which retrieves a node list

`notation` In querySelector or querySelectorAll:
- use `#` to indicate an id
- use `.` to indicate a class

```javascript
// javascript will wait for html to be completely loaded
document.addEventListener('DOMContentLoaded', function () {
    // write in console that DOM has been loaded
    console.log('DOMContentLoaded');

    // get an element in the document
    // type 1 - old but possible
    const my_div = document.getElementById('myDiv');

    // to get/search an html tag within the div tag (not whole document)
    // const my_btn = my_div.getElementById('loginInput'); 
    // Uncaught TypeError: my_div.getElementById is not a function
    // ***solution***
    const my_btn = new DOMParser().parseFromString(my_div, 'text/html');
    console.log(my_btn);


    // type 2 - new, modern, more reliable
    const btn = document.querySelector('#myBtn');
    btn.addEventListener('click', function () {
        console.log('btn clicked');
    })

})
```
