# Data Structures
or maybe `Standard built-in objects`  
resource: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

## Number
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number

## String
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String

## Array
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

## Object
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object


## Implicit Type Conversion
```javascript
const firstName = 'mahdi';
const lastName = 'mohammadi';
const fullName = firstName + ' ' + lastName;
console.log(fullName)  // mahdi mohammadi

const number1 = 4;
const number2 = 10;
const result = number1 + number2;
console.log(result);  // 14

const value = number1 - lastName;
console.log(value);  // NaN
// weak

let number3 = '10';
let number4 = '5';
const result2 = number3 - number4;
// this is where implicit type conversion happened
console.log(result2);  // 5
console.log(number3 * number4);  // 50
console.log(number3 / number4);  // 2
// for summation, the string concatenation is the priority
console.log(number3 + number4);  // 105
console.log(parseInt(number3) + parseInt(number4));  // 15
```

```javascript
console.log(4 + '5')  // "45"
console.log('5'+4)  // "54"
console.log(4+2+'3')  // "63"
console.log(4+'7'+9) // "479"
console.log(4+'7'+9+8)  // "4798"
console.log(4+2+'3'+6+4)  // "6364" 
```