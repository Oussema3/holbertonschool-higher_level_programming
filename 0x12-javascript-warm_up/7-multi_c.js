#!/usr/bin/node
const Script = 'C is fun';
const i = Number(process.argv[2]);

if (isNaN(i))  {
    console.log('Missing number of occurrences');
}
else {
    let v=0;
    while(v < i){
	console.log(Script);
	v++;
    }
}

    
