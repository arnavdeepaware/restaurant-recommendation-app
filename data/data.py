import kagglehub

# Download latest version
path = kagglehub.dataset_download("ahmedshahriarsakib/uber-eats-usa-restaurants-menus")

print("Path to dataset files:", path)   