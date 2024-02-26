# using Nginx base image
FROM nginx

# delete nginx default .conf files
RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf

# add the .conf files we have created
COPY nginx_green.conf /etc/nginx/nginx_green.conf
COPY nginx_blue.conf /etc/nginx/nginx_blue.conf

RUN ln -s /etc/nginx/nginx_green.conf /etc/nginx/nginx.conf