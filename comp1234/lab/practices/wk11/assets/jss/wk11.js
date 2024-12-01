alert('message from wk11.js');

// 
/*

there are 8 baisc data types in JavaScript.

Seven primitive data types:
    numbers for number of any kind: integer, floating-point
    bigint for integer number for arbitary length.
    string for strings. A string may have zero or more characters.
     Note: there's no single-character data type like in C or Java.
    boolean is for True orFlase.
    null for unknown values - a standalone type that has a single value null.
    undefined for unassigned values - a standalone that has a single value undefined.
    symbol for unique indentifers
    And one non primitive data type:
        object for more complex data structures.

    
    typeof operator allows us to see which type of data is stored in a variable.

*/

let message = 'Hello';
message = 123456789;

// number type represents both integer and folating point numbers.

let n = 123;

n = 12.345;

//besides regular numbers, there are so called "special numeric values" which also belong to this data type:


// alert(1/0); //infinity

// NaN represents a computational error. It is a result of an incorrect or undefined math operation.
// alert('not a number'/2); NaN such a division is erroneous

// alert(NaN + 1) //NaN
// alert(3 * NaN) //NaN

//  embed a variable

let str = "Hello";
let str2 = 'Single quotes are ok too';
let phrase = `can embed another ${str}`;
// document.write(phrase);

let isGreater = 4 > 1;
// alert(isGreater);

birthday = undefined;
// alert(birthday);

const PI = 3.14;

document.write('Value of pi is ' +PI)

PI = 9.8;

document.write('Value of pi is ' +PI)