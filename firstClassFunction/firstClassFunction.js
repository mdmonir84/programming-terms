
/*
Assigning  function as variable
*/

// function square(x) {
//   return x*x;
// }
//
// let f = square;
//
// console.log(square);
// console.log(f);
// console.log(f(5));


/*
Accepting function as args
*/

// function square(x) {
//   return x*x;
// }
//
// function cube(x){
//     return x*x*x;
// }
//
// function my_map(func, args){
//   result =[];
//   for(let arg of args){
//     result.push(func(arg));
//   }
//   return result;
// }
//
// let squares = my_map(square, [1,2,3,4,5]);
// console.log(squares);
//
// let cubes = my_map(cube, [1,2,3,4,5]);
// console.log(cubes);


/*
return a function from another function
*/

/*
Example-1
*/
// function logger(msg){
//   function log_message() {
//     console.log('Log: '+msg);
//   }
//   return log_message;
// }
//
// log_hi = logger('Hi!');
// log_hi();

/*
Example-2
*/
function html_tag(tag){
  function wrap_text(msg) {
    console.log('<'+tag+ '>'+msg+'</'+tag+'>');
  }
  return wrap_text;
}

print_h1 = html_tag('h1');
print_h1('Test Headline');
print_h1('Another Headline');

print_h1 = html_tag('p');
print_h1('Test Paragraph');
