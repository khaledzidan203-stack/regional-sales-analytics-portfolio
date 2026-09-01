# Data Dictionary

## Branch Master input

| Column | Type | Description |
|---|---|---|
| Branch | Text | Runtime branch identifier |
| Branch Name | Text | Runtime display name |
| City | Text | Runtime geographic grouping |
| Category | Text | Runtime branch format/category |
| Size SQM | Number | Runtime branch size |
| Opening Date | Date | Lifecycle start date |
| Closing Date | Date / blank | Lifecycle end date when applicable |

## Sales Collection CSV

| Column | Type | Description |
|---|---|---|
| Date | Date | Sales date |
| Branch | Text | Branch key |
| Core Retail Sales | Decimal | Primary retail sales component |
| Service Channel Sales | Decimal | Secondary service sales component |
| Priority Sales | Decimal | Strategic subset of core retail |
| Customer Count | Integer | Daily customer/transaction count |

## Sales Budget Breakdown XLSX

| Column | Type | Description |
|---|---|---|
| Month | YYYY-MM | Target month |
| Branch | Text | Branch key |
| Total Budget | Decimal | Monthly total target |
| Core Retail Budget | Decimal | Monthly target for core retail |
| Service Channel Budget | Decimal | Monthly target for service channel |

## Optional Delivery Channel XLSX

| Column | Type | Description |
|---|---|---|
| Date | Date | Channel sales date |
| Branch | Text | Branch key |
| Delivery Channel Sales | Decimal | Sales attributable to the delivery sub-channel; already included within Core Retail Sales |

These schemas document runtime expectations only. The repository contains no populated business input files.
