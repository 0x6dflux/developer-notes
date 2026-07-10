# Declaring Variables
### Follow `camelCase` rule for variable naming.
resource: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#declaring_variables

`const`: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const  
`var`: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var  
`let`: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let

```javascript
const a = 1;
var b = 2;
let c = 3;
```

```javascript
var b;
console.log(b); // undefined
```

## `var` vs `let`

### The main difference lies on the scoping rules
`let` is available only in the defined scope. if that variable is logged (`console.log()`) outside of the scope, a `ReferenceError` will be raised.

The variable which is defined by var, is also accessible outside of the defined scope.

### `Redeclaration` is another difference
```javascript
var a = 5;
console.log(a1);  // 5
var a = 10;
console.log(a1);  // 10

let b = 10;
console.log(b2);  // 10
let b = 15;
console.log(b2);  // Uncaught SyntaxError: redeclaration of let b2
```
### Another difference
do not know anything about this!!
```javascript
var foo = 'Foo';  // globally scoped
let bar = 'Bar';  // globally scoped
console.log(window.foo)  // Foo
console.log(window.bar)  // undefined
```