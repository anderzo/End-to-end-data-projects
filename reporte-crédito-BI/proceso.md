# estrucura
Credito{
    dashboard: aqui se guardaran los dashboard eschos en las distintas herramientas
    data_Sets: aqui se guardaran el csv crudo y los xlsx limpios
    especificaciones: aqui se guardaran el procedimiento, requerimiento y descripcion del proyecto
    ipynb: aaqui se guardaran scripst de limpieza y analisis exploratorio
    ML: aqui se guardar los modelos ml de prediccions ya sea en ipynb o en py
}

# para exploracion_#1.ipynb 
1- cargamos un data srt y vemos vemos los nulos en el data set con isna(), sin ebargo no se ven ya que el dataset contiene valores nulos pero no de tipo str entonces usamos otro metodo para verlos 
2- convertimos esos str a tipos nulos 
3- limpiamos datos= en salario lo K los cambiamos a numero para representar milecimas
4- quitamos el signo de la moneda $ para una mejor visualicion en los dashboard
5 en genero M y F nos aseguramos que solo sean mayusculas
6- finalmente lo exportamos a un archivo xlsx para su visualizacion en excel con los datos limpios
7- se cambiar los tipos de datos para limite_credito y otros que eran de tipo Float y estaban con tipo str   cadenas de texto

# para limp.ipynb 
1 - aqui hacemos la limpieza muy similiar a la anterior
2 - le agregos llenado de nulos con la moda de su respecticva colmna 
3 - preparamos los datos para crear un ML de predicion sobre el limite de credito y sobre default
4 - exportamos a un xlsx que se guardara en la carpeta data_sets

# modelo SVC
1- realice un ML SVC para ver que clientes caerian en mora con el mismp data set
2- entre el modelo a un 50% de los datos
3- use plotly para imprimir un grafico de correlacion
4- use Confusiondiplay para verificar la matris de confusion y verificar el modelo
5- exporte a fromato xlsx ya listo para realizar el dasbord con final

# metricas del dashboard
1- % de clientes en mora, default = 1
2- toral de clientes al dia defaul = 0
3- total de clientes
4- grafico todal de clientes por rango se salario
5- defaul por escolaridad
6- transacciones por tarjeta
7- evaluacion de mora o no, por rago de edad
8- grafico de dispercion
9- segmetadores como estado civil y genero
10- prediciones con modelo SVC (valore predecidos y % de diferecia)
11- diseño de tajetas con HTML content, graficos interativos y segmentadore

