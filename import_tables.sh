#!/bin/bash
#
cd Tables
rm ../import_test.db
    sqlite3 ../import_test.db << EOF
create table if not exists  fed_data(
Date TEXT,
Interest TEXT,
Vacancy TEXT,
Inflation TEXT
);

create table if not exists price_data(
Date TEXT,
Interest TEXT,
Vacancy TEXT,
Inflation TEXT,
Price TEXT,
Value TEXT,
Adjusted_Price TEXT,
Adjusted_Value TEXT,
Next_Quarted TEXT
);
EOF
for FILE in *.csv; do 
    echo "Importing $FILE"
    sqlite3 ../import_test.db << EOF
.mode csv
.import --skip 1 $FILE ${FILE%.csv} 
EOF
done

