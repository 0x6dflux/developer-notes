# Asynchronous JavaScript And XML (AJAX)

## Template
### Type 1 - Preferred
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

                $.ajax({
                    url: 'http://localhost:8004/',
                    type: 'POST',
                    data: JSON.stringify({ "username": "test" }),
                    contentType: 'application/json',
                    dataType: 'json',
                    success: function (data) { },
                    error: function (rs, e) { }
                });
                
            }
        }

    }); // end of loginBtn

}); // end of DOMContentLoaded

```

### Type 2 - Old
It is possible to add an `onclick` event on the HTML tag. Note that, there are other `on<event>`.
```html
<button onclick='submitLoginForm(event)'>
```
```javascript
function submitLoginForm(event) {
    // lots of valuable info will be stored in the event, which a PointerEvent
    // one of useful attribute is target which gives the html element
    console.log(event.target)
}
```