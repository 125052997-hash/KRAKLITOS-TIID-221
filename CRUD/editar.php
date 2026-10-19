<?php

// Incluir la conexión a la base de datos
include("conexion.php");

// Conectarnos a la base de datos
$con = conectar();

// Obtener el ID del alumno
$id = $_GET['id'];

// Consultar los datos del alumno
$sql = "SELECT * FROM alumno WHERE id = '$id'";

// Ejecutar la consulta
$query = mysqli_query($con, $sql);

// Obtener los datos
$row = mysqli_fetch_array($query);

?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <h1>EDITAR ALUMNO</h1>

    <form action="actualizar.php" method="post">

        <input type="hidden" name="id"
        value="<?php echo $row['id']; ?>">

        <input type="text" name="matricula"
        placeholder="Matricula"
        value="<?php echo $row['matricula']; ?>">

        <input type="text" name="nombre"
        placeholder="Nombre"
        value="<?php echo $row['nombre']; ?>">

        <input type="text" name="apellido_p"
        placeholder="Apellido Paterno"
        value="<?php echo $row['apellido_p']; ?>">

        <input type="text" name="apellido_m"
        placeholder="Apellido Materno"
        value="<?php echo $row['apellido_m']; ?>">

        <input type="text" name="edad"
        placeholder="Edad"
        value="<?php echo $row['edad']; ?>">

        <button type="submit">Actualizar</button>

    </form>

    <br>
</body>

</html>