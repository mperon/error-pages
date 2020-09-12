{{#pages}}
error_page {{id}} /error/{{id}}.html;
{{/pages}}

location /error {
    root /var/www;
    internal;
}
