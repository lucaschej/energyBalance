# -*- coding: utf-8 -*-

def read_value_from_dat_file(file_path):
    with open(file_path, 'r') as file:
        # Leer todas las líneas del archivo .dat
        lines = file.readlines()
        
        # Obtener el valor de la fila 4 y columna 5 (ten en cuenta que Python usa índices base 0)
        value = float(lines[3].split()[4])
        
    return value

def main():
    output_file = "output.dat"

    # Lista de archivos a procesar
    file_names = ["wallHeatFlux_1.dat", "wallHeatFlux_2.dat", "wallHeatFlux_3.dat", "wallHeatFlux_4.dat"]

    # Ruta de la carpeta contenedora de los archivos .dat
    folder_path = "postProcessing/metal/wallHeatFlux/0/"

    with open(output_file, 'w') as output:
        # Escribir la primera fila con los números de los archivos
        output.write("1 2 3 4\n")

        for file_name in file_names:
            # Construir la ruta completa al archivo
            file_path = folder_path + file_name

            # Leer el valor del archivo .dat actual
            value = read_value_from_dat_file(file_path)

            # Escribir el valor en el archivo de salida
            output.write(f"{value} ")

    print("Proceso completado. Los valores han sido guardados en 'output.dat'.")

if __name__ == "__main__":
    main()
