def display_banner():
    banner = """
    
                              v1.0
________                      __________________  ____  ___
\_____  \ ______   ____   ____\______   \______ \ \   \/  /
 /   |   \\____ \_/ __ \ /    \|       _/|    |  \ \     / 
/    |    \  |_> >  ___/|   |  \    |   \|    `   \/     \ 
\_______  /   __/ \___  >___|  /____|_  /_______  /___/\  \
        \/|__|        \/     \/       \/        \/      \_/


    $OpenRDX.py [options]

    usage: OpenRDX.py [options]

    Options:
    -h, --help               help menu
    -u, --url URL            URL to scan 
    -U, --url_file FILE      File containing URLs to scan
    -p, --payload <filename> read payload from txt
    -o, --output_file FILE   Output file to save vulnerable URLs
    """
    print(banner)

