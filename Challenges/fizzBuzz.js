for (let i = 1; i <= 100; i++){
    let out = '';
    if (i % 3 == 0) out += 'Fizz';
    if (i % 5 == 0) out += 'Buzz';
    console.log(out || i);
}

function FizzBuzz(aTarget) {
    for (var i = 1; i <= aTarget; i++) {
        var result = "";
        if (i%3 === 0) result += "Fizz";        
        if (i%5 === 0) result += "Buzz";
        if (result.length ===0) result = i;

        console.log(result);
    }
}