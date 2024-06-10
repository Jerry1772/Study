function add(x, y) {
    let temp = x+y;
    return temp
}

console.log(add(1,2))

myArray = [1,2,3,4,5]
for(let i=0; i<10; i++) {
    if (i<5) {
        console.log(`문자열 포맷팅: ${myArray[4-i]}`)
    } else {
        console.log("pass")
    }
}

let tempSum = 0;
myArray.forEach(element => {
    console.log(element);
});
    