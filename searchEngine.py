import subprocess

ls = []

for add in range(10):
    for iL in range(256):
        ip = f"192.168.{add}.{iL}"
        ls.append(ip)

for curr in ls:
    try:
        resp = subprocess.run(
            ["ping", "-n", "1", curr],
            capture_output=True,
            text=True
        )

        if resp.returncode == 0:
            print(f"{curr} is reachable")
        else:
            print(f"{curr} is not reachable")

    except Exception as e:
        print(f"{curr} is not reachable")