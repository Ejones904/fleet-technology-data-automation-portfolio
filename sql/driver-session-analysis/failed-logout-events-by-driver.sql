SELECT
    operating_locations.location_name,
    drivers.driver_login,
    drivers.driver_name,
    driver_sessions.vehicle_id,
    driver_sessions.login_time,
    driver_sessions.logout_time,
    DATEDIFF(hour, driver_sessions.login_time, driver_sessions.logout_time) AS Login_Duration,
    DATEPART(WEEKDAY, login_time) AS Day_of_Week,
    COUNT(CASE WHEN DATEDIFF(hour, driver_sessions.login_time, driver_sessions.logout_time) > 16
        THEN 1 ELSE NULL END) OVER(PARTITION BY drivers.driver_name) AS Failed_Logout_Events_Count,
    COUNT(CASE WHEN DATEDIFF(hour, driver_sessions.login_time, driver_sessions.logout_time) > 16
        THEN 1 ELSE NULL END) OVER(PARTITION BY operating_locations.location_name) AS Failed_Logout_Events_By_DC
FROM driver_sessions
LEFT JOIN drivers
    ON driver_sessions.driver_login = drivers.driver_login
LEFT JOIN operating_locations
    ON drivers.home_location = operating_locations.location_id
WHERE DATEDIFF(hour, driver_sessions.login_time, driver_sessions.logout_time) > 16
    AND drivers.driver_name IS NOT NULL
    AND login_time > DATEADD(day, -7, GETDATE())
ORDER BY
    operating_locations.location_name ASC,
    Failed_Logout_Events_Count DESC,
    Day_of_Week DESC,
    insert_datetime DESC;
