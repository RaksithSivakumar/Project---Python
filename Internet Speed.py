import speedtest

test = speedtest.Speedtest()
print("Loading server list....")

test.get_servers()
print("Choosing best server...")
best = test.get_best_server()
print(f"Found: {best['host']} located in {best['country']}")

print("Performing download test...")
download_result = test.download()
print("Performing upload test...")
upload_result = test.upload()

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbps")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbps")
