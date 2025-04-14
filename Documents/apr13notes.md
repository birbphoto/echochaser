Install gowall
https://github.com/Achno/gowall

Sadly only easy on my Arch build.
Might have to switch to arch :P
I used yay -S gowall

You may have to build from source:
`git clone https://github.com/Achno/gowall
cd gowall
go build
sudo cp gowall /usr/local/bin/
gowall`

Syntax I used (nyc.jpg as example)
gowall convert nyc.jpg -t nord --output ./nycnord.jpg

I will make the theme soon!