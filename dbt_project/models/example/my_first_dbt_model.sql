WITH mdl AS (
            SELECT cn.t_date,
                DATE_PART('year', cn.t_date) AS year,
                cn.ticker, 
                cn.weight, 
                e.e_score, 
                s.q_ending_total_return 
            
            FROM {{ source("public", "constituents") }} cn
                LEFT JOIN {{source("public","escores")}} e ON e.t_date = cn.t_date AND e.ticker= cn.ticker
                LEFT JOIN {{source("public","performance")}} s ON s.t_date = cn.t_date AND s.ticker = cn.ticker 
            )

SELECT ticker, 
	   t_date,
 	   e_score,
       AVG(e_score) OVER W AS rolling_average,
 	   COALESCE((STDDEV(e_score) OVER W),0) AS standard_deviation     

FROM mdl

WINDOW W AS (
		  	PARTITION BY ticker 
 		  	ORDER BY t_date ASC 
 		  	RANGE BETWEEN 
 		  	'1 year' PRECEDING 
 		  	AND CURRENT ROW 
 	  		)

