---
title: "Use summary data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-views/summary-data"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-views"
created_at: "2026-06-23T20:42:52.824695+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use summary data

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- Admin

This use case is to help you understand how to use summary data in your reporting and analysis. The use case details all the steps that are required to use summary data in Customer Journey Analytics:

- [Ingest](#ingest) summary data and other data sources in Experience Platform.
- Set up your [Connection](#connection) for the summary data and other data sources.
- Configure your [Data view](#data-view) to combine your data sources.
- Report and analyze in [Workspace](#workspace) on your combined data.

The use case provides sample data for summary data, event data and lookup data. All data contains random values.

## Ingest

You use the following sample summary data for this use case, showing summary data for running campaigns on Facebook.

Summary data
| table 0-row-8 1-row-8 2-row-8 3-row-8 4-row-8 5-row-8 6-row-8 7-row-8 8-row-8 9-row-8 10-row-8 11-row-8 12-row-8 13-row-8 14-row-8 15-row-8 16-row-8 17-row-8 18-row-8 3-align-right 4-align-right 12-align-right 13-align-right 21-align-right 22-align-right 30-align-right 31-align-right 39-align-right 40-align-right 48-align-right 49-align-right 57-align-right 58-align-right 66-align-right 67-align-right 75-align-right 76-align-right 84-align-right 85-align-right 93-align-right 94-align-right 102-align-right 103-align-right 111-align-right 112-align-right 120-align-right 121-align-right 129-align-right 130-align-right 138-align-right 139-align-right 147-align-right 148-align-right 156-align-right 157-align-right 165-align-right 166-align-right |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| _id | campaign_name | cost | impression | campaign_id | network | ad_group | timestamp |
| 1 | 123 Campaign | 100 | 5000 | abc123 | facebook | abc-adgroup | 2024-07-18T18:20:39.000Z |
| 2 | 123 Campaign | 50 | 4000 | def123 | facebook | def-adgroup | 2024-07-18T18:20:39.000Z |
| 3 | 123 Campaign | 125 | 6000 | ghi123 | facebook | ghi-adgroup | 2024-07-18T18:20:39.000Z |
| 4 | 456 Campaign | 25 | 2500 | abc456 | facebook | abc-adgroup | 2024-07-18T18:20:39.000Z |
| 5 | 456 Campaign | 10 | 1000 | def456 | facebook | def-adgroup | 2024-07-18T18:20:39.000Z |
| 6 | 456 Campaign | 115 | 5500 | ghi456 | facebook | ghi-adgroup | 2024-07-18T18:20:39.000Z |
| 7 | 789 Campaign | 200 | 9000 | abc789 | facebook | abc-adgroup | 2024-07-18T18:20:39.000Z |
| 8 | 789 Campaign | 20 | 2000 | def789 | facebook | def-adgroup | 2024-07-18T18:20:39.000Z |
| 9 | 789 Campaign | 225 | 12000 | ghi789 | facebook | ghi-adgroup | 2024-07-18T18:20:39.000Z |
| 10 | 987 Campaign | 125 | 10000 | abc987 | facebook | abc-adgroup | 2024-07-18T18:20:39.000Z |
| 11 | 987 Campaign | 120 | 15000 | def987 | facebook | def-adgroup | 2024-07-18T18:20:39.000Z |
| 12 | 987 Campaign | 315 | 22500 | ghi987 | facebook | ghi-adgroup | 2024-07-18T18:20:39.000Z |
| 13 | 654 Campaign | 325 | 20000 | abc654 | facebook | abc-adgroup | 2024-07-18T18:20:39.000Z |
| 14 | 654 Campaign | 320 | 25000 | def654 | facebook | def-adgroup | 2024-07-18T18:20:39.000Z |
| 15 | 654 Campaign | 315 | 22500 | ghi654 | facebook | ghi-adgroup | 2024-07-18T18:20:39.000Z |
| 16 | 321 Campaign | 25 | 2000 | abc321 | facebook | abc-adgroup | 2024-07-18T18:20:39.000Z |
| 17 | 321 Campaign | 20 | 2500 | def321 | facebook | def-adgroup | 2024-07-18T18:20:39.000Z |
| 18 | 321 Campaign | 15 | 2250 | ghi321 | facebook | ghi-adgroup | 2024-07-18T18:20:39.000Z |

[Download sample summary data](assets/summary-data)

To use the summary data in Customer Journey Analytics, in a report or as part of analyzing data in Workspace, you need

- a summary schema in Experience Platform,
- a summary dataset in Experience Platform,
- a connection in Customer Journey Analytics configured to use the summary dataset,
- a data view in Customer Journey Analytics, correctly configured with metrics and dimensions for the summary data.

You use this summary data alongside a dataset for event data and a dataset for lookup data.

Event data
Event data is available in the Example Event Data Dataset. The sample data looks like:

| table 0-row-7 1-row-7 2-row-7 3-row-7 4-row-7 5-row-7 6-row-7 7-row-7 8-row-7 9-row-7 10-row-7 11-row-7 12-row-7 13-row-7 14-row-7 15-row-7 16-row-7 17-row-7 18-row-7 19-row-7 20-row-7 21-row-7 22-row-7 23-row-7 24-row-7 25-row-7 26-row-7 27-row-7 28-row-7 29-row-7 30-row-7 31-row-7 32-row-7 33-row-7 34-row-7 35-row-7 36-row-7 37-row-7 38-row-7 39-row-7 40-row-7 41-row-7 42-row-7 43-row-7 44-row-7 45-row-7 46-row-7 47-row-7 48-row-7 49-row-7 50-row-7 51-row-7 52-row-7 53-row-7 54-row-7 55-row-7 56-row-7 57-row-7 58-row-7 59-row-7 60-row-7 61-row-7 62-row-7 63-row-7 64-row-7 65-row-7 66-row-7 67-row-7 68-row-7 69-row-7 70-row-7 71-row-7 72-row-7 73-row-7 74-row-7 75-row-7 76-row-7 77-row-7 78-row-7 79-row-7 80-row-7 81-row-7 82-row-7 83-row-7 84-row-7 85-row-7 86-row-7 87-row-7 88-row-7 89-row-7 90-row-7 91-row-7 92-row-7 93-row-7 94-row-7 95-row-7 96-row-7 97-row-7 98-row-7 99-row-7 100-row-7 101-row-7 102-row-7 103-row-7 104-row-7 105-row-7 106-row-7 107-row-7 108-row-7 109-row-7 110-row-7 111-row-7 112-row-7 113-row-7 114-row-7 115-row-7 116-row-7 117-row-7 118-row-7 119-row-7 120-row-7 121-row-7 122-row-7 123-row-7 124-row-7 125-row-7 126-row-7 127-row-7 128-row-7 129-row-7 130-row-7 131-row-7 132-row-7 133-row-7 134-row-7 135-row-7 136-row-7 137-row-7 138-row-7 139-row-7 140-row-7 141-row-7 142-row-7 143-row-7 144-row-7 145-row-7 146-row-7 147-row-7 148-row-7 149-row-7 150-row-7 151-row-7 152-row-7 153-row-7 154-row-7 155-row-7 156-row-7 157-row-7 158-row-7 159-row-7 160-row-7 161-row-7 162-row-7 163-row-7 164-row-7 165-row-7 166-row-7 167-row-7 168-row-7 169-row-7 170-row-7 171-row-7 172-row-7 173-row-7 174-row-7 175-row-7 176-row-7 177-row-7 178-row-7 179-row-7 2-align-right 6-align-right 7-align-right 10-align-right 14-align-right 15-align-right 18-align-right 22-align-right 23-align-right 26-align-right 30-align-right 31-align-right 34-align-right 38-align-right 39-align-right 42-align-right 46-align-right 47-align-right 50-align-right 54-align-right 55-align-right 58-align-right 62-align-right 63-align-right 66-align-right 70-align-right 71-align-right 74-align-right 78-align-right 79-align-right 82-align-right 86-align-right 87-align-right 90-align-right 94-align-right 95-align-right 98-align-right 102-align-right 103-align-right 106-align-right 110-align-right 111-align-right 114-align-right 118-align-right 119-align-right 122-align-right 126-align-right 127-align-right 130-align-right 134-align-right 135-align-right 138-align-right 142-align-right 143-align-right 146-align-right 150-align-right 151-align-right 154-align-right 158-align-right 159-align-right 162-align-right 166-align-right 167-align-right 170-align-right 174-align-right 175-align-right 178-align-right 182-align-right 183-align-right 186-align-right 190-align-right 191-align-right 194-align-right 198-align-right 199-align-right 202-align-right 206-align-right 207-align-right 210-align-right 214-align-right 215-align-right 218-align-right 222-align-right 223-align-right 226-align-right 230-align-right 231-align-right 234-align-right 238-align-right 239-align-right 242-align-right 246-align-right 247-align-right 250-align-right 254-align-right 255-align-right 258-align-right 262-align-right 263-align-right 266-align-right 270-align-right 271-align-right 274-align-right 278-align-right 279-align-right 282-align-right 286-align-right 287-align-right 290-align-right 294-align-right 295-align-right 298-align-right 302-align-right 303-align-right 306-align-right 310-align-right 311-align-right 314-align-right 318-align-right 319-align-right 322-align-right 326-align-right 327-align-right 330-align-right 334-align-right 335-align-right 338-align-right 342-align-right 343-align-right 346-align-right 350-align-right 351-align-right 354-align-right 358-align-right 359-align-right 362-align-right 366-align-right 367-align-right 370-align-right 374-align-right 375-align-right 378-align-right 382-align-right 383-align-right 386-align-right 390-align-right 391-align-right 394-align-right 398-align-right 399-align-right 402-align-right 406-align-right 407-align-right 410-align-right 414-align-right 415-align-right 418-align-right 422-align-right 423-align-right 426-align-right 430-align-right 431-align-right 434-align-right 438-align-right 439-align-right 442-align-right 446-align-right 447-align-right 450-align-right 454-align-right 455-align-right 458-align-right 462-align-right 463-align-right 466-align-right 470-align-right 471-align-right 474-align-right 478-align-right 479-align-right 482-align-right 486-align-right 487-align-right 490-align-right 494-align-right 495-align-right 498-align-right 502-align-right 503-align-right 506-align-right 510-align-right 511-align-right 514-align-right 518-align-right 519-align-right 522-align-right 526-align-right 527-align-right 530-align-right 534-align-right 535-align-right 538-align-right 542-align-right 543-align-right 546-align-right 550-align-right 551-align-right 554-align-right 558-align-right 559-align-right 562-align-right 566-align-right 567-align-right 570-align-right 574-align-right 575-align-right 578-align-right 582-align-right 583-align-right 586-align-right 590-align-right 591-align-right 594-align-right 598-align-right 599-align-right 602-align-right 606-align-right 607-align-right 610-align-right 614-align-right 615-align-right 618-align-right 622-align-right 623-align-right 626-align-right 630-align-right 631-align-right 634-align-right 638-align-right 639-align-right 642-align-right 646-align-right 647-align-right 650-align-right 654-align-right 655-align-right 658-align-right 662-align-right 663-align-right 666-align-right 670-align-right 671-align-right 674-align-right 678-align-right 679-align-right 682-align-right 686-align-right 687-align-right 690-align-right 694-align-right 695-align-right 698-align-right 702-align-right 703-align-right 706-align-right 710-align-right 711-align-right 714-align-right 718-align-right 719-align-right 722-align-right 726-align-right 727-align-right 730-align-right 734-align-right 735-align-right 738-align-right 742-align-right 743-align-right 746-align-right 750-align-right 751-align-right 754-align-right 758-align-right 759-align-right 762-align-right 766-align-right 767-align-right 770-align-right 774-align-right 775-align-right 778-align-right 782-align-right 783-align-right 786-align-right 790-align-right 791-align-right 794-align-right 798-align-right 799-align-right 802-align-right 806-align-right 807-align-right 810-align-right 814-align-right 815-align-right 818-align-right 822-align-right 823-align-right 826-align-right 830-align-right 831-align-right 834-align-right 838-align-right 839-align-right 842-align-right 846-align-right 847-align-right 850-align-right 854-align-right 855-align-right 858-align-right 862-align-right 863-align-right 866-align-right 870-align-right 871-align-right 874-align-right 878-align-right 879-align-right 882-align-right 886-align-right 887-align-right 890-align-right 894-align-right 895-align-right 898-align-right 902-align-right 903-align-right 906-align-right 910-align-right 911-align-right 914-align-right 918-align-right 919-align-right 922-align-right 926-align-right 927-align-right 930-align-right 934-align-right 935-align-right 938-align-right 942-align-right 943-align-right 946-align-right 950-align-right 951-align-right 954-align-right 958-align-right 959-align-right 962-align-right 966-align-right 967-align-right 970-align-right 974-align-right 975-align-right 978-align-right 982-align-right 983-align-right 986-align-right 990-align-right 991-align-right 994-align-right 998-align-right 999-align-right 1002-align-right 1006-align-right 1007-align-right 1010-align-right 1014-align-right 1015-align-right 1018-align-right 1022-align-right 1023-align-right 1026-align-right 1030-align-right 1031-align-right 1034-align-right 1038-align-right 1039-align-right 1042-align-right 1046-align-right 1047-align-right 1050-align-right 1054-align-right 1055-align-right 1058-align-right 1062-align-right 1063-align-right 1066-align-right 1070-align-right 1071-align-right 1074-align-right 1078-align-right 1079-align-right 1082-align-right 1086-align-right 1087-align-right 1090-align-right 1094-align-right 1095-align-right 1098-align-right 1102-align-right 1103-align-right 1106-align-right 1110-align-right 1111-align-right 1114-align-right 1118-align-right 1119-align-right 1122-align-right 1126-align-right 1127-align-right 1130-align-right 1134-align-right 1135-align-right 1138-align-right 1142-align-right 1143-align-right 1146-align-right 1150-align-right 1151-align-right 1154-align-right 1158-align-right 1159-align-right 1162-align-right 1166-align-right 1167-align-right 1170-align-right 1174-align-right 1175-align-right 1178-align-right 1182-align-right 1183-align-right 1186-align-right 1190-align-right 1191-align-right 1194-align-right 1198-align-right 1199-align-right 1202-align-right 1206-align-right 1207-align-right 1210-align-right 1214-align-right 1215-align-right 1218-align-right 1222-align-right 1223-align-right 1226-align-right 1230-align-right 1231-align-right 1234-align-right 1238-align-right 1239-align-right 1242-align-right 1246-align-right 1247-align-right 1250-align-right 1254-align-right 1255-align-right 1258-align-right 1262-align-right 1263-align-right 1266-align-right 1270-align-right 1271-align-right 1274-align-right 1278-align-right 1279-align-right 1282-align-right 1286-align-right 1287-align-right 1290-align-right 1294-align-right 1295-align-right 1298-align-right 1302-align-right 1303-align-right 1306-align-right 1310-align-right 1311-align-right 1314-align-right 1318-align-right 1319-align-right 1322-align-right 1326-align-right 1327-align-right 1330-align-right 1334-align-right 1335-align-right 1338-align-right 1342-align-right 1343-align-right 1346-align-right 1350-align-right 1351-align-right 1354-align-right 1358-align-right 1359-align-right 1362-align-right 1366-align-right 1367-align-right 1370-align-right 1374-align-right 1375-align-right 1378-align-right 1382-align-right 1383-align-right 1386-align-right 1390-align-right 1391-align-right 1394-align-right 1398-align-right 1399-align-right 1402-align-right 1406-align-right 1407-align-right 1410-align-right 1414-align-right 1415-align-right 1418-align-right 1422-align-right 1423-align-right 1426-align-right 1430-align-right 1431-align-right 1434-align-right 1438-align-right 1439-align-right |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| timestamp | _id | page_name | person_id | tracking_code | orders | revenue_amount |
| 2024-07-18T19:15:39+00:00 | 1 | home page | person-1abc123 | abc123 |  |  |
| 2024-07-18T19:15:39+00:00 | 2 | confirmation page | person-1abc123 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 3 | home page | person-2def123 | def123 |  |  |
| 2024-07-18T19:15:39+00:00 | 4 | home page | person-3ghi123 | ghi123 |  |  |
| 2024-07-18T19:15:39+00:00 | 5 | confirmation page | person-3ghi123 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 6 | home page | person-4abc456 | abc456 |  |  |
| 2024-07-18T19:15:39+00:00 | 7 | home page | person-5def456 | def456 |  |  |
| 2024-07-18T19:15:39+00:00 | 8 | home page | person-6ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 9 | confirmation page | person-6ghi456 |  | 1 | 159.25 |
| 2024-07-18T19:15:39+00:00 | 10 | home page | person-7abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 11 | home page | person-8def789 | def789 |  |  |
| 2024-07-18T19:15:39+00:00 | 12 | home page | person-9ghi789 | ghi789 |  |  |
| 2024-07-18T19:15:39+00:00 | 13 | confirmation page | person-9ghi789 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 14 | home page | person-10abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 15 | home page | person-11def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 16 | home page | person-12ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 17 | home page | person-13abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 18 | home page | person-14def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 19 | home page | person-15ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 20 | confirmation page | person-15ghi654 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 21 | home page | person-16abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 22 | home page | person-17def321 | def321 |  |  |
| 2024-07-18T19:15:39+00:00 | 23 | home page | person-18ghi321 | ghi321 |  |  |
| 2024-07-18T19:15:39+00:00 | 24 | home page | person-19abc123 | abc123 |  |  |
| 2024-07-18T19:15:39+00:00 | 25 | home page | person-20def123 | def123 |  |  |
| 2024-07-18T19:15:39+00:00 | 26 | home page | person-21ghi123 | ghi123 |  |  |
| 2024-07-18T19:15:39+00:00 | 27 | confirmation page | person-21ghi123 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 28 | home page | person-22abc456 | abc456 |  |  |
| 2024-07-18T19:15:39+00:00 | 29 | home page | person-23def456 | def456 |  |  |
| 2024-07-18T19:15:39+00:00 | 30 | home page | person-24ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 31 | home page | person-25abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 32 | confirmation page | person-25abc789 |  | 1 | 139.25 |
| 2024-07-18T19:15:39+00:00 | 33 | home page | person-26abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 34 | home page | person-27def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 35 | home page | person-28ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 36 | home page | person-29abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 37 | confirmation page | person-29abc654 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 38 | home page | person-30def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 39 | home page | person-31ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 40 | home page | person-32abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 41 | home page | person-33ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 42 | confirmation page | person-33ghi456 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 43 | home page | person-34abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 44 | home page | person-35def789 | def789 |  |  |
| 2024-07-18T19:15:39+00:00 | 45 | home page | person-36ghi789 | ghi789 |  |  |
| 2024-07-18T19:15:39+00:00 | 46 | confirmation page | person-36ghi789 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 47 | home page | person-37abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 48 | home page | person-38def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 49 | home page | person-39ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 50 | home page | person-40abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 51 | confirmation page | person-40abc654 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 52 | home page | person-41def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 53 | home page | person-42ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 54 | home page | person-43abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 55 | home page | person-44def321 | def321 |  |  |
| 2024-07-18T19:15:39+00:00 | 56 | home page | person-45ghi321 | ghi321 |  |  |
| 2024-07-18T19:15:39+00:00 | 57 | home page | person-46abc123 | abc123 |  |  |
| 2024-07-18T19:15:39+00:00 | 58 | confirmation page | person-46abc123 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 59 | home page | person-47def123 | def123 |  |  |
| 2024-07-18T19:15:39+00:00 | 60 | home page | person-48ghi123 | ghi123 |  |  |
| 2024-07-18T19:15:39+00:00 | 61 | home page | person-49abc456 | abc456 |  |  |
| 2024-07-18T19:15:39+00:00 | 62 | home page | person-50def456 | def456 |  |  |
| 2024-07-18T19:15:39+00:00 | 63 | home page | person-51ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 64 | home page | person-52abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 65 | confirmation page | person-52abc789 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 66 | home page | person-53abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 67 | home page | person-54def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 68 | home page | person-55ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 69 | confirmation page | person-55ghi987 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 70 | home page | person-56abc123 | abc123 |  |  |
| 2024-07-18T19:15:39+00:00 | 71 | home page | person-57def123 | def123 |  |  |
| 2024-07-18T19:15:39+00:00 | 72 | confirmation page | person-57def123 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 73 | home page | person-58ghi123 | ghi123 |  |  |
| 2024-07-18T19:15:39+00:00 | 74 | home page | person-59abc456 | abc456 |  |  |
| 2024-07-18T19:15:39+00:00 | 75 | confirmation page | person-59abc456 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 76 | home page | person-60def456 | def456 |  |  |
| 2024-07-18T19:15:39+00:00 | 77 | home page | person-61ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 78 | home page | person-62abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 79 | confirmation page | person-62abc789 |  | 1 | 159.25 |
| 2024-07-18T19:15:39+00:00 | 80 | home page | person-63def789 | def789 |  |  |
| 2024-07-18T19:15:39+00:00 | 81 | home page | person-64ghi789 | ghi789 |  |  |
| 2024-07-18T19:15:39+00:00 | 82 | home page | person-65abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 83 | confirmation page | person-65abc987 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 84 | home page | person-66def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 85 | home page | person-67ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 86 | home page | person-68abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 87 | home page | person-69def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 88 | home page | person-70ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 89 | home page | person-71abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 90 | confirmation page | person-71abc321 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 91 | home page | person-72def321 | def321 |  |  |
| 2024-07-18T19:15:39+00:00 | 92 | home page | person-73ghi321 | ghi321 |  |  |
| 2024-07-18T19:15:39+00:00 | 93 | home page | person-74abc123 | abc123 |  |  |
| 2024-07-18T19:15:39+00:00 | 94 | home page | person-75def123 | def123 |  |  |
| 2024-07-18T19:15:39+00:00 | 95 | home page | person-76ghi123 | ghi123 |  |  |
| 2024-07-18T19:15:39+00:00 | 96 | home page | person-77abc456 | abc456 |  |  |
| 2024-07-18T19:15:39+00:00 | 97 | confirmation page | person-77abc456 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 98 | home page | person-78def456 | def456 |  |  |
| 2024-07-18T19:15:39+00:00 | 99 | home page | person-79ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 100 | home page | person-80abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 101 | home page | person-81abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 102 | confirmation page | person-81abc987 |  | 1 | 139.25 |
| 2024-07-18T19:15:39+00:00 | 103 | home page | person-82def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 104 | home page | person-83ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 105 | home page | person-84abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 106 | home page | person-85def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 107 | confirmation page | person-85def654 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 108 | home page | person-86ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 109 | home page | person-87abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 110 | home page | person-88ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 111 | home page | person-89abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 112 | confirmation page | person-89abc789 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 113 | home page | person-90def789 | def789 |  |  |
| 2024-07-18T19:15:39+00:00 | 114 | home page | person-91ghi789 | ghi789 |  |  |
| 2024-07-18T19:15:39+00:00 | 115 | home page | person-92abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 116 | confirmation page | person-92abc987 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 117 | home page | person-93def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 118 | home page | person-94ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 119 | home page | person-95abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 120 | home page | person-96def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 121 | confirmation page | person-96def654 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 122 | home page | person-97ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 123 | home page | person-98abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 124 | home page | person-99def321 | def321 |  |  |
| 2024-07-18T19:15:39+00:00 | 125 | home page | person-100ghi321 | ghi321 |  |  |
| 2024-07-18T19:15:39+00:00 | 126 | home page | person-101abc123 | abc123 |  |  |
| 2024-07-18T19:15:39+00:00 | 127 | home page | person-102def123 | def123 |  |  |
| 2024-07-18T19:15:39+00:00 | 128 | confirmation page | person-102def123 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 129 | home page | person-103ghi123 | ghi123 |  |  |
| 2024-07-18T19:15:39+00:00 | 130 | home page | person-104abc456 | abc456 |  |  |
| 2024-07-18T19:15:39+00:00 | 131 | home page | person-105def456 | def456 |  |  |
| 2024-07-18T19:15:39+00:00 | 132 | home page | person-106ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 133 | home page | person-107abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 134 | home page | person-108abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 135 | confirmation page | person-108abc987 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 136 | home page | person-109def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 137 | home page | person-110ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 138 | confirmation page | person-110ghi987 |  |  |  |
| 2024-07-18T19:15:39+00:00 | 139 | home page | person-111def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 140 | home page | person-112def987 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 141 | confirmation page | person-112def987 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 142 | home page | person-113ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 143 | home page | person-114abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 144 | home page | person-115def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 145 | confirmation page | person-115def654 |  | 1 | 159.25 |
| 2024-07-18T19:15:39+00:00 | 146 | home page | person-116ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 147 | home page | person-117abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 148 | home page | person-118def321 | def321 |  |  |
| 2024-07-18T19:15:39+00:00 | 149 | confirmation page | person-118def321 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 150 | home page | person-119ghi321 | ghi321 |  |  |
| 2024-07-18T19:15:39+00:00 | 151 | home page | person-120abc123 | abc123 |  |  |
| 2024-07-18T19:15:39+00:00 | 152 | home page | person-121def123 | def123 |  |  |
| 2024-07-18T19:15:39+00:00 | 153 | home page | person-122ghi123 | ghi123 |  |  |
| 2024-07-18T19:15:39+00:00 | 154 | home page | person-123abc456 | abc456 |  |  |
| 2024-07-18T19:15:39+00:00 | 155 | home page | person-124def456 | def456 |  |  |
| 2024-07-18T19:15:39+00:00 | 156 | confirmation page | person-124def456 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 157 | home page | person-125ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 158 | home page | person-126abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 159 | home page | person-127abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 160 | home page | person-128def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 161 | home page | person-129ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 162 | home page | person-130abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 163 | confirmation page | person-130abc654 |  | 1 | 149.25 |
| 2024-07-18T19:15:39+00:00 | 164 | home page | person-131def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 165 | home page | person-132ghi654 | ghi654 |  |  |
| 2024-07-18T19:15:39+00:00 | 166 | home page | person-133abc321 | abc321 |  |  |
| 2024-07-18T19:15:39+00:00 | 167 | home page | person-134ghi456 | ghi456 |  |  |
| 2024-07-18T19:15:39+00:00 | 168 | confirmation page | person-134ghi456 |  | 1 | 139.25 |
| 2024-07-18T19:15:39+00:00 | 169 | home page | person-135abc789 | abc789 |  |  |
| 2024-07-18T19:15:39+00:00 | 170 | home page | person-136def789 | def789 |  |  |
| 2024-07-18T19:15:39+00:00 | 171 | home page | person-137ghi789 | ghi789 |  |  |
| 2024-07-18T19:15:39+00:00 | 172 | home page | person-138abc987 | abc987 |  |  |
| 2024-07-18T19:15:39+00:00 | 173 | confirmation page | person-138abc987 |  | 1 | 124.25 |
| 2024-07-18T19:15:39+00:00 | 174 | home page | person-139def987 | def987 |  |  |
| 2024-07-18T19:15:39+00:00 | 175 | home page | person-140ghi987 | ghi987 |  |  |
| 2024-07-18T19:15:39+00:00 | 176 | home page | person-141abc654 | abc654 |  |  |
| 2024-07-18T19:15:39+00:00 | 177 | home page | person-142def654 | def654 |  |  |
| 2024-07-18T19:15:39+00:00 | 178 | confirmation page | person-142def654 |  | 1 | 174.25 |
| 2024-07-18T19:15:39+00:00 | 179 | home page | person-143ghi654 | ghi654 |  |  |

[Download sample event data](assets/event-data)

Lookup data
Lookup data is available in the Example Lookup Data Dataset. The sample data looks like:

| table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 5-row-4 6-row-4 7-row-4 8-row-4 9-row-4 10-row-4 11-row-4 12-row-4 13-row-4 14-row-4 15-row-4 16-row-4 17-row-4 18-row-4 |  |  |  |
| --- | --- | --- | --- |
| _id | tracking_code | ad_group | campaign_name |
| 1 | abc123 | abc-adgroup | 123 Campaign |
| 2 | def123 | def-adgroup | 123 Campaign |
| 3 | ghi123 | ghi-adgroup | 123 Campaign |
| 4 | abc456 | abc-adgroup | 456 Campaign |
| 5 | def456 | def-adgroup | 456 Campaign |
| 6 | ghi456 | ghi-adgroup | 456 Campaign |
| 7 | abc789 | abc-adgroup | 789 Campaign |
| 8 | def789 | def-adgroup | 789 Campaign |
| 9 | ghi789 | ghi-adgroup | 789 Campaign |
| 10 | abc987 | abc-adgroup | 987 Campaign |
| 11 | def987 | def-adgroup | 987 Campaign |
| 12 | ghi987 | ghi-adgroup | 987 Campaign |
| 13 | abc654 | abc-adgroup | 654 Campaign |
| 14 | def654 | def-adgroup | 654 Campaign |
| 15 | ghi654 | ghi-adgroup | 654 Campaign |
| 16 | abc321 | abc-adgroup | 321 Campaign |
| 17 | def321 | def-adgroup | 321 Campaign |
| 18 | ghi321 | ghi-adgroup | 321 Campaign |

[Download sample lookup data](assets/lookup-data)

INFO
Further details for setting up schemas and datasets for the event and lookup data are not provided. This setup is assumed common knowledge and follows the same steps as for the lookup data.
### Summary schema

Summary data needs a summary schema in Experience Platform. A summary schema is a schema that is using the XDM Summary Metrics as its base class.

To create a summary schema in Experience Platform:

- Select **Experience Platform** from the app switcher.
- Select **Schemas** from the left rail.
- Select **Create schema**.
- Select **Manual** in the **Create a schema** dialog. Then use **Select** to continue.
- In the **Select a class** step of the **Schemas** > **Create schema** wizard, select **Other** from the **Select a base class for this schema** options.
- From the list, select **XDM Summary Metrics** (or use field to search for) and select **Next**.
- In the **Name and review** step of the **Schemas** > **Create schema** wizard, enter a **Schema display name**, for example Example Summary Data Schema and an optional description. Select **Finish** to finish this step.

The structure of your base summary schema is displayed, ready to be augmented with the fields for your summary data. You add fields to a schema, using field groups.

To add a field group, containing the fields for your sample data:

- Select Add in Field groups .
- In the Add field groups dialog, select Create new field group .
- Enter a Display name for the field group, for example Example Summary Data . Optionally provide a description.
- Select Add field groups .
- You are back in the schema structure user interface. Select the new Example Summary Data in Field groups .
- Select the next to the schema name Example summary Data Schema . A Field properties panel opens up allowing you to add details for a field. Enter a Field name : campaign_id Enter a Display name : campaign_id Select a Type from the Select data type drop-down menu: String Ensure Assign to Field group is selected, and select Example Summary Data from the drop-down menu. Scroll down to the bottom, and select Apply .
- Repeat the previous step for the other fields of the summary data. See the table below for the correct values. table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 5-row-4 Field name Display name Type Field Group ad_group ad_group String Example Summary Data campaign_name campaign_name String Example Summary Data cost cost Double Example Summary Data impression impression Integer Example Summary Data network network String Example Summary Data
- To save your Example Summary Data field group as part of your schema, select Save . You see a confirmation when your schema is successfully saved.

You have now defined a schema, detailing the model for your summary data. Similar to the one below.

### Summary dataset

To store your summary data in Experience Platform, you first need to create a dataset, and then upload your summary data into the dataset.

To create a dataset:

- Select Experience Platform from the app switcher.
- Select Datasets from the left rail.
- Select Create dataset .
- In the Datasets > Create datasets screen, select Create dataset from schema .
- In the Select schema step of the Workflows > Create dataset from schema wizard, search for and select your Example Summary Data Schema .
- Select Next .
- In the Configure dataset step of the Workflows > Create dataset from schema wizard: Enter a Name for the dataset, for example: Example Summary Data Dataset . Optionally provide a description. Select Finish .

You see a screen displaying the details of your new dataset.

To upload your sample data into this dataset:

- Select Experience Platform from the app switcher.
- Select Workflows from the left rail. Select Map CSV to XDM schema from the Data ingestion options in the Workflows screen. Select Launch from the Map CSV to XDM schema panel.
- In the Dataflow detail step of the Workflows > Map CSV to XDM schema wizard: Select Existing dataset for Target dataset . Select Example Summary Data Dataset from the drop-down menu. Select Next .
- In the Select data step of the Workflows > Map CSV to XDM schema wizard: Drag and drop your file with summary data in CSV format onto Drag and drop files . Alternatively, use Choose files to select your file. Ensure the Data format and Delimiter do have the correct values for your sample data. For example, Delimited as the Data format , and , as the Delimiter . A sample (10 records) of your summary data is shown in Sample data . Select Next .
- In the Mapping step of the Workflows > Map CSV to XDM schema wizard: Check whether all data fields of your Source Data are correctly mapped to the corresponding Target fields in your schema. For the sample data, no errors are reported as you explicitly named the fields in your schema similar to the field names in your sample data. Otherwise, you can use this screen to correct the mapping. You can optionally select Validate to (once more) validate the data. You can optionally select Preview data to open a dialog with a preview of the data once loaded into the dataset. Select Finish .

In **Sources** > **Dataflow - XX/XX/XXXX, XX:XX XX**, the status of your upload appears. Refresh to see updates of the upload. When successful, your sample data is loaded into Experience Platform.

## Connection

To use your sample data in Customer Journey Analytics, you create a connection that includes the Example Summary Data Dataset from Experience Platform.

- Select Customer Journey Analytics from the app switcher.
- Select Connections , optionally from Data management , in the top menu.
- Select Create new connection .
- In Connections > Untitled connection : Enter a Connection name , for example Example Connection Using Summary Data . Select the sandbox that contains the dataset you created and the other datasets you want to include from the Sandbox drop-down menu. Select less than 1 million from the Average number of daily events drop-down menu. Select Add datasets . In the Select datasets step of the Add datasets wizard: Search and select Example Summary Data Dataset , Example Event Data Dataset , and Example Lookup Data Dataset . Select Next . In the Datasets settings step of the Add datasets wizard: For the Example Event Data Dataset : Confirm the selections for Person ID ( person_id ) and Timestamp are correct. Select Web Data from the Data source type . Enable Import all new data . Enable Backfill all existing data . For the Example Lookup Data Dataset : Select tracking_code as the Key and tracking_code (Event datasets) as the Matching Key. Select Web Data from the Data source type . Enable Import all new data . Enable Backfill all existing data . For the Example Summary Data Dataset : Confirm the selections for Timestamp and Timezone are correct. Enable Import all new data . Enable Backfill all existing data . Select Add datasets .
- In the Connections > Example Connection using Summary Data connection screen, select Save to save the connection.

The data from the datasets is added to Customer Journey Analytics, which can take a couple of hours. So please, be patient before continuing.

After a while, verify that data from your datasets is properly loaded in Customer Journey Analytics.

- Select Customer Journey Analytics from the app switcher.
- Select Connections , optionally from Data management , in the top menu.
- Select your connection, for example Example Connection Using Summary Data .
- Select an appropriate date range in the Connection > Example Connection Using Summary data details. Select and then select Last 7 days . Select Apply .

In the list of **Datasets**, the values in the **Records added** column should confirm that data from your datasets is now part of Customer Journey Analytics.

## Data view

To ensure you can report on the correct data in Workspace, you want to create a data view containing the relevant metrics and dimensions.

- Select Customer Journey Analytics from the app switcher.
- Select Data views , optionally from Data management , in the top menu.
- Select Create new data view .
- In Data views , go through the wizard screens to configure your data view. In the Configure step of Data views : Select your connection from Settings | Connection . For example, Example Connection Using Summary Data . Enter a Name for your data view, for example Example Data View Using Summary Data . Leave all other settings. Select Save and continue . In the Components step of Data views > Example Data View Using Summary Data : Add the following components to the Dimensions and Metrics list. Note that for clarity, the component names are modified from their default name, using Component name in Component settings in the component panel (at the right). Metrics table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 Component name Dataset Schema data type Schema path Cost Example Summary Data Dataset Double _tenant .cost Impressions Example Summary Data Dataset Integer _tenant .impression Orders Example Event Data Dataset Integer _tenant .orders Revenue Example Event Data Dataset Double _tenant .revenue_amount Dimensions table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 5-row-4 6-row-4 7-row-4 8-row-4 9-row-4 10-row-4 Component name Dataset Schema data type Schema path Ad Group (Lookup) Example Lookup Data Dataset String _tenant .ad_group Ad Group Example Summary Data Dataset String _tenant .ad_group Campaign Id Example Summary Data Dataset String _tenant .campaign_id Campaign Name (Lookup) Example Lookup Data Dataset String _tenant .campaign_name Campaign Name Example Summary Data Dataset String _tenant .campaign_name Network Example Summary Data Dataset String _tenant .network Page Name Example Event Data Dataset String _tenant .page_name Person Id Example Event Data Dataset String _tenant .person_id Tracking Code (Event) Example Event Data Dataset String _tenant .tracking_code Tracking Code (Lookup) Example Lookup Data Dataset String _tenant .tracking_code Select the Tracking Code (Event) dimension in the Dimensions list. In the component panel: Unfold Summary Data Group . Enable Create grouping . Select Campaign Id from the Dimension drop-down menu. This step ensures that event data and summary data is properly combined for reporting. You can optionally enable Hide in reporting . Hide in reporting ensures the selected dimension (Campaign Id) is hidden in Analysis Workspace and other Customer Journey Analytics reporting tools. If you have enabled this option, you can verify the option: Select the Campaign Id dimension in the Dimensions list. You notice that Hide component in reporting in Component settings is now automatically enabled. Create a new derived field, for example Campaign Name (Lookup Derived Field) , to ensure you can report in Workspace using the Campaign Name (Lookup) dimension from the Example Lookup Data dataset. Select campaign_id for Value . Select Example Lookup Data Dataset from the Lookup dataset drop-down menu. Select tracking_code from the Matching Key drop-down menu. Select campaign_name from the Values to return drop-down menu. Select Save . Add the newly created derived field, Campaign Name (Lookup Derived Field) , to the Dimensions component list. Select the Campaign Name (Lookup) dimension in the Dimensions list. In the component panel: Unfold Summary Data Group . Enable Create grouping . Select Campaign Name (Lookup Derived Field) from the Dimension drop-down menu. This step ensures that the Campaign Name (Lookup) from the Example Lookup Data Dataset can be safely used in reporting (see Workspace ). Select the Revenue metric from the Metrics list. In the component panel: Unfold Attribution . Select Last Touch from the Attribution Model drop-down menu. Select 30 Day from the Lookback window drop-down menu. Unfold Format . Select Currency from the Format drop-down menu. Select 2 from the Decimal places drop-down menu. Select the Orders metric from the Metrics list. In the component panel: Unfold Attribution . Select Last Touch from the Attribution Model drop-down menu. Select 30 Day from the Lookback window drop-down menu. Unfold Format . Select Decimal from the Format drop-down menu. Select ▲ Good (green) from the Show upward trend as drop-down menu. Select Save and continue . In the Settings step of Data views : Leave all settings at their defaults. Select Save and finish.

You have now set up your data view for proper reporting on summary data.

## Workspace

To report on your summary data, create a new Project in Analysis Workspace.

- Select **Customer Journey Analytics** from the app switcher.
- Select **Workspace** from the top menu.
- Select **Create project**.
- Select **Blank Workspace project** from the dialog with options to create a blank Workspace project.
- Select **Create**.

You see an empty canvas with a Freeform panel, consisting of an empty Freeform table.

- Ensure that the data view, selected for the panel, is referring to the data view containing the configuration for the summary data. For example, **Example Data View Using Summary Data.**
- Ensure that the date range is valid for the data you want to report on. For example: **Last 2 full months**.
- Drag **Tracking Code (Event)** from **Dimensions** and drop the dimension onto the empty Freeform table.
- Drag **Orders** from **Metrics**, and drop the metric onto the **Events** column to replace that column in the Freeform table.
- Drag **Revenue** from **Metrics**, and drop the metric to add as an additional column to the Freeform table.
- Drag **Impressions** from **Metrics**, and drop the metric to add as an additional column to the Freeform table.
- Drag **Cost** from **Metrics**, and drop the metric to add as an additional column to the Freeform table.
- To save your project, select **Project** > **Save**, and provide a name for your project. For example, Example Project Using Summary Data.

You want to use the power of reporting on summary data and report on cost per impression and return on ad spend (ROAS). To report on these metrics, you have to create two calculated metrics.

- Select Components > Calculated metrics .
- Select Add to add a new calculated metric. Specify Cost per Impression for the Name . Select Currency for Format . Specify 4 for Decimal places . Use Cost ÷ Impressions as Definition . Select Save .
- Select Add to add another new calculated metric. Specify Return on Ad Spend for the Name . Select Currency for Format . Select 2 for Decimal places . Use Revenue (Last Touch | 30 Days) − Cost as Definition . Select Save .

Add your calculated metrics to your report.

- Drag Cost per Impression from Metrics and drop the metric to add as an additional column to the Freeform table. Select Column settings. Disable Percent .
- Drag Return on Ad Spend from Metrics and drop the metric to add as an additional column to the Freeform table. Select Column settings. Disable Percent . Enable Conditional formatting . Select Auto-generated . Select a preferred Conditional formatting palette . Select Save to save your project.

If you want to report on Campaign Name rather than Tracking Code (Event), take the following steps:

- Duplicate the **Summary Data Report** Freeform table visualization.
- Rename the duplicated visualization to Summary Data Report (using Campaign Name).
- Replace the **Tracking Code (Event)** dimension with the **Campaign Name (Lookup)** dimension.

You can report correctly on Campaign Name (Lookup) because of the derived field you created, and the summary data group component configuration for Campaign Name (Lookup). See [Data view](#data-view).

Your final project should look like the one shown below.

Related Articles
Summary data
Summary data group component settings
recommendation-more-help
