# Twitter Warmup

A simple, multi-threaded, asynchronous python script to warmup your twitter accounts
automate the telegram you-to-you subscription and following back

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Prerequisites

List any prerequisites or dependencies that users need to have before they can use your project. For example:
- Python 3.11 (*IMPORTANT!*)
- A virtual environment tool (e.g., `virtualenv`, `venv`, or `conda`)

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/BlathanAevon/twitter_warmup.git
   cd twitter_warmup
   ```
2. Create a `venv` (virtual environment):
  ```bash
  pythhon (or python3) -m venv venv
  ```

  **Identify your system!**
  
  On Windows:
  ```cmd
  venv\Scripts\activate
  ```
  On MacOS:
  ```zsh
  source venv/bin/activate
  ```
3. Install required modules:
   ```bash
   pip install -r requirements.txt
   ```

## Config files
in `msg.txt` - put the message which you want to be sent to telegram chats
in `chats.txt` - put chats names without @ or t.me
in `tokens.txt` - put tokens of twitter profiles
in `proxies.txt` - put proxies in format `socks5://user:password:ip:port`
in `.env` - put the data from `https://my.telegram.org/apps`


# RUN
```python
python main.py
```

  

