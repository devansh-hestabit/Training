# **API Investigation Report**

**Day 4 — HTTP / API Forensics**

## **1\. Understanding the HTTP Request–Response Cycle**

An HTTP request is sent by the client (curl or Postman) to a server.  
The server processes the request and sends back an HTTP response.

Each request contains:

* Method (GET)  
* URL  
* Headers

Each response contains:

* Status code  
* Headers  
* Body (optional)

Using `curl -v`, the complete request and response cycle was observed,  
including headers and status codes.

## **2\. Headers Analysis**

Headers are key-value pairs used to exchange metadata between client and server.

### **Common headers observed:**

* **Content-Type**: Defines response format (application/json)  
* **User-Agent**: Identifies the client making the request  
* **Authorization**: Used for authentication (ignored in this API)  
* **ETag**: Unique identifier for a specific version of the resource  
* **Cache-Control**: Defines caching rules  
* **Access-Control-Allow-Origin**: Enables cross-origin access

Removing the `User-Agent` header did not affect the response.  
Sending a fake `Authorization` header was ignored, showing that the endpoint is public.

## **3\. Pagination Behavior**

Pagination was tested using query parameters:

* `limit`: number of items to return  
* `skip`: number of items to skip

Example:

/products?limit=5\&skip=10

The response returned only 5 products starting after skipping the first 10\.  
This shows that pagination is controlled by the client using query parameters.

**4\. ETag and HTTP Caching**

The server returned an **ETag** header with the response.

Example:

ETag: W/"ac3a-uk0FDUI0X0lS5liyUbIxqA7L7F4"

This ETag was reused in a conditional request using the `If-None-Match` header.

When the same ETag was sent back to the server, the response was:

HTTP/2 304 Not Modified

This means the resource had not changed and the cached version could be reused.  
No response body was returned, saving bandwidth.

## **5\. CDN and Cache Observations**

The response contained:

cf-cache-status: HIT

This indicates that the response was served from Cloudflare’s cache instead of the origin server.  
The `age` header showed that the response had been cached for several days.

This demonstrates the difference between browser caching and CDN caching.

**6\. Local Node.js Server Testing**

A local HTTP server was created using Node.js with the following endpoints:

* `/echo` → returns request headers  
* `/slow?ms=3000` → delays response  
* `/cache` → sends cache-related headers

These endpoints helped in understanding:

* How servers read headers  
* How response delay works  
* How cache headers are set

