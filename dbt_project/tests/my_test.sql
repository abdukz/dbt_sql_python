SELECT *
FROM {{ ref("my_first_dbt_model") }}
WHERE standard_deviation IS NOT NULL 