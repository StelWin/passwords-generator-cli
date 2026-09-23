# newpass

A tiny command-line tool that generates strong passwords you can actually type on a phone.

```
$ newpass
uvufag-Jau3uv-3kanfF-sju3gs
```

- **Easy to type on a phone.** Mostly lowercase, so you rarely need to switch keyboards, yet every password contains at least one capital letter and one digit, so it passes the usual site rules.
- **No look-alike characters.** `i l o I L O 0` are never used.
- **Strong.** About 128 bits of entropy, drawn from `/dev/urandom`.
- **No dependencies.** One shell script that works on macOS and Linux out of the box.

## Install

```
git clone https://github.com/StelWin/passwords-generator.git
ln -s "$PWD/passwords-generator/newpass" ~/.local/bin/newpass
```

Make sure `~/.local/bin` is on your `PATH`. Or simply copy `newpass` to any directory on your `PATH`.
