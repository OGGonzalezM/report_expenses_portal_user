# encoding: utf-8
# Created by Oscar Gonzalez at 8/08/18
# Created to expenses
import os
import io
import csv
import functools
import sys
import tempfile
import base64

from odoo import http
from odoo.http import request


class UpdateProductsData(http.Controller):

    @http.route('/website/update_product_data', type='http', auth='user', website=True, methods=['POST'])
    def update_products_data(self, products_file_data=None, **kwargs):
        if products_file_data.filename:

            print("\n Mi archivo fijo")
            archivo = '/odoo/custom/odoo_ogm/res.partner.csv'

            with open(archivo, 'rt', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(str(row['name']).encode('utf-8'))

            """
            for c_file in request.httprequest.files.getlist('products_file_data'):
                myfile = c_file.read()
                mycsv, path = tempfile.mkstemp(suffix='.csv', prefix='datos_productos')
                with os.fdopen(mycsv, 'rt') as products_file:
                    escritura = base64.b64encode(myfile)
                    towrite = escritura.decode('utf-8')
                    print("\n **********Data to write")
                    print(str(towrite).encode('utf-8'))
                    print ("\n *****************************Escritura realizada")
                    towrite = str(towrite).encode('utf-8')
                    products_file.write(towrite)
                    productos = csv.reader(open(products_file, 'w'))
                    if productos:
                        print (" \n -*-*-*-*-*-Mis productos  ")
                        print (productos)
                        for linea in productos:
                            print("------Linea de datos")
                            print(linea) """
            """try:
            except Exception as e:
                print("\n Ocurrio un error al leer el archivo")
                print(str(e)) """


