# Alter a Javascript function after declaring it

## 1
How about this, without having to redefine the function:

```
let a = function() { 
    return arguments.callee.value || 1; 
    };

alert(a()); // => 1
a.value = 2;
alert(a()); // => 2
```

## 2

You can do all kinds of fun stuff with javascript, including redefining functions:

```
let a = function(){ 
    return 1; 
    }

alert(a()); //1

// keep a reference
var old = a;

// redefine
a = function(){
  // call the original function with any arguments specified, storing the result
  var originalResult = old.apply(old, arguments);
  // add one
  return originalResult + 1;
};
alert(a()); //2
```
Voila.

Edit: Updated to show this in a crazier scenario:

```
var test = new String("123");
console.log(test.toString()); // logs 123
console.log(test.substring(0)); // logs 123
String.prototype.substring = function(){ return "hahanope"; }
console.log(test.substring(0)); // logs hahanope
```
You can see here that even though "test" is defined first, and we redefine substring() afterwards, the change still applies.

Side note: you really should reconsider your architecture if you're doing this...you're going to confuse the crap out of some poor developer 5 years down the road when s/he's looking at a function definition that's supposed to return 1, but seems to always return 2....


## 3

```
// declare function foo
let foo = function (a) { 
    alert(a); 
    };

// modify function foo
foo = new Function (
  "a",
  foo.toSource()
    .replace("alert(a)", "alert('function modified - ' + a)")
    .replace(/^function[^{]+{/i,"")  // remove everything up to and including the first curly bracket
    .replace(/}[^}]*$/i, "")  // remove last curly bracket and everything after<br>
);
```

- https://stackoverflow.com/questions/2136522/can-you-alter-a-javascript-function-after-declaring-it


## Partial Function 



## Currying 


- https://www.digitalocean.com/community/tutorials/javascript-functional-programming-explained-partial-application-and-currying
- https://medium.com/@JosephJnk/partial-function-application-in-javascript-and-flow-7f3ca87074fe
- https://towardsdatascience.com/javascript-currying-vs-partial-application-4db5b2442be8
