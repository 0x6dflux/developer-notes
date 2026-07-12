# jQuery
send request to a backend server

other applications (e.g. to interact with the page), which requires a good understanding of javascript (need time)

it is also possible to send a request to a backend server using javascript, but, using jquery is better, clean, and easy to debug.

API Documentation: https://api.jquery.com/

Download jQuery: https://jquery.com/download/

Tutorials:
- https://www.geeksforgeeks.org/jquery/jquery-tutorial/
- https://www.w3schools.com/jquery/default.asp

## jQuery Selectors
resource: https://www.w3schools.com/jquery/jquery_selectors.asp

jQuery selectors allow you to select and manipulate HTML element(s).

jQuery selectors are used to "find" (or select) HTML elements based on their name, id, classes, types, attributes, values of attributes and much more. It's based on the existing `CSS Selectors`, and in addition, it has some own custom selectors.

All selectors in jQuery start with the dollar sign and parentheses: `$()`.


### The #id Selector
```javascript
$(function(){
    // the above function will be executed when the DOM is ready
    $('button').on('click', function(){
        // the above function will be executed when a button is clicked
        $('#test').hide();
        // When a user clicks on a button, the element with id="test" will be hidden
    });
});

// *****************************************************
// below syntaxes are deprecated, but still functioning
// *****************************************************

$(document).ready(function(){
  $("button").click(function(){
    // When a user clicks on a button, the element with id="test" will be hidden
    $("#test").hide();
  });
});
```

### The .class Selector
```javascript
$(function(){
    // the above function will be executed when the DOM is ready
    $('button').on('click', function(){
        // the above function will be executed when a button is clicked
        $('.test').hide();
        // When a user clicks on a button, the elements with class="test" will be hidden
    });
});

// *****************************************************
// below syntaxes are deprecated, but still functioning
// *****************************************************

$(document).ready(function(){
  $("button").click(function(){
    // When a user clicks on a button, the elements with class="test" will be hidden
    $(".test").hide();
  });
});
```

### The Element Name Selector
```javascript
$(function(){
    // the above function will be executed when the DOM is ready
    $('button').on('click', function(){
        // the above function will be executed when a button is clicked
        $('p').hide();
    });
});

// *****************************************************
// below syntaxes are deprecated, but still functioning
// *****************************************************

$(document).ready(function(){
  $("button").click(function(){
    // When a user clicks on a button, all <p> elements will be hidden
    $("p").hide();
  });
});
```

### Chain of Selector
Suppose, you want to find another HTML element, e.g. a button, within a form. There are several approaches.

resource: https://stackoverflow.com/questions/5808606/jquery-selecting-elements-from-inside-a-element

```javascript
// type 1


const loginForm = $('#login-form');
// the above syntax will store a `JQuery<HTMLElement>` in the variable.

loginForm > $('#login-btn').on('click', function () {
    // write your expressions
});

// or

$('#login-form') > $('#login-btn').on('click', function () {
    // write your expressions
});
```

```javascript
// type 2


const loginForm = $('#login-form');
const loginButton = loginForm.find('#login-btn');

// or

const loginForm = $('#login-form');
const loginButton = loginForm.find($('#login-btn'));
```
`IMPORTANT` Combining types 1 and 2 are `NOT` possible.
```javascript
// not working

const loginForm = $('#login-form');
const loginButton = loginForm > $('#login-btn');
// the above syntax will result in 'false'
```

```javascript
// type 3


$('#login-form > #login-btn').on('click', function () {
    // write your expressions
    // note that, `this` refers to the latest jQuery<HTMLElement> object
    // in this case, `this` or `$(this)` refers to the $('#login-btn')
});
```

`IMPORTANT` I personally prefer types 1 and 2. Since the element is stored in a variable and can be accessed later.

### jQuery Selector Tester
resource: https://www.w3schools.com/jquery/trysel.asp

### jQuery Selectors Reference
resource: https://www.w3schools.com/jquery/jquery_ref_selectors.asp


## jQuery Event Methods
resource: https://www.w3schools.com/jquery/jquery_events.asp

### Commonly Used jQuery Event Methods

#### $(document).ready()
This method allows us to execute a function when the document is fully loaded.

#### click()
This method attaches an event handler function to an HTML element. The function is executed when the user clicks on the HTML element.

```javascript
$('p').on('click', function(){
    $(this).hide();
    // note that the hide is a method of jQuery.
    // without using $(), this method will not work.
});

// *****************************************************
// below syntaxes are deprecated, but still functioning
// *****************************************************

$("p").click(function(){
    // When a click event fires on a <p> element
    // hide the current <p> element
    $(this).hide();
});
```


## Working with Form
```html
<form id="login-form" action="http://localhost:8004/" method="post">
    <label for="username">username</label>
    <input type="text" id="username" name="username">

    <label for="password">password</label>
    <input type="password" id="password" name="password">
    
    <button type="button" id="login-btn">login</button>
</form>
```
```javascript
const loginForm = $('#login-form');
const usernameInput = loginForm.find('#username');
const passwordInput = loginForm.find('#password');

const usernameValue = usernameInput.val();
const passwordValue = passwordInput.val();
// or
const usernameValue = usernameInput[0].value;
const passwordValue = passwordInput[0].value;
```

`Note` The `val()` method is used to get and set the value of an input.

resources:
- https://www.w3schools.com/jquery/jquery_dom_get.asp
- https://www.w3schools.com/jquery/jquery_dom_set.asp
- https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_dom_html_set
```javascript
const usernameValue = usernameInput.val();
// gets the value of the input and stores it in usernameValue variable


usernameInput.val('some text');
// sets the value of the input
```

`Note` The `usernameInput[0]` returns the HTMLElement and HTML DOM elements work on it. Please see this link https://www.w3schools.com/jsref/dom_obj_all.asp.

another resource: https://www.geeksforgeeks.org/jquery/how-to-replace-innerhtml-of-a-div-using-jquery/
```javascript
usernameInput[0].classList.remove('d-none');
usernameInput[0].classList.add('d-none');


usernameInput[0].innerHTML = 'some text or <p>HTML Tag</p>';
// or
usernameInput.html('some text or <p>HTML Tag</p>');
```

`IMPORTANT` The `loginForm` jQuery\<HTMLElement> object has an `attr()` method which is useful to obtain the destination url of a form element, specified in the action section.

resource: https://api.jquery.com/category/attributes/

```javascript
url: loginForm.attr('action'),
```

`IMPORTANT` The `loginForm` jQuery\<HTMLElement> object has a `serialize()` method which is useful in sending a POST ajax request.
```javascript
data: loginForm.serialize(),
```
