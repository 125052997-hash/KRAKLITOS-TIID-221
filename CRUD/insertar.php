<?php
// incluir la informacion del archivo conexion.php
include("conexion.php");

// mandamo a llamar la funcion conectar para poder conectarnos a la base de datos
$con = conectar();

$matricula = $_POST['matricula'];
$nombre = $_POST['nombre'];
$apellido_paterno = $_POST['apellido_p'];
$apellido_materno = $_POST['apellido_m'];
$edad = $_POST['edad'];

/*crear nuestra consulta para insertar los datos a la base de datos */
$sql = "INSERT INTO alumno 
(matricula, nombre, apellido_p, apellido_m, edad) 
VALUES ('$matricula', '$nombre', '$apellido_paterno', '$apellido_materno', '$edad')";

/* Ejecutar la consulta */
$query = mysqli_query($con, $sql);

/*Comprobar y direccionar */
if($query){
    Header("Location: alumnos.php");

    }else{
        echo "No se pudo insertar el registro";
    }
?>
