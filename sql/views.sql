DROP VIEW IF EXISTS avg_temp_por_dispositivo;
DROP VIEW IF EXISTS leituras_por_hora;
DROP VIEW IF EXISTS temp_max_min_por_dia;

CREATE VIEW avg_temp_por_dispositivo AS
SELECT 
    device_id,
    AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;

CREATE VIEW leituras_por_hora AS
SELECT 
    EXTRACT(HOUR FROM timestamp) AS hora,
    COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

CREATE VIEW temp_max_min_por_dia AS
SELECT 
    DATE(timestamp) AS data,
    MAX(temperature) AS temp_max,
    MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY DATE(timestamp)
ORDER BY data;