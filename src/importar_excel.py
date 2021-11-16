# import os
# from flask import Flask, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename
# from flask import send_from_directory


# @app.route('/uploads/<name>')
# def download_file(name):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], name)



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
