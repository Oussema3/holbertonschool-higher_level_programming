#!/usr/bin/node
const Script = 'C is fun';
const x = Number(process.argv[2]);

if (isNaN(x))  {
    console.log('Missing number of occurrences');
}
else {
    let v=0;
    while(v < x){
	console.log(Script);
	v++;
    }
}

    
