# Product Query Engine

## Endpoint

GET /api/products

Returns a list of products with support for search, filtering, sorting,
pagination, and soft deletes.


## Query Parameters

### Search

?minPrice=500&maxPrice=1000
Filter products within a price range.


### Sorting
?sortBy=price&order=asc
Sort products by price in ascending order. Use `desc` for descending.


### Limit
?limit=20
Limit number of products returned (default: 10).



### Soft Deleted Products
?includeDeleted=true
Include soft-deleted products in the results.

### Example Request
GET /api/products?search=phone&minPrice=300&sort=price:asc&limit=5


## Error Response Format
```json
{
  "success": false,
  "message": "Product not found",
  "code": "PRODUCT_NOT_FOUND"
}

