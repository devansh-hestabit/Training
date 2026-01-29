# Security Testing

All tests were performed against the running API using curl and verified
with screenshots.

Base URL used for testing:
#### http://localhost:4000/api

##  1. Normal Request (Baseline Test)

### Purpose
To verify that the API works correctly under normal conditions before
performing any security attacks.

### Result
- Products fetched successfully
- API responded with status `200`

### Screenshot
![Normal Request](./screenshots/Security%20Test/Normal%20Request.png)


##  2. Rate Limiting

### Purpose
To prevent abuse by limiting the number of requests from a single IP.

### Test
Multiple rapid requests were sent to the same endpoint.

### Result
- After exceeding the limit, API returned `429 Too Many Requests`

### Screenshot
![Rate Limiting](./screenshots/Security%20Test/Rate%20Limiting.png)



##  3. Payload Size Limit

### Purpose
To prevent large payload / memory exhaustion attacks.

### Test
A request with payload larger than 10kb was sent.

### Result
- Request was rejected
- Payload size limit enforced successfully

### Screenshot
![Payload Limit](./screenshots/Security%20Test/Payload%20Limit.png)



##  4. NoSQL Injection (Query Parameters)

### Purpose
To ensure MongoDB operators cannot be injected through query parameters.

### Test
A query containing MongoDB operators was sent.

### Result
- API did not crash
- Query was safely handled

### Screenshot
![NoSQL Injection Query](./screenshots/Security%20Test/NoSQL%20Injection(Query).png)




##  5. NoSQL Injection (Request Body)
### Purpose
To prevent malicious MongoDB operators in request body.

### Test
MongoDB operators were sent in request body.

### Result
- Request was rejected or safely handled
- No database manipulation occurred

### Screenshot
![NoSQL Injection Body](./screenshots/Security%20Test/NoSQL%20(Request%20Body).png)




##  6. XSS (Cross-Site Scripting)

### Purpose
To test how the backend handles script injection attempts.

### Test
Script tags were sent as input data.

### Result
- Script stored as plain text
- No execution occurred on backend
- API remained stable

> Note: XSS prevention is handled at the frontend by escaping output.
The backend ensures data integrity and stability.

### Screenshot
![XSS](./screenshots/Security%20Test/XSS.png)


##  7. Parameter Pollution

### Purpose
To ensure duplicate query parameters do not break application logic.

### Test
Multiple values were provided for the same query parameter.

### Result
- API responded normally
- No unexpected behavior observed

### Screenshot
![Parameter Pollution](./screenshots/Security%20Test/Parameter%20Pollution.png)




##  8. Security Headers (Helmet)

### Purpose
To verify that HTTP security headers are enabled.

### Test
Response headers were inspected using curl.

### Result
- Security headers like `X-Content-Type-Options`, `X-Frame-Options` present

### Screenshot
![Helmet Headers](./screenshots/Security%20Test/Helmet.png)




## 9. CORS (Cross-Origin Resource Sharing)

### Purpose
To verify CORS configuration.

### Test
Request was sent with a custom `Origin` header.

### Result
- Request was allowed (CORS set to `*` for development)
- Behavior is expected

### Screenshot
![CORS](./screenshots/Security%20Test/cors.png)
