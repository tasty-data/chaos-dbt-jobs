SELECT
	date,
	service,
	sum(unblendedcost)::NUMERIC(16,2) AS cost
FROM
	(
	SELECT
		date,
		service ,
		unblendedcost
	FROM
		{{ ref('aws_chaos_billing_2023_01_01_2023_05_01') }}
    where unblendedcost > 0
    ) a
GROUP BY
	date, service
ORDER BY
	date, service
