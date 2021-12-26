FROM debian:bullseye
RUN apt update && apt install -y curl gpg && curl https://packages.ipfire.org/79842AA7CDBA7AE3-pub.asc | apt-key add -
RUN echo "deb     https://packages.ipfire.org/location bullseye/\ndeb-src https://packages.ipfire.org/location bullseye/" >> /etc/apt/sources.list.d/location.list
RUN apt update && apt install -y location && location update
ADD httpd.py /
ADD entrypoint.sh /
CMD ["httpd"]
ENTRYPOINT ["/entrypoint.sh"]
