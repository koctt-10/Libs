import speedtest as st


def speedtest():
    test = st.Speedtest()
    
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print(f"Downloading speed in Mbps: {down_speed}")
    
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print(f"Uploading speed in Mbps: {up_speed}")
    
    ping = test.results.ping
    print(f"Ping: {ping}")

speedtest()