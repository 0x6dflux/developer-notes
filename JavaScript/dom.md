# HTML Document Object Model (DOM)

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
`IMPORTANT` In the above form, the type of button has been set to `button` to handle a form that has nowhere to submit. Otherwise an error will be raised.

### JavaScript file
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


## Send an AJAX Request to BackEnd Server
```javascript
document.addEventListener('DOMContentLoaded', function () {
    // get the button element
    const loginBtn = document.querySelector('#login-btn');

    // wait or listen when the button is clicked
    loginBtn.addEventListener('click', function () {
        const loginForm = document.querySelector('#login-form');
        // get the form element

        // get the input element by its name
        // it is also possible to get these inputs by id
        const username = loginForm.querySelector('input[name="username"]');
        const password = loginForm.querySelector('input[name="password"]');

        if (username && password) {
            // get the input values
            const usernameValue = username.value;
            const passwordValue = password.value;
            
            // check whether they are empty or not
            if (!usernameValue || !passwordValue) {
                alert('username nad password required')
                // it is also possible to add a css class, e.g. red border by
                // password.classList.add('') 
            }
            else {
                // prepare data to be sent to the backend server
                const data = {
                    'username': usernameValue,
                    'password': passwordValue
                }
                // send request and send data in body
                // depending on your backend, csrf may be required
                // some drf projects exempt the csrf, some do not
            }
        }

    }); // end of loginBtn

}); // end of DOMContentLoaded

```