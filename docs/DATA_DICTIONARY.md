# Data Dictionary

## `data/sample/branch_master.csv`

| Column | Type | Description |
|---|---|---|
| Branch | Text | Synthetic branch identifier (`B001`, etc.) |
| Branch Name | Text | Synthetic display name |
| City | Text | Synthetic geographic grouping |
| Category | Text | Synthetic branch format/category |
| Size SQM | Number | Synthetic branch size |
| Opening Date | Date | Lifecycle start date |
| Closing Date | Date / blank | Lifecycle end date when applicable |

## `data/sample/sales_daily.csv`

| Column | Type | Description |
|---|---|---|
| Date | Date | Sales date |
| Branch | Text | Branch key |
| Core Retail Sales | Decimal | Primary retail sales component |
| Service Channel Sales | Decimal | Secondary service sales component |
| Priority Sales | Decimal | Strategic subset of core retail |
| Customer Count | Integer | Daily customer/transaction count |

## `data/sample/monthly_budget.csv`

| Column | Type | Description |
|---|---|---|
| Month | YYYY-MM | Target month |
| Branch | Text | Branch key |
| Total Budget | Decimal | Monthly total target |
| Core Retail Budget | Decimal | Monthly target for core retail |
| Service Channel Budget | Decimal | Monthly target for service channel |

## `data/sample/delivery_channel.csv`

| Column | Type | Description |
|---|---|---|
| Date | Date | Channel sales date |
| Branch | Text | Branch key |
| Delivery Channel Sales | Decimal | Sales attributable to the delivery sub-channel; already included within Core Retail Sales |
