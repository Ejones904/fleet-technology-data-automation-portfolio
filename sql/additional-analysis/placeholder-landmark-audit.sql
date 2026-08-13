SELECT DISTINCT
    dispatch.created_datetime,
    dispatch.operating_center,
    dispatch_stops.dispatch_number,
    landmark_audit.landmark_id,
    landmark_audit.customer_id,
    landmark_audit.name,
    landmark_audit.description
FROM landmark_audit
LEFT JOIN dispatch_stops
    ON landmark_audit.landmark_id = dispatch_stops.landmark_id
LEFT JOIN dispatch
    ON dispatch_stops.dispatch_number = dispatch.dispatch_number
WHERE command_type = 'Placeholder'
AND dispatch.operating_center IS NOT NULL;
