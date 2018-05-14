#! /usr/bin/python

# infinite chill / 2017

import sys, os
import argparse
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS


def make_press_kit(title,info,logo,image1,image2,link1,link2,link3,output_file):
    with open(info) as f:
        f = list(f)
        a, b, c = (list(__import__('itertools').islice(f, i, None, 3)) for i in range(3))
    par1 = ''.join(a).replace('\n', "")
    par2 = ''.join(b).replace('\n', "")
    par3 = ''.join(c).replace('\n', "")

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("mypresskit.html")

    template_vars = {
        "title" : title,
        "par1" : par1,
        "par2" : par2,
        "par3" : par3,
        "logo" : logo,
        "image1" : image1,
        "image2" : image2,
        "link1" : link1,
        "link2" : link2,
        "link3" : link3
    }

    html_out = template.render(template_vars)
    HTML(string=html_out,base_url="").write_pdf(output_file,stylesheets=[CSS('style.css')], presentational_hints=True)
    return os.path.isfile(output_file) 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', help='title')
    parser.add_argument('--info', help='info file')
    parser.add_argument('--logo', help='logo file')
    parser.add_argument('--image1', help='image1 file')
    parser.add_argument('--image2', help='image2 file')
    parser.add_argument('--link1', help='link1')
    parser.add_argument('--link2', help='link2')
    parser.add_argument('--link3', help='link3')   
    parser.add_argument('--output', help='output file')
    args = parser.parse_args()

    successful = make_press_kit(args.title,args.info,args.logo,args.image1,args.image2,args.link1,args.link2,args.link3,args.output)

    if successful:
        print args.output
    else:
        print "Error."

if __name__ == '__main__':

    main()
