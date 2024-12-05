# Code documentation tags

https://goswagger.io/go-swagger/generate-spec/spec/

## swagger:meta

```Go
// Package classification of Product API.
//
// Documenting for Product API
//
//	Schemes: http, https
//	BasePath: /
//	Version: 0.0.1
//
//	Consumes:
//	- application/json
//
//	Produces:
//	- application/json
//
// swagger:meta
```

## swagger:response

```Go
// A list of products returns in the response
// swagger:response productsResponseWrapper
type productsResponseWrapper struct {
	// All products in the system
	// in: body
	Body []data.Product
}
```