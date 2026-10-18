<?php
// incluir la informacion del archivo conexion.php
include("conexion.php");

// mandamo a llamar la funcion conectar para poder conectarnos a la base de datos
$con = conectar();

//Todo lo que tenga de alumnos
$sql = "SELECT * FROM alumno";

// ejecutamos la consulta y tendremos acceso a la informacion de la tabla alumnos
$query = mysqli_query($con, $sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>TABLA DE ALUMNOS</h1>

    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>MATRICULA</th>
                <th>NOMBRE</th>
                <th>APELLIDO PATERNO</th>
                <th>APELLIDO MATERNO</th>
                <th>EDAD</th>
                <th>ACCIONES</th>
            </tr>

        </thead>
        <tbody>
            <?php
            while($row=mysqli_fetch_array($query)){
            ?>
            <tr>
                <td><?php echo $row['id']; ?></td>
                <td><?php echo $row['matricula']; ?></td>
                <td><?php echo $row['nombre']; ?></td>
                <td><?php echo $row['apellido_p']; ?></td>
                <td><?php echo $row['apellido_m']; ?></td>
                <td><?php echo $row['edad']; ?></td>
                <td>
                    Editar
                    <br>
                    Eliminar
                </td>
            </tr>
            <?php
            }
            ?>
        </tbody>
      
    </table>
    <h1>FORMULARIO</h1>
    <form action="insertar.php" method="post">
    <input type="text" class="form-control" name="matricula" placeholder="Matricula">
    <input type="text" class="form-control" name="nombre" placeholder="Nombre">
    <input type="text" class="form-control" name="apellido_p" placeholder="Apellido Paterno">
    <input type="text" class="form-control" name="apellido_m" placeholder="Apellido Materno">
    <input type="text" class="form-control" name="edad" placeholder="Edad">
    <button type="submit">Guardar</button>

    </form>
</body>
</html>