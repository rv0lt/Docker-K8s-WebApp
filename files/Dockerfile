FROM python:3.9-slim-buster as builder

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

FROM scratch

COPY . .

ENV FLASK_APP=back.py

#---------- flask and redis modules external dependencies ----

COPY --from=builder /lib/x86_64-linux-gnu/libnss_dns.so.2 /lib/x86_64-linux-gnu/libnss_dns.so.2
COPY --from=builder /lib/x86_64-linux-gnu/libresolv.so.2 /lib/x86_64-linux-gnu/libresolv.so.2

COPY --from=builder /lib/x86_64-linux-gnu/libz.so.1 /lib/x86_64-linux-gnu/libz.so.1

#---------- python external dependencies ----
COPY --from=builder /lib/x86_64-linux-gnu/libcrypt.so.1 /lib/x86_64-linux-gnu/libcrypt.so.1
COPY --from=builder /lib/x86_64-linux-gnu/libdl.so.2 /lib/x86_64-linux-gnu/libdl.so.2 
COPY --from=builder /usr/local/lib/libpython3.9.so.1.0 /usr/local/lib/libpython3.9.so.1.0 
COPY --from=builder /etc/ld.so.cache /etc/ld.so.cache
COPY --from=builder /lib/x86_64-linux-gnu/libpthread.so.0 /lib/x86_64-linux-gnu/libpthread.so.0
COPY --from=builder /lib/x86_64-linux-gnu/libutil.so.1 /lib/x86_64-linux-gnu/libutil.so.1
COPY --from=builder /lib/x86_64-linux-gnu/libm.so.6 /lib/x86_64-linux-gnu/libm.so.6 
COPY --from=builder /lib/x86_64-linux-gnu/libc.so.6 /lib/x86_64-linux-gnu/libc.so.6
COPY --from=builder /lib64/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2

#---------- python files ----

COPY --from=builder /usr/local/bin/python /usr/local/bin/python
COPY --from=builder /usr/local/bin/flask /usr/local/bin/flask
COPY --from=builder /usr/local/lib/python3.9/ /usr/local/lib/python3.9/


EXPOSE 5000

CMD ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]