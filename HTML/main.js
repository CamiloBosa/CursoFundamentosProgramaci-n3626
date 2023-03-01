    	alert("Hola mundo")

var nombre= "carlos días";
var edad= 46
var estatura=140

var concatenar= nombre+" "+edad;

document.write(concatenar);

/*
document.write(nombre);
document.write(edad);
document.write(estatura);
*/

var datos= document.getElementById("datos");
//datos.innerHTML =concatenar;

datos.innerHTML= `
    <h1> Estos son los datos </h1>
    <h2> Mi nombre: ${nombre} </h2>
    <h3> Edad: ${edad} años</h3>
    <h3> Estatura: ${estatura} cm</h3>

`;
 

