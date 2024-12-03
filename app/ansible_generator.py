import os

def generate_ansible(max_connections, shared_buffers):
    ansible_dir = "ansible/"
    os.makedirs(ansible_dir, exist_ok=True)

    playbook_content = f"""
    - hosts: all
      become: true
      tasks:
        - name: Install PostgreSQL
          apt:
            name: postgresql
            state: present

        - name: Configure PostgreSQL settings
          lineinfile:
            path: /etc/postgresql/14/main/postgresql.conf
            regexp: "^#?max_connections"
            line: "max_connections = {max_connections}"
          notify: restart postgresql

        - name: Configure shared_buffers
          lineinfile:
            path: /etc/postgresql/14/main/postgresql.conf
            regexp: "^#?shared_buffers"
            line: "shared_buffers = {shared_buffers}"
          notify: restart postgresql

      handlers:
        - name: restart postgresql
          service:
            name: postgresql
            state: restarted
    """

    with open(os.path.join(ansible_dir, "playbook.yml"), "w") as f:
        f.write(playbook_content)
