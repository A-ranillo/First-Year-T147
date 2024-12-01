// Delear and Output student information including lab session day
document.write('<strong>' + 'Student ID: ' + '</strong>' + '101475343 ');
document.write('<strong>' + 'Full Name: ' + '</strong>' + 'Philip Bezalel Asher Ranillo' + '<br>');
document.write('<strong>' + 'Lab Proffessor: ' + '</strong>' + 'Azzad Kara ');
document.write('<strong>' + 'Student ID: ' + '</strong>' + 'Week 13');

function part2(num1, num2) {
    // Assign the return value to a variable named _return
    let _return = '';
    // Your code should start here
    // check num1 and 2
   if (num1>num2){
    _return = 2;
   }else if (num1<num2){// check num1 and 2
    _return = 1;
   }else if (num1=num2){// check num1 and 2
    _return = 0;
   }
    /* Your code ends here.
       Don't add or change anything after this line.*/
    return _return;
}

function part3(num1, num2) {
    // Assign the return value to a variable named _return
    let _return = '';
    // Your code should start here
    if (num1<num2){// check num1 and 2
        for (let i = num1; i <= num2; i++){
            _return += i;
        }
    }else if (num1>num2){// check num1 and 2
        for (let i = num1; i >= num2; i--){
            _return += i;
        }
    }else{//if other stuff in the above doesnt work.
        _return = num1+num2;
    }
  
    /* Your code ends here.
       Don't add or change anything after this line.*/
    return _return;
}


function part4(array_index, array) {
    // Assign the return value to a variable named _return
    let _return = '';
    // Your code should start here
    if (array_index >= 0 && array_index < array.length){//checks if the array length is 0 and if the array_index is smaller than array.length
        _return = true;
    }else{//all else false above
        _return = false;
    }

    /* Your code ends here.
       Don't add or change anything after this line.*/
    return _return;
}


function part5(array) {
    // Assign the return value to a variable named _return
    let _return = '';
    // Your code should start here

    for (let i = 0; i < array.length; i++){//it loops the exact length of the array.
        if (array[i] % 2 == 0){//checks value inside of the array if its even
            _return += array[i];
        }
    }
    if (array.length == 0 || _return == ''){//all else fails
        _return = 0;
    }

    /* Your code ends here.
       Don't add or change anything after this line.*/
    return _return;
}


