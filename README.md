# Open Redirection Vulnerability Tool

________                      __________________  ____  ___
\_____  \ ______   ____   ____\______   \______ \ \   \/  /
 /   |   \\____ \_/ __ \ /    \|       _/|    |  \ \     / 
/    |    \  |_> >  ___/|   |  \    |   \|    `   \/     \ 
\_______  /   __/ \___  >___|  /____|_  /_______  /___/\  \
        \/|__|        \/     \/       \/        \/      \_/



## Installation

To install the tool, clone the repository and use the `setup.py` file to install the necessary dependencies and create a command-line script.

```sh
git clone https://github.com/AwakenDoldsoul2/OpenRDX..git
cd OpenRDX.

For a single URL:
python3 main.py -u http://example.com -p payloads.txt -o output.txt

For multiple URLs from a file:
python3 main.py -U urls.txt -p payloads.txt -o output.txt


