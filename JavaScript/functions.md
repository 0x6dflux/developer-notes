# Functions

## Structure
```javascript
function <name>(<parameters>){
    // expressions;

    return <output>
}
```

### Anonymous Function
```javascript
<let, var, const> <functionName> = function(<parameters>){
    // expressions;

    return <output>
}
```

### Arrow Function
```javascript
// type 1
// multi expressions

<let, var, const> <functionName> = (<parameters>){
    // expressions;

    return <output>
}


// type 2
// one expression
<let, var, const> <functionName> = (<parameters>)=>  // one expression;
```

### Examples
```javascript
// function hello(var name) wrong, javascript handle that
function hello(firstName, lastName){
    console.log('hello ' + firstName + ' ' + lastName);
}

hello('mahdi', 'mohammadi');  // hello mahdi mohammadi
```

All javascript functions will return `undefined`.

```javascript
function hello(firstName, lastName){
    console.log('hello ' + firstName + ' ' + lastName);
}

let someVariable = hello('mahdi', 'mohammadi');
console.log(someVariable)  // undefined
```

```javascript
const hello = function(){
    return 'helloWorld'
}

console.log(hello())  // helloWorld
```

```javascript
function mySum(num1, num2){
    return num1 + num2
}

console.log(mySum(1, 2))  // 3

// or

const add = (num1, num2) => num1 + num2;
console.log(mySum(1, 2))  // 3
```
