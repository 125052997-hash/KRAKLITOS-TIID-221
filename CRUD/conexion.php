<?php

/*Creamos una funcion llamada conectar */
function conectar() {
    /*informacion del servidor */
    $host = "localhost";
    $user = "root";
    $pass = "";


    /*Base de datos: */
    $db = "221";

    /*Permite conectar MyQL */
    $con=mysqli_connect($host, $user, $pass);

    /*no se ve la proyeccion  */
    mysqli_select_db($con, $db);
    return $con;
}
?>