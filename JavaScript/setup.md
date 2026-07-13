# Set Up

## VS Code Extensions
- HTML CSS Support by ecmel
- Live Server by Ritwick Dey

## Type 1

### index.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script>
        console.log('hello');
        alert('hello');
    </script>
</body>

</html>
```

## Type 2

### index.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script src="home.js"></script>
</body>

</html>
```

### home.js
```javascript
console.log('hello');
alert('hello');
```


## Add jQuery File
```html
<body>
    ...

    <!-- follow the order of import -->
    <script src='jquery_3.5.1.min.js'></script>
    <!-- import bootstrap js files -->
    <!-- import other javascript files -->
</body>
```

`IMPORTANT` Do not use jquery slim version `https://code.jquery.com/jquery-4.0.0.slim.min.js`, it does not have AJAX.   

`IMPORTANT` Write your AJAX request in another JavaScript file and add an script tag at the end of your imports.
