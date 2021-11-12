# <?php
#     if(is_array($_FILES['archivoexcel']) && count($_FILES['archivoexcel'])>0){
#         require_once 'src/PHPExcel.php';
#         require_once 'conexion.php';

#         $tmpfname = $_FILES['archivoexcel']['tmkp_name'];
#         //Crear el excel para leerlo luego
#         $leerexcel = PHPExcel_IOFactory::createReaderForLine($tmpfname);
#         //Cargar el excel
#         $excelobj = $leerexcel ->load($tmpfname);

#     }
# ?>