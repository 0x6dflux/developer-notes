# JavaScript

## JavaScript MIME Type
### Exception Traceback
```
The script from “http://127.0.0.1:5501/index.html” was loaded even though its MIME type (“text/html”) is not a valid JavaScript MIME type.
```

### Exception Explanation
This means that the server received an HTML file instead of a JavaScript file.   
Suppose you have:
```javascript
<script src="script.js"></script>
```
but, the server received this:
```html
<!DOCTYPE html>
<html>
...

<!-- This file maybe the 404 error. -->
```
Thus, the MIME type will be `text/html` and the browser says:  
`this is not a valid JavaScript MIME type`

### Exception Solution
#### Check the file path
```
project/
│
├── index.html
├── js/
│   └── script.js
```
```javascript
<script src="script.js"></script>
// this is wrong
```
```javascript
<script src="./js/script.js"></script>
// this is correct
```
If the file path is incorrect, the browser may receive the 404 page instead of JavaScript file.


# AJAX

## AJAX URL Exception
### Exception Traceback
```
Cannot GET /127.0.0.1:8000/shop/api/products/
```

### Exception Explanation
The FrontEnd server supposed that `/127.0.0.1:8000/shop/api/products/` is a path, not a complete url. The ajax part may contain the following:
```javascript
$.ajax({
    url: "127.0.0.1:8000/shop/api/products/",
});

// or

url: "127.0.0.1:8000/shop/api/products/"
```
So, the browser will send the request to the `http://127.0.0.1:5501/127.0.0.1:8000/shop/api/products/` which is not valid and will receive the 404 error.

### Exception Solution
#### Write the complete url
```javascript
url: "http://127.0.0.1:8000/shop/api/products/"

// or

url: "http://localhost:8000/shop/api/products/"

// note that
url: "http://127.0.0.1:8000//shop/api/products/"
// the above url does not raise an error
// but, it is better to remove the `//` after the port number
```


## CROS Exception
### Exception Traceback
```
Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://127.0.0.1:8000//shop/api/products/. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing). Status code: 200.
```

### Exception Explanation
The FrontEnd and BackEnd servers are not on a same origin.

### Exception Solution
<!-- Complete this -->