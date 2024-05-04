CREATE TYPE week_days AS enum ('MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN');
ALTER TYPE week_days OWNER TO postgres;

CREATE TYPE genders AS enum ('MALE', 'FEMALE', 'OTHERS');
ALTER TYPE genders OWNER TO postgres;

CREATE TYPE doc_types AS enum ('CPF', 'CNPJ');
ALTER TYPE doc_types OWNER TO postgres;

CREATE TABLE IF NOT EXISTS job_categories
(
    id   serial PRIMARY KEY,
    name VARCHAR NOT NULL
);
ALTER TABLE
    job_categories
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS jobs
(
    id          serial PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES job_categories,
    name        VARCHAR NOT NULL
);
ALTER TABLE
    jobs
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS workers
(
    id              uuid DEFAULT gen_random_uuid() NOT NULL PRIMARY KEY,
    first_name      VARCHAR(50)                    NOT NULL,
    last_name       VARCHAR(50)                    NOT NULL,
    gender          genders                        NOT NULL,
    business_name   VARCHAR(50)                    NOT NULL,
    job_id          INTEGER                        NOT NULL REFERENCES jobs,
    email           VARCHAR(255)                   NOT NULL UNIQUE,
    phone           CHAR(15)                       NOT NULL UNIQUE,
    doc_num         VARCHAR(14)                    NOT NULL UNIQUE,
    doc_type        doc_types                      NOT NULL,
    profile_pic_url VARCHAR                        NOT NULL
);
ALTER TABLE
    workers
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS expedients
(
    worker_id  uuid      NOT NULL REFERENCES workers,
    week_day   week_days NOT NULL,
    start_time TIME      NOT NULL,
    end_time   TIME      NOT NULL,
    PRIMARY KEY (worker_id, week_day)
);
ALTER TABLE
    expedients
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS workers_login
(
    worker_id     uuid     NOT NULL
        PRIMARY KEY
        REFERENCES public.workers,
    hash_password CHAR(64) NOT NULL,
    salt          uuid     NOT NULL
);

ALTER TABLE workers_login
    OWNER TO postgres;