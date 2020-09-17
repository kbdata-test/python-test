FROM golang:1.8-alpine
ADD . /go/src/python-test
RUN go install python-test
FROM alpine:latest
COPY --from=0 /go/bin/python-test .
ENV PORT 8080
CMD ["./python-test"] 