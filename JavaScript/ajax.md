# Asynchronous JavaScript And XML (AJAX)

## Template
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
