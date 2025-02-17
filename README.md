# Selenium test playground

Examples of using Selenium with Python and WSL2.

I could only get it to work when the Chrome was installed
via Ubuntu WSL2, rather than linking to the Windows installation.

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
sudo apt install chromium-chromedriver

python3.12 -m venv venv
source venv/bin/activate
pip install selenium
```
