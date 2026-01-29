CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
	email VARCHAR(254) UNIQUE NOT NULL,
	phone_number VARCHAR(15) UNIQUE,
	password VARCHAR(255) NOT NULL,
	is_admin BOOLEAN DEFAULT FALSE,
	is_active BOOLEAN DEFAULT TRUE,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS tokens (
	id SERIAL PRIMARY KEY,
	user_id INT UNIQUE NOT NULL,
	token VARCHAR(40) NOT NULL UNIQUE,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_token_user
		FOREIGN KEY (user_id)
		REFERENCES users(id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS customers (
	id SERIAL PRIMARY KEY,
	user_id INT UNIQUE NOT NULL,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(10),
	photo TEXT,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_customers_user
		FOREIGN KEY (user_id)
		REFERENCES users(id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS providers (
	id SERIAL PRIMARY KEY,
	user_id INT UNIQUE NOT NULL,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(10),
	description VARCHAR(500),
	photo TEXT UNIQUE,
	verified BOOLEAN DEFAULT FALSE,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_providers_user
		FOREIGN KEY (user_id)
		REFERENCES users(id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS documents (
	id SERIAL PRIMARY KEY,
	provider_id INT NOT NULL,
	document_type VARCHAR(30) NOT NULL,
	document_number VARCHAR(50) NOT NULL UNIQUE,
	file_name TEXT NOT NULL,
	status VARCHAR(20) NOT NULL DEFAULT 'Pending',
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_documents_provider
		FOREIGN KEY (provider_id)
		REFERENCES providers(id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS services (
	id SERIAL PRIMARY KEY,
	provider_id INT NOT NULL,
	title VARCHAR(100) DEFAULT 'Service through CitySewa',
	service_type VARCHAR(50) NOT NULL,
	description TEXT,
	price INT NOT NULL,
	price_unit VARCHAR(20),
	archived BOOLEAN DEFAULT FALSE,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_services_provider
		FOREIGN KEY (provider_id)
		REFERENCES providers(id)
		ON DELETE CASCADE
);

CREATE TABLE districts (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE locations (
	id SERIAL PRIMARY KEY,
	area VARCHAR(100) NOT NULL,
	ward INT NOT NULL,
	city VARCHAR(50) NOT NULL,
	district_id INT NOT NULL,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_locations_district
		FOREIGN KEY (district_id)
		REFERENCES districts(id)
		ON DELETE CASCADE
);

CREATE TABLE addresses (
	id SERIAL PRIMARY KEY,
	user_id INT NOT NULL,
	location_id INT NOT NULL,
	landmarks VARCHAR(150) NOT NULL,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_addresses_user
		FOREIGN KEY (user_id)
		REFERENCES users(id)
		ON DELETE CASCADE,
	CONSTRAINT fk_addresses_location
		FOREIGN KEY (location_id)
		REFERENCES locations(id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS bookings (
	id SERIAL PRIMARY KEY,
	service_id INT NOT NULL,
	customer_id INT NOT NULL,
	address_id INT NOT NULL,
	booking_date DATE NOT NULL,
	booking_time TIME NOT NULL,
	status VARCHAR(20) DEFAULT 'PENDING',
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	CONSTRAINT fk_bookings_service
		FOREIGN KEY (service_id)
		REFERENCES services(id)
		ON DELETE CASCADE,
	CONSTRAINT fk_bookings_customer
		FOREIGN KEY (customer_id)
		REFERENCES customers(id)
		ON DELETE CASCADE,
	CONSTRAINT fk_bookings_address
		FOREIGN KEY (address_id)
		REFERENCES addresses(id)
);
