SELECT
    vehicle_location_history.vehicle_id,
    COUNT(*) AS Poor_GPS_Quality_Events,
    vehicles.operating_center
FROM vehicle_location_history
LEFT JOIN vehicles
    ON vehicle_location_history.vehicle_id = vehicles.vehicle_id
WHERE vehicle_location_history.gps_quality IN (0, 1)
    AND vehicles.operating_center IS NOT NULL
    AND vehicle_location_history.recorded_at > DATEADD(DAY, -90, GETDATE())
GROUP BY
    vehicle_location_history.vehicle_id,
    vehicles.operating_center
ORDER BY
    Poor_GPS_Quality_Events DESC;
