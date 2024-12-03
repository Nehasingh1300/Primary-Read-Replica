import os

def generate_terraform(postgres_version, instance_type, num_replicas):
    terraform_dir = "terraform/"
    os.makedirs(terraform_dir, exist_ok=True)

    # main.tf template
    main_tf_content = f"""
    provider "aws" {{
      region = "us-east-1"
    }}

    resource "aws_instance" "postgres_primary" {{
      ami           = "ami-0c55b159cbfafe1f0"
      instance_type = "{instance_type}"
      tags = {{
        Name = "postgres-primary"
      }}
    }}

    resource "aws_instance" "postgres_replica" {{
      count         = {num_replicas}
      ami           = "ami-0c55b159cbfafe1f0"
      instance_type = "{instance_type}"
      tags = {{
        Name = "postgres-replica-${{count.index + 1}}"
      }}
    }}
    """

    with open(os.path.join(terraform_dir, "main.tf"), "w") as f:
        f.write(main_tf_content)

    # Write variables.tf (optional, based on your structure)
    # Add other files like outputs.tf as needed.
