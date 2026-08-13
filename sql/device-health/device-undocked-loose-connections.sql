SELECT
    P.vehicle_id,
    P.Loose_Connection_Event,
    Q.operating_center
FROM (
    SELECT
        vehicle_id,
        COUNT(*) AS Loose_Connection_Event
    FROM device_events
    WHERE device_events.event_type = 'Device Undocked'
      AND device_events.created_at >= DATEADD(DAY, -30, GETDATE())
    GROUP BY vehicle_id
    HAVING COUNT(*) > 30
) AS P
LEFT JOIN vehicles AS Q
    ON P.vehicle_id = Q.vehicle_id
WHERE Q.operating_center IS NOT NULL
ORDER BY P.Loose_Connection_Event DESC;
