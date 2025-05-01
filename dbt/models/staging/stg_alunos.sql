select *
from {{ source('academia_etl', 'alunos_raw') }}