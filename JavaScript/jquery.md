send request to a backend server

other applications (e.g. to interact with the page), which requires a good understanding of javascript (need time)

it is also possible to send a request to a backend server using javascript, but, using jquery is better, clean, and easy to debug.

# jQuery
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