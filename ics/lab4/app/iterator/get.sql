SELECT
    "id",
    "origin",
    "destination",
    "schedule"
FROM
    "routes"
WHERE
    "id" = ?
;
