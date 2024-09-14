**SQL injection with filter bypass via XML encoding**
*-Goals:* Exploit SQL injection to retrieve the admin user's credentials from the users table and log in.
*-Hint:*
>A web application firewall (WAF) will block requests that contain obvious signs of a SQL injection attack. You'll need to find a way to obfuscate your malicious query to bypass this filter. We recommend using the Hackvertor extension to do this. 
*-Analysis:*

`1 UNION SELECT username || '~' ||password from users`

*`LAB SOLVED`*
![alt text](image.png)