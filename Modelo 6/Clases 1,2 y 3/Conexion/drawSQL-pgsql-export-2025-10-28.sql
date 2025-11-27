-- Eliminar tablas si existen
DROP TABLE IF EXISTS "pagos" CASCADE;
DROP TABLE IF EXISTS "vehiculos" CASCADE;
DROP TABLE IF EXISTS "tipo_vehiculo" CASCADE;

-- Eliminar secuencias si existen
DROP SEQUENCE IF EXISTS tipo_vehiculo_id_seq;
DROP SEQUENCE IF EXISTS vehiculos_id_seq;
DROP SEQUENCE IF EXISTS pagos_id_seq;

-- Crear secuencias
CREATE SEQUENCE tipo_vehiculo_id_seq START 1;
CREATE SEQUENCE vehiculos_id_seq START 1;
CREATE SEQUENCE pagos_id_seq START 1;

-- Crear tabla tipo_vehiculo
CREATE TABLE "tipo_vehiculo"(
    "id" BIGINT NOT NULL DEFAULT nextval('tipo_vehiculo_id_seq'),
    "nombre" VARCHAR(100) NOT NULL,
    "tarifa" FLOAT(8) NOT NULL,
    "limite" BIGINT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
);
ALTER TABLE "tipo_vehiculo" ADD PRIMARY KEY("id");

-- Crear tabla vehiculos
CREATE TABLE "vehiculos"(
    "id" BIGINT NOT NULL DEFAULT nextval('vehiculos_id_seq'),
    "id_tipovehiculo" BIGINT NULL,
    "placa" VARCHAR(10) NULL,
    "documento" VARCHAR(100) NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "hora_llegada" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
    "estado" BOOLEAN NOT NULL DEFAULT TRUE,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
);
ALTER TABLE "vehiculos" ADD PRIMARY KEY("id");

-- Crear tabla pagos
CREATE TABLE "pagos"(
    "id" BIGINT NOT NULL DEFAULT nextval('pagos_id_seq'),
    "id_vehiculo" BIGINT NOT NULL,
    "pago" BIGINT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
);
ALTER TABLE "pagos" ADD PRIMARY KEY("id");

-- Agregar foreign keys
ALTER TABLE "vehiculos" ADD CONSTRAINT "vehiculos_id_tipovehiculo_foreign" 
    FOREIGN KEY("id_tipovehiculo") REFERENCES "tipo_vehiculo"("id");

ALTER TABLE "pagos" ADD CONSTRAINT "pagos_id_vehiculo_foreign" 
    FOREIGN KEY("id_vehiculo") REFERENCES "vehiculos"("id");

-- Insertar datos de ejemplo (tipos de vehículos)
INSERT INTO tipo_vehiculo (nombre, tarifa, limite) VALUES
    ('Moto', 2000, 30),
    ('Auto', 3000, 20),
    ('Camioneta', 4000, 15),
    ('Camión', 5000, 10);

-- Mensaje de confirmación
SELECT 'Base de datos creada exitosamente!' as mensaje;