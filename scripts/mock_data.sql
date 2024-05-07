INSERT INTO job_categories(name)
VALUES ('generic_category');

INSERT INTO jobs (category_id, name)
VALUES (1, 'generic_job');

INSERT INTO workers(id, first_name, last_name, gender, business_name, job_id, email, phone, doc_num, doc_type,
                    profile_pic_url)
VALUES ('481f35cb-3dbe-4336-a7ce-751809944b6e', 'carlos', 'adalberto', 'MALE', 'chaveiro arruda', 1, 'carlos@email.com',
        '11988776655', '11122233344', 'CPF', NULL);

INSERT INTO workers_login(worker_id, hashed_password, salt)
VALUES ('481f35cb-3dbe-4336-a7ce-751809944b6e', '2c06a2dd4f685882c2e3088c26906882241203c9c2ce3733b44cee3a5ae719c3',
        '53f995c7-45eb-4bcf-bb94-a1ed84e5ba7d');


INSERT INTO expedients(worker_id, week_day, start_time, end_time)
VALUES ('481f35cb-3dbe-4336-a7ce-751809944b6e', 'MON', '8:30', '18:00');
