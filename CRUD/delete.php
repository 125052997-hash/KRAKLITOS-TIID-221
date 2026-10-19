<?php
// incluir la informacion del archivo conexion.php
include("conexion.php");

// mandamo a llamar la funcion conectar para poder conectarnos a la base de datos
$con = conectar();

$id = $_GET[ 'id' ];

$sql = "DELETE FROM alumno WHERE id = '$id'";

$query = mysqli_query($con, $sql);

if($query){
    header("Location: alumnos.php");
    exit();
} else {
    echo "Error al eliminar el alumno: " . mysqli_error($con);
}
?>