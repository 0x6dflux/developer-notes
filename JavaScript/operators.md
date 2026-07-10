# Operators
resource: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators

## `++` and `--`
resource (`++`): https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment    
resource (`--`): https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement     

```javascript
console.log(1 / 0);  // Infinity
var a = 1;
console.log('a is:', a);  // a is: 1
console.log('a in console.log(a++); is:', a++);  // a in console.log(a++); is: 1
console.log('a after console.log(a++); is:', a);  // a after console.log(a++); is: 2 
a++;
console.log('a after a++; is:', a);  // a after a++; is: 3 
console.log('a in console.log(a--); is:', a--);  // a in console.log(a--); is: 3 
console.log('a after console.log(a--); is:', a);  // a after console.log(a--); is: 2

console.log('a is:', a);  // a is: 2
console.log('a is:', a += 1);  // a is: 3
console.log('a in console.log(++a); is:', ++a);  // a in console.log(++a); is: 4

```