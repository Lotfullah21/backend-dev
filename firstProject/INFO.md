## URL

every single resource on web is located by an address, known as `uniform resource locator`.
url is an address where files are stored.

query parameters and path parameters are two ways to pass data to a web server, but they serve different purposes and are structured differently. Here's a breakdown of their differences:

## Path parameter

Path parameters are part of the URL path itself, it is used to capture any part of a url, `google.com/2022/`: here, 2022 is a parameter.

`Example: https://example.com/users/123` (where 123 is the path parameter representing a specific user ID)

## Query String

A query string is a sequence of one or more key=value pairs concatenated by the & symbol. Each key is the query parameter. The query string ends with the ? symbol after the URL endpoint.
It is the entire part of the URL that comes after the ?.

The URL dispatcher doesn’t parse these parameters. They are fetched by the view from the request object it receives. The request object’s GET property is a dictionary object.

The key-value pairs in the query string are added to the request.GET property. Hence, the name can be obtained with `request.GET[‘name’]` expression.

`google.com/?year=2022`: here, year is a query string.

we can more than one query string by adding `&` in between.

`google.com/?year=2022&month="Oct"`

## Query parameters

Query parameters refer to the individual key-value pairs in the query string.

```py
https://example.com/search?query=apple&sort=price
```

`query=apple` is a query parameter.

query parameters for optional filters or settings and path parameters for identifying specific resources

| Feature             | **Query String**                                                          | **Query Parameters**                                                           | **Path Parameters**                                                         |
| ------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **Definition**      | The entire section after the `?` in a URL, consisting of key-value pairs. | Individual key-value pairs that make up the query string.                      | Values embedded directly in the URL path that represent specific resources. |
| **Purpose**         | To pass optional data or filters to the server.                           | To define individual pieces of optional data, like filters or search criteria. | To identify specific resources or entities (e.g., user IDs, product IDs).   |
| **Location in URL** | After the `?` symbol. Example: `?key=value&sort=asc`                      | Each `key=value` pair after the `?` and separated by `&`.                      | Inside the URL path itself. Example: `/users/123`                           |
| **Syntax**          | Starts with `?` followed by `key=value` pairs separated by `&`.           | `key=value` pairs. Each parameter is separated by `&`.                         | Typically part of the path structure with no special symbols.               |
| **Use Cases**       | Used for filtering, sorting, pagination, or search terms.                 | Filters, sorting options, pagination values (e.g., `page=2`), etc.             | Used for resource identification like `/users/{id}` or `/products/{id}`.    |
| **Example**         | `?category=fruits&sort=price`                                             | `category=fruits`, `sort=price`                                                | `/products/456`, `/users/123`                                               |

## Client error responses

`400`: It represents a bad request, some of the params might not match what the server expects.
`401`: For authentication, the use must logged in to be able make a request.
`403`: Request is successful, but the user does not have required permission.
`404`: The resource cannot be located at the specified path.

## Server error responses

It shows that a failure occurred on the web sever when trying to process the request.
For instance, application failure, long time to respond.

`500`: Server failed to process the request.

Django handles all error cases by raising an exception which is invoked via an error handler view.
We can configure it as well.
A project level `views.py` must be created handling all the errors across the project.
