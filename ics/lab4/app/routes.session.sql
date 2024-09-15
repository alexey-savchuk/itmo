CREATE TABLE "routes" (
    "id" INTEGER PRIMARY KEY,
    "origin" TEXT,
    "destination" TEXT,
    "schedule" TEXT
);

DROP TABLE "routes"

INSERT INTO
    "routes" ("origin", "destination", "schedule")
VALUES
    ('Санкт-Петербург', 'Пушкин', '0 7 * * *'),   -- at  7 am every day
    ('Гатчина', 'Санкт-Петербург', '0 7 * * *'),   -- at 12 pm on Sat. and Sun.
    ('Санкт-Петербург', 'Петергоф', '0 6 */5 * *') -- at  6 am on every 5th day-of-month

SELECT
    "id",
    "origin",
    "destination",
    "schedule"
FROM
    "routes"
WHERE
    "id" =
;
