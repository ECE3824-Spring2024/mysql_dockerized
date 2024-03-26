def generate_nginx_config(site_name, root_path):
    config = f"""
    server {{
        listen 80;
        server_name {site_name};

        root {root_path};
        index index.html;

        location / {{
            try_files $uri $uri/ =404;
        }}
    }}
    """

    return config

def write_config_to_file(config_text, file_path):
    with open(file_path, 'w') as f:
        f.write(config_text)

# Example usage:
site_name = "yourdomain.com"
root_path = "/path/to/your/webpage"
config_text = generate_nginx_config(site_name, root_path)
config_file_path = "/etc/nginx/sites-available/yourwebsite.conf"
write_config_to_file(config_text, config_file_path)
