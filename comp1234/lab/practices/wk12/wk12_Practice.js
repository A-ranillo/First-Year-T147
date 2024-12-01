/*
    The if statement execute te block of code if the condition is satisfied.
    The following is the general syntax of the if statement.

        if (condition)
            statement(s);



let age = 18;

if (age < 18){ // condition is false
    document.write('Sorry you cannot sign up' + "<br>")// output is not displayed
}


let age = 18;

if (age >= 18){ // condition is false
    document.write('Sorry you cannot sign up' + "<br>")// output is not displayed
}

*/

// Nested if condition (generally avoid it)

// let minor_age = 16;
// let state = 'CA';

// if (state == 'CA') {
//     if (minor_age >= 16) {
//         document.write('you can drive');
//     }
// }

// let minor_age = 16;
// let state = 'CA';

// if(state == 'CA' && minor_ == 16) {
//     document.write('you can drive');
// }

// Functions
//  To declare a function, you use function keyword, followed by function name,
// a list of parameters and the function body as follows:

// general syntax:
    // function body
    // ...


// // A function can accept zero, one or multiple parameters.
// function say(){
//     // code an required information
// }

// function square(a){
//     result = a*a;
// }

// square(8)

// document.write('Square of 8' + result + '<br>')

// function add(a, b){
//      result = a + b;
// }

// add(15, 16);
// document.write('Addtion of 15 and 16 is ' + result + '<br>');

// let result;

// function compare(x,y){
//     if (x > y){ //if x > y then return -1
//         return -1;
//     } else if (x < y){
//         return 1; //if x < y then return 1
//     }
//     return 0;
// }


// result = compare (10, 4);
// document.write('x is greater thn y ' + result + "<br>")

// result = compare (1, 9);
// document.write('x is less thn y ' + result + "<br>")

// result = compare (15, 15);
// document.write('x is less thn y ' + result + "<br>")

// empty array
// const empty_array = [];

// // string array
// const string_array1= ['eat', 'work', 'sleep'];

// // number array
// const num_array = [5,2,15,22];

// // mixed array of different data types
// const mixed_array = ['hi', 33, true] //string_array1, number, boolean

// const myArray = ['H', 'e', 'l', 'l', 'o'];
// // lets output the first element from myArray
// document.write('The first element from my Array is: '+ myArray[0] + "<br>")//first Element
// document.write('The second element from my Array is: '+ myArray[1] + "<br>")//first Element
// document.write('The last element from my Array is: '+ myArray[4] + "<br>")//last Element
// document.write('referencing out of range elemt from myArray : ' + myArray[5] + "<br>") //undefiined element
// document.write('referencing out of range eleemtn from myArray : ' + myArray[5] + "<br>") //undefiined element

// let my_array_length = myArray.length;
// document.write('lenght of my Array: ' + my_array_length + "<br>") //# of elements    

// Loops for & while

// general syntax for 'for' loop
// for (initialization condition; update statement){
// block of code to execute

// const n = 5;
// let i = 1;
// for (let i = 1; i < n; i++){
//     document.write('Value of i is: ' + i + 'I love JavaScript' + "<br>")
// }

// document.write('Out of loop value of i is ' + i);

// white loop has one expression:
// condition -defines the loop stop condition
// while (condition){
// block of code to be executed.

// const grade = [79, 84, 92, 49, 33];
// let i = 0;

// while (i < grade.length){
//     document.write(grade[i] + "<br>");
//     i++;
// }

// // set population limit of aquarium to 10
// const popLimit = 10;

// // start off with 0 fish
// let fish = 0;

// // Initiate the while loop to run until fish reaches population limit

// while (fish < population){
//     // add one fish for each iteration
//     fish++;
//     document.write('There is room for ' + (popLimit-fish) + 'more fish' + "<br>")
// }

let myName = 'James Bond 007';

document.write("<div style='color: red; font-size: 10pt; position: fixed; top 10px; right: 10px;'>");
document.write('<strong><em> My name is</em></strong>' + myName);