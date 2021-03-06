# yaow
 Yet another openconnect wrapper.

This is a simple script to make connecting with openconnect easier, along with storing mfa codes in your local keychain.

This makes your 2nd factor the physical device that the keychain is stored on.

## Usage

```
% yaow --help
usage: yaow [-h] [--username USERNAME] [--server SERVER] [--servercert SERVERCERT] [--group GROUP] [--script SCRIPT] [--totp] [--email EMAIL]
            [--folder FOLDER] [--regex REGEX] [--backupKeyringFile BACKUPKEYRINGFILE] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   Username to connect to. The script will prompt for the password and store it in the keychain.
  --server SERVER       Server to connect to. Example https://1.1.1.1/vpn
  --servercert SERVERCERT
                        Example: pin-sha256:k+H........=
  --group GROUP         Group name when connecting. Passed to --authgroup=
  --script SCRIPT       Script argument to pass to openconnect.
  --totp                TOTP 2-factor authentication
  --email EMAIL         Email mfa authentication
  --folder FOLDER       Email folder to watch for mfa token.
  --regex REGEX         Regular expression to match the mfa token.
  --backupKeyringFile BACKUPKEYRINGFILE
                        Keyring file location if your os doesn't have a keyring installed. Defaults to /keyring.json.
  --debug               Enable debug traceback.
```

## Example
```
~ % yaow --username user --servercert pin-sha256:pADF6S+9sLpt0uGWl3upUIFQX9+Gmv3kZr73r2D2As= --server https://1.2.3.4/ --group "Cisco AnyConnect VPN" --script 'vpn-slice 10.1.1.0/24'
```

## Building and Installing

```
python3 setup.py bdist_wheel --universal
python3 -m pip install dist/yaow-*-py2.py3-none-any.whl
```


## Changelog

### 0.0.1
- Initial Release