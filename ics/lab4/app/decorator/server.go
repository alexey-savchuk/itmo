package main

import (
	"net/http"
)

type HttpHandler = func(w http.ResponseWriter, r *http.Request)

func CheckCookie(handler HttpHandler) HttpHandler {
	return func(w http.ResponseWriter, r *http.Request) {
		cookie, err := r.Cookie("bus-ticket-sales")
		if cookie == nil || err != nil {
			w.Write([]byte("Sorry... You must sing in"))
			w.WriteHeader(http.StatusForbidden)
			return
		}
		handler(w, r)
	}
}

func BuyTicket(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Yeah. You can buy a ticket"))
}

func main() {
	handler := BuyTicket
	handler = CheckCookie(handler)

	http.HandleFunc("/ticket", handler)
}
