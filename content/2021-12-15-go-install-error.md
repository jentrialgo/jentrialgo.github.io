Title: Error cannot use path@version syntax in GOPATH mode
Date: 2021-12-15 12:00
Category: go
Tags: go

I was trying to install xk6 using this command:

```bash
go install go.k6.io/xk6/cmd/xk6@latest
```

And I got this error:

```text
package go.k6.io/xk6/cmd/xk6@latest: cannot use path@version syntax in GOPATH mode
```

Although I found [a question in Stack
Overflow](https://stackoverflow.com/q/54415733) with that error, the given
solutions didn't work for me. In the end, I learned that the message was caused
because I was using an old version of Go: the `path@version` was added in Go
1.16 and I was using 1.15. Thus, the solution for my problem was updating Go.
