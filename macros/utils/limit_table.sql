{% macro limit_table() -%}
    {%- set production_targets = ('prod','docs','ci') -%}
    {%- if target.name in production_targets -%}
    {%- else -%}
    LIMIT 100
    {%- endif -%}
{%- endmacro %}