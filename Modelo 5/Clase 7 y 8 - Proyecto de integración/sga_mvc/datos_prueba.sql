-- Datos de prueba para el Sistema de Gestión Académica (SGA)

-- Insertar Docentes
INSERT INTO docentes (nombre, correo) VALUES
('Juan Perez', 'juan.perez@universidad.edu'),
('Maria Garcia', 'maria.garcia@universidad.edu'),
('Carlos Rodriguez', 'carlos.rodriguez@universidad.edu'),
('Ana Martinez', 'ana.martinez@universidad.edu'),
('Luis Hernandez', 'luis.hernandez@universidad.edu');

-- Insertar Programas
INSERT INTO programas (nombre, duracion, docente_id) VALUES
('Ingenieria de Software', 8, 1),
('Ciencia de Datos', 6, 2),
('Desarrollo Web', 4, 1),
('Inteligencia Artificial', 6, 3),
('Ciberseguridad', 5, 4),
('Bases de Datos', 3, 5);

-- Insertar Alumnos
INSERT INTO alumnos (nombre, correo, programa_id) VALUES
('Pedro Lopez', 'pedro.lopez@estudiante.edu', 1),
('Laura Sanchez', 'laura.sanchez@estudiante.edu', 1),
('Diego Torres', 'diego.torres@estudiante.edu', 2),
('Sofia Ramirez', 'sofia.ramirez@estudiante.edu', 2),
('Miguel Flores', 'miguel.flores@estudiante.edu', 3),
('Carmen Diaz', 'carmen.diaz@estudiante.edu', 3),
('Roberto Morales', 'roberto.morales@estudiante.edu', 4),
('Elena Castro', 'elena.castro@estudiante.edu', 4),
('Fernando Ruiz', 'fernando.ruiz@estudiante.edu', 5),
('Patricia Gomez', 'patricia.gomez@estudiante.edu', 5),
('Andres Vargas', 'andres.vargas@estudiante.edu', 1),
('Gabriela Mendoza', 'gabriela.mendoza@estudiante.edu', 2);

-- Insertar Notas
INSERT INTO notas (alumno_id, asignatura, calificacion) VALUES
(1, 'Programacion I', 4.5),
(1, 'Matematicas Discretas', 4.2),
(1, 'Bases de Datos', 4.8),
(1, 'Algoritmos', 4.0),
(2, 'Programacion I', 5.0),
(2, 'Matematicas Discretas', 4.7),
(2, 'Bases de Datos', 4.9),
(2, 'Algoritmos', 4.8),
(3, 'Python para Data Science', 4.6),
(3, 'Estadistica', 4.3),
(3, 'Machine Learning I', 4.5),
(3, 'Visualizacion de Datos', 4.4),
(4, 'Python para Data Science', 4.8),
(4, 'Estadistica', 4.9),
(4, 'Machine Learning I', 5.0),
(4, 'Visualizacion de Datos', 4.7),
(5, 'HTML y CSS', 4.2),
(5, 'JavaScript', 4.0),
(5, 'React', 3.8),
(5, 'Node.js', 4.1),
(6, 'HTML y CSS', 4.9),
(6, 'JavaScript', 4.7),
(6, 'React', 4.8),
(6, 'Node.js', 4.6),
(7, 'Redes Neuronales', 4.3),
(7, 'Deep Learning', 4.1),
(7, 'NLP', 4.4),
(7, 'Computer Vision', 4.2),
(8, 'Redes Neuronales', 4.7),
(8, 'Deep Learning', 4.5),
(8, 'NLP', 4.6),
(8, 'Computer Vision', 4.8),
(9, 'Seguridad de Redes', 4.0),
(9, 'Criptografia', 3.9),
(9, 'Ethical Hacking', 4.2),
(9, 'Analisis Forense', 4.1),
(10, 'Seguridad de Redes', 4.5),
(10, 'Criptografia', 4.6),
(10, 'Ethical Hacking', 4.7),
(10, 'Analisis Forense', 4.4),
(11, 'Programacion I', 3.5),
(11, 'Matematicas Discretas', 3.8),
(11, 'Bases de Datos', 4.0),
(12, 'Python para Data Science', 5.0),
(12, 'Estadistica', 4.8),
(12, 'Machine Learning I', 4.9);
