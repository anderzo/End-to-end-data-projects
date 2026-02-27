CREATE DATABASE mi_primera_bd;

CREATE TABLE Clientes (
    ID_Cliente int ,        
    Nombre VARCHAR(100),
	Apellido VARCHAR(100),
    Email TEXT UNIQUE, 
	Fecha_Registro date,
	Region VARCHAR(100),
	constraint ID_cliente_pk primary key (ID_cliente)
)

CREATE TABLE Categorias(
    ID_Categoria int ,        
    Categoria VARCHAR(100),
	Descripcion VARCHAR(100),
	constraint ID_Categoria_pk primary key (ID_Categoria)
)

CREATE TABLE Metodos_Pago (
    ID_Metodo_Pago int ,        
	Metodo_Pago VARCHAR(100),
	Descripcion VARCHAR(100),
	constraint ID_Metodo_Pago_pk primary key (ID_Metodo_Pago)
)

CREATE TABLE Productos (
    ID_Productos int ,        
	Nombre_Productos VARCHAR(100),
	Precio_unitario money,
	Stock int,
	ID_categoria int,
	constraint ID_Productos_pk primary key (ID_Productos),
	constraint ID_categoria_fk foreign key (ID_categoria) references Categorias(ID_Categoria) on delete cascade
)

CREATE TABLE Ventas(
    ID_Venta int ,        
	ID_Producto int,
	ID_Cliente int,
	Metodo_Pago int,
	Fecha date,
	Cantidad int,
	Estado varchar(100),
	constraint ID_Venta_pk primary key (ID_Venta),
	constraint ID_Producto_fk foreign key (ID_Producto) references Productos(ID_Productos) on delete cascade,
	constraint ID_Cliente_fk_ foreign key (ID_Cliente) references Clientes(ID_Cliente) on delete cascade,
	constraint ID_Metodo_Pago foreign key (Metodo_Pago) references Metodos_Pago(ID_Metodo_Pago) on delete cascade
)

ALTER TABLE metodos_pago
ALTER COLUMN descripcion TYPE TEXT;

select * from ventas


TRUNCATE TABLE ventas RESTART IDENTITY;

