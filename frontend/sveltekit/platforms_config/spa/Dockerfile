FROM alexxxnf/spa-builder as builder

WORKDIR app
COPY ./package.json /
RUN yarn

COPY . /
RUN yarn run build && for i in `find | grep -E "\.css$|\.html$|\.js$|\.svg$|\.txt$|\.ttf$"`; do gzip -9kf "$i" \
    && brotli -fZ "$i" ; done

FROM alexxxnf/nginx-spa
COPY --from=builder /public /etc/nginx/html/