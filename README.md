# chaos-dbt-jobs
a spot to hold dbt jobs


├── dbt_project.yml
├── models
│   ├── analytics
│   │   ├── users.sql
│   │   └── pageviews.sql
│   ├── insights
│   │   ├── most_active_users.sql
│   │   ├── pageviews_by_country.sql
│   │   └── daily_conversions.sql
│   └── raw
│       ├── customers.sql
│       ├── orders.sql
│       └── products.sql
├── macros
│   ├── custom_time_dimension.sql
│   └── custom_date_range.sql
├── tests
│   ├── analytics
│   │   ├── test_users.sql
│   │   └── test_pageviews.sql
│   ├── insights
│   │   ├── test_most_active_users.sql
│   │   ├── test_pageviews_by_country.sql
│   │   └── test_daily_conversions.sql
│   └── raw
│       ├── test_customers.sql
│       ├── test_orders.sql
│       └── test_products.sql
├── seed
│   ├── customers.csv
│   ├── orders.csv
│   └── products.csv
└── target
    ├── dev.yml
    ├── prod.yml
    └── staging.yml
