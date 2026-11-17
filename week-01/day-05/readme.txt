REST APIs and HTTP Fundamentals
Welcome to Day 5 of your AI Engineer roadmap! 🚀

Today we're starting an important skill for AI Engineering: REST APIs.

Why does this matter? When you build an AI application, it often needs to communicate with other applications, databases, AI models, and external services. APIs make that communication possible.

What is an API?
API stands for Application Programming Interface.

HTTP method	    Purpose	            Example
GET	            Retrieve data	    Get all employees
POST	        Create data	        Add an employee
PUT	            Replace data	    Replace employee details
PATCH	        Partially update	Update employee salary
DELETE	        Remove data	        Delete an employee



4. Important HTTP status codes
Servers use status codes to tell clients what happened.
Status	Meaning
200	OK — request successful
201	Created — resource created
204	No Content — successful, no response body
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
422	Unprocessable Content
500	Internal Server Error

For example, if an employee with ID 100 does not exist, the API might return 404 Not Found.