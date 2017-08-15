// Javascript 101 by samKhoo

/*
multi-line commenting
*/ 


// variables and data types
var var1 = 'yellow friend'; // NEED TO 'SUPPRESS' W/ SEMI-COLON
var var2 = 1;
var var3 = 1.1;
var var4 = true;
var var5 = false;

// konkatinasi "uncle sam"
combovar = var1+var2; // no need to convert string
document.write(combovar+"<br>"+combovar); // print out stuff
alert('something wong with '+var1+' :('); // unless you wanna alert someone, remove this
console.log('meh.'); // ONLY for DEBUGGING

//===========================================================================
/* Expressions and operators



*/
//===========================================================================

// Conditional statements (if, ifelse etc.)
var condiOne = 5;
var condiTwo = 10;
var condiThree = 100;

if(condiOne == condiTwo || condiTwo == condiThree)
{
	document.write('your dps is insufficient');
}

else if(condiOne < condiTwo && condiTwo < condiThree)
{
	document.write('happy day (cause your dps doesn\'t suck now)');
}

else
{
	document.write('ding ding ding. we have our MVP here');
}


// ARRAYS YO
var arraySatu = [1,3];
document.write(arraySatu);

// looping
for (i=0; i<5; i++)	// (variable, condition, looping increment)

{
	// code to loop
}


function coolBeans(cool)
{
	document.write('I is '+cool+'.');
}


inputverb = 'kewl';
coolBeans(inputverb);