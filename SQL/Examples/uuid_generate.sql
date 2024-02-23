-- 1. Enable third part UUID extension first

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Generate a sample UUID value first

-- 2.1. UUID Version 1 (Time-based): Generated based on the current timestamp and the node (usually the MAC address) of the machine.
-- Structure: xxxxxxxx-xxxx-1xxx-xxxx-xxxxxxxxxxxx.

SELECT uuid_generate_v1() AS generated_uuid;

-- 2.2. UUID Version 2 (DCE Security): Similar to Version 1 but includes POSIX UID/GID and POSIX timestamps.

SELECT uuid_generate_v2() AS generated_uuid;

-- 2.3. UUID Version 3 (Name-based, MD5): Generated based on a namespace UUID and a name (using MD5 hash).
-- Structure: xxxxxxxx-xxxx-3xxx-xxxx-xxxxxxxxxxxx.

SELECT uuid_generate_v3() AS generated_uuid;

-- 2.4. UUID Version 4 (Random): Generated using random or pseudo-random numbers.
-- Structure: xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx.

SELECT uuid_generate_v4() AS generated_uuid;

-- 2.5. UUID Version 5 (Name-based, SHA-1): Similar to Version 3 but uses SHA-1 hash instead of MD5.
-- Structure: xxxxxxxx-xxxx-5xxx-xxxx-xxxxxxxxxxxx.

SELECT uuid_generate_v5() AS generated_uuid;

-- 3. Create a table using UUID

CREATE TABLE table_uuid(
	product_id UUID DEFAULT uuid_generate_v1(),
	product_name VARCHAR(100) not null
);

-- 4. Alter UUID default value

ALTER TABLE table_uuid
ALTER COLUMN product_id
SET DEFAULT uuid_generate_v4();