<?php

// Incluir la conexión
include("conexion.php");

// Conectarnos a la base de datos
$con = conectar();

// Obtener los datos del formulario
$id = $_POST['id'];
$matricula = $_POST['matricula'];
$nombre = $_POST['nombre'];
$apellido_paterno = $_POST['apellido_p'];
$apellido_materno = $_POST['apellido_m'];
$edad = $_POST['edad'];

// Actualizar los datos del alumno
$sql = "UPDATE alumno SET
        matricula = '$matricula',
        nombre = '$nombre',
        apellido_p = '$apellido_paterno',
        apellido_m = '$apellido_materno',
        edad = '$edad'
        WHERE id = '$id'";

// Ejecutar la consulta
$query = mysqli_query($con, $sql);

// Comprobar el resultado
if ($query) {

    header("Location: alumnos.php");
    exit();

} else {

    echo "No se pudo actualizar el registro";

}

?>