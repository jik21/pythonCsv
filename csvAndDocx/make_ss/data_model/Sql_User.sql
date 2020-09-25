--SQL Server
SELECT  c.TABLE_NAME, c.COLUMN_NAME,c.DATA_TYPE, c.character_maximum_length, (cast(c.numeric_precision as varchar)+','+cast(c.numeric_scale as varchar)) as num_len, c.is_nullable
             ,CASE WHEN pk.COLUMN_NAME IS NOT NULL THEN 'Y' ELSE 'N' END AS isPK
FROM INFORMATION_SCHEMA.COLUMNS c
LEFT JOIN (
            SELECT ku.TABLE_CATALOG,ku.TABLE_SCHEMA,ku.TABLE_NAME,ku.COLUMN_NAME
            FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc
            INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS ku
                ON tc.CONSTRAINT_TYPE = 'PRIMARY KEY' 
                AND tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME
         )   pk 
ON  c.TABLE_CATALOG = pk.TABLE_CATALOG
            AND c.TABLE_SCHEMA = pk.TABLE_SCHEMA
            AND c.TABLE_NAME = pk.TABLE_NAME
            AND c.COLUMN_NAME = pk.COLUMN_NAME
ORDER BY c.TABLE_SCHEMA,c.TABLE_NAME, c.ORDINAL_POSITION 


--Oracle
select Table_name,Column_name,Data_type,Data_length, (to_char(NVL(Data_Precision,0)) || ',' || to_char(NVL(Data_SCALE,0))) as numLen, nullable,
(case when exists (select 1 from all_constraints cons, all_cons_columns cols
WHERE cons.constraint_type = 'P'
AND cons.constraint_name = cols.constraint_name
AND cons.owner = cols.owner
and cols.OWNER='PCPS'
and cols.table_name = atc.table_name
and cols.column_name = atc.Column_name) then 'Y'
else 'N' end) as pk
from 
ALL_TAB_COLUMNS atc where owner = 'PCPS' and 
table_name not in (select view_name from all_views where owner = 'PCPS')
order by TAble_name,COLUMN_ID;