CREATE TABLE "vehiculos"(
    "id" BIGINT NOT NULL,
    "id_tipoVehiculo" BIGINT NULL,
    "placa" VARCHAR(10) NULL,
    "documento" VARCHAR(100) NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "hora_llegada" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT 'now()',
    "estado" BOOLEAN NOT NULL DEFAULT '1',
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT 'now()'
);
ALTER TABLE
    "vehiculos" ADD PRIMARY KEY("id");
CREATE TABLE "pagos"(
    "id" BIGINT NOT NULL,
    "id_vehiculo" BIGINT NOT NULL,
    "pago" BIGINT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT 'now()'
);
ALTER TABLE
    "pagos" ADD PRIMARY KEY("id");
CREATE TABLE "tipo_vehiculo"(
    "id" BIGINT NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "tarifa" FLOAT(8) NOT NULL,
    "limite" BIGINT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL DEFAULT 'now()'
);
ALTER TABLE
    "tipo_vehiculo" ADD PRIMARY KEY("id");
ALTER TABLE
    "vehiculos" ADD CONSTRAINT "vehiculos_id_tipovehiculo_foreign" FOREIGN KEY("id_tipoVehiculo") REFERENCES "tipo_vehiculo"("id");
ALTER TABLE
    "pagos" ADD CONSTRAINT "pagos_id_vehiculo_foreign" FOREIGN KEY("id_vehiculo") REFERENCES "vehiculos"("id");