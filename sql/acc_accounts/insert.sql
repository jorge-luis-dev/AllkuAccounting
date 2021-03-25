INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status)
VALUES(1, '1', 'ACTIVOS', 'Grupo', CURRENT_TIMESTAMP, 'Activo');

INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(2, '1.1', 'ACTIVOS CORRIENTES', 'Grupo', CURRENT_TIMESTAMP, 'Activo', 1);

INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(3, '1.1.1', 'Efectivo o Equivalente', 'Grupo', CURRENT_TIMESTAMP, 'Activo', 2);

INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(4, '1.1.1.01', 'Caja', 'Movimiento', CURRENT_TIMESTAMP, 'Activo', 3);
INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(5, '1.1.1.02', 'Banco', 'Grupo', CURRENT_TIMESTAMP, 'Activo', 3);
INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(6, '1.1.1.02.01', 'Banco Local', 'Movimiento', CURRENT_TIMESTAMP, 'Activo', 5);

INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(7, '1.1.2', 'Inversiones Financieras', 'Grupo', CURRENT_TIMESTAMP, 'Activo', 2);

INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(8, '1.1.2.01', 'Cuentas por cobrar', 'Movimiento', CURRENT_TIMESTAMP, 'Activo', 7);
INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(9, '1.1.2.02', 'Documentos por cobrar', 'Movimiento', CURRENT_TIMESTAMP, 'Activo', 7);
INSERT INTO acc_accounts
(id, code, "name", "type", date_created, status, account_id)
VALUES(10, '1.1.2.03', 'Provisión Cuentas Incobrables', 'Movimiento', CURRENT_TIMESTAMP, 'Activo', 7);
