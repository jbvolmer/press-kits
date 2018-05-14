#infinite chill / 2017
all: clean press-kits run

press-kits: press-kits.py
	cp press-kits.py press-kits
	chmod u+x press-kits
run:
	./press-kits \
	--title "Aaron Cohen: Off the Ground" \
	--info "info.txt" \
	--logo "logo.png" \
	--image1 "image1.jpg" \
	--image2 "image2.jpg" \
	--link1 "http://www.candydrips.com" \
	--link2 "http://candydrips.bigcartel.com"  \
	--link3 "http://twitter.com/candydrips" \
	--output "output.pdf"

clean:
	rm -f press-kits
	