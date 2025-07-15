import subprocess


def main():
    commands = [
        ["docker", "compose", "stop", "tasks_app"],
        ["docker", "compose", "up", "-d", "--build", "tasks_app"],
    ]
    for command in commands:
        subprocess.run(command)


if __name__ == "__main__":
    main()
