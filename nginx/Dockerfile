# NGINX 
FROM nginx

#RUN rm /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/conf.d/default.conf

#RUN rm /etc/nginx/conf.d/examplessl.conf

ADD sites-enabled/ /etc/nginx/sites-enabled

#COPY conf /etc/nginx