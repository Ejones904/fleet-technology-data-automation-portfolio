SELECT
    operating_locations.location_name,
    ds.driver_login,
    d.driver_name,
    ds.vehicle_id,
    ds.login_time,
    ds.logout_time,
    ds.login_odometer,
    ds.logout_odometer
FROM driver_sessions AS ds
LEFT JOIN drivers AS d
    ON ds.driver_login = d.driver_login
LEFT JOIN operating_locations
    ON d.home_location_id = operating_locations.location_id
WHERE ds.login_time IS NOT NULL
    AND ds.login_time > DATEADD(DAY, -7, GETDATE())
    AND ds.logout_time IS NULL
    AND ds.status = '0'
    AND d.driver_status = '1'
ORDER BY
    operating_locations.location_name ASC,
    ds.insert_datetime ASC;
