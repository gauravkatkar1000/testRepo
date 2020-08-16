CREATE VIEW BATCH_LIST_VW as select BATCH_ID, COUNT(SERIAL_ID) as TOTAL_TRUCKS, SUM(NET_WEIGHT_VAL) TOTAL_NET_WT, SUM(ACCPTED_BAGS) as TOTAL_ACCEPTED_BAGS, substr(MAX(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON)),0,11) as RELEASE_DATE , substr(MAX(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON)),11,6) as RELEASE_TIME,MIN(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON)) as START_DATE , CASE WHEN COUNT(SERIAL_ID)  >= AVG(TOTAL_TRUCKS_CNT) THEN "COMPLETE" ELSE "IN PROGRESS" END as STATUS   from WEIGHT_MST GROUP BY BATCH_ID

sqlite> pragma table_info(WEIGHT_MST_FCI_VW);
0|SERIAL_ID|INTEGER|0||0
1|CONTRACTOR_ID|INTEGER|0||0
2|CONTRACTOR_NAME|TEXT|0||0
3|MATERIAL_NAME|TEXT|0||0
4|GROSS_WT_VAL||0||0
5|TARE_WT_VAL||0||0
6|GROSS_WT_DATE||0||0
7|TARE_WT_DATE||0||0
8|STATUS|INTEGER|0||0
9|SERIAL_ID_DISPLY||0||0
10|NET_WEIGHT_VAL|INTEGER|0||0
11|VEHICLE_NO|TEXT|0||0
12|FIRST_WT_CRTEATED_ON|INTEGER|0||0
13|SECOND_WT_CREATED_ON|INTEGER|0||0
14|REMARK|text|0||0
15|MANNUAL_INS_FLG|text|0||0
16|DRIVER_IN_OUT|text|0||0
17|FIRST_WEIGHT_MODE|NUMERIC|0||0
18|FIRST_WEIGHT_VAL|NUMERIC|0||0
19|SECOND_WT_MODE|TEXT|0||0
20|SECOND_WT_VAL|INTEGER|0||0
21|CURR_TRUCK_CNT|INTEGER|0||0
22|TOTAL_TRUCKS_CNT|INTEGER|0||0
23|ACCPTED_BAGS|INTEGER|0||0
24|PROPOSED_BAGS|INTEGER|0||0
25|TARGET_STORAGE|TEXT|0||0
26|BATCH_ID|TEXT|0||0
27|ISSUE_ID|TEXT|0||0
400"