CREATE OR REPLACE VIEW v_acc_accounts
AS with recursive rec_accounts as (
select
	id,
	code,
	name,
	name as location,
	type,
	status,
	account_id 
from
	acc_accounts
where
	account_id is null
union all
select
	l.id ,
	l.code,
	l.name,
	rec_accounts.location || ' - ' || l.name,
	l.type,
	l.status,
	l.account_id 
from
	acc_accounts l
join rec_accounts on
	l.account_id = rec_accounts.id 
)
select
	id, 
	code,
	name, 
	replace (location, ' - ' || name, '') as location , 
	type, 
	status, 
	account_id
from
	rec_accounts;
