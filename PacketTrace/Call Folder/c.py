import pyshark


namefile = "callWiFi.pcapng"
captures = pyshark.FileCapture(input_file=namefile)
