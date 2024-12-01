let Name = prompt('Enter your Name please','Your Name Please')
let ID = prompt('Enter Your Student Number please','Student ID')
let Limit = prompt('Enter a number: 1-9')
let LimitCheck = 0;
let Conditioner = 0;
let myString = 1;
let LimitCheck2 = 0;

while(isNaN(ID)){
    ID = prompt('Enter Your Student Number please','Student ID')
}

while (isNaN(Limit)){
    Limit = prompt('Enter a number: 1-9');
}

while(LimitCheck2 == 0){
    if(Limit >= 10 || Limit <= 0){
        Limit = prompt('Enter a number: 1-9');
        LimitCheck2 = 0;
    }
    else{
        LimitCheck2 = 1;
    }
}

document.write("<strong>" + 'My name is: ' + "</strong>" + Name+ "<br>");
document.write("<strong>" + 'My Student ID is: '  + "</strong>" + ID+ "<br>");
document.write("<br>");
document.write(myString+"<br>");
Limit = Limit - 1;
while (Conditioner < Limit){
    Conditioner++;
    SubConditioner = Conditioner + 1;
    myString = myString * 10 + SubConditioner;
    document.write(myString+"<br>");
}