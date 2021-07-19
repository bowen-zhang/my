FROM envoyproxy/envoy:v1.18.2
EXPOSE 8082
COPY src/envoy.yaml /etc/envoy/envoy.yaml