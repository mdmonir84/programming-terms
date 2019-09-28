<?php
/*
FirstClass Function example
*/

$input = [1, 2, 3, 4, 5, 6];

// Creates a new anonymous function and assigns it to a variable
// $filter_even = function($item) {
//     return ($item % 2) == 0;
// };
//
// // Built-in array_filter accepts both the data and the function
// $output = array_filter($input, $filter_even);

// The function doesn't need to be assigned to a variable. This is valid too:
$output = array_filter($input, function($item) {
    return ($item % 2) == 0;
});

print_r($output);


/*
A closure is an anonymous function that can access variables imported from the outside scope without using any global variables. Theoretically, a closure is a function with some arguments closed (e.g. fixed) by the environment when it is defined. Closures can work around variable scope restrictions in a clean way.

In the next example we use closures to define a function returning a single filter function for array_filter(), out of a family of filter functions.
*/


/**
 * Creates an anonymous filter function accepting items > $min
 *
 * Returns a single filter out of a family of "greater than n" filters
 */
function criteria_greater_than($min)
{
    return function($item) use ($min) {
        return $item > $min;
    };
}

$input = [1, 2, 3, 4, 5, 6];

// Use array_filter on a input with a selected filter function
$output = array_filter($input, criteria_greater_than(3));

print_r($output); // items > 3
