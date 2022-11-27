import logging
import os
import sys

from rubikscolorresolver.color import LabColor, html_color

logger = logging.getLogger(__name__)

ALL_COLORS = ("Bu", "Gr", "OR", "Rd", "Wh", "Ye")

if sys.implementation.name == "pybricks-micropython":
    HTML_FILENAME = "rubiks-color-resolver.html"
else:
    HTML_FILENAME = "/tmp/rubiks-color-resolver.html"

try:
    os.unlink(HTML_FILENAME)
except Exception:
    pass


def get_important_square_indexes(size):
    squares_per_side = size * size
    max_square = squares_per_side * 6
    first_squares = []
    last_squares = []

    for index in range(1, max_square + 1):
        if (index - 1) % squares_per_side == 0:
            first_squares.append(index)
        elif index % squares_per_side == 0:
            last_squares.append(index)

    last_UBD_squares = (last_squares[0], last_squares[4], last_squares[5])
    return (first_squares, last_squares, last_UBD_squares)


crayola_colors = {
    # Handy website for converting RGB tuples to hex
    # http://www.w3schools.com/colors/colors_converter.asp
    #
    # These are the RGB values as seen via a webcam
    #   white = (235, 254, 250)
    #   green = (20, 105, 74)
    #   yellow = (210, 208, 2)
    #   orange = (148, 53, 9)
    #   blue = (22, 57, 103)
    #   red = (104, 4, 2)
    "Wh": LabColor(100.0, 0.00526049995830391, -0.01040818452526793, 255, 255, 255),
    "Gr": LabColor(39.14982168015123, -32.45052099773829, 10.60519920674466, 20, 105, 74),
    "Ye": LabColor(97.13824698129729, -21.55590833483229, 94.48248544644462, 255, 255, 0),
    "OR": LabColor(35.71689493804023, 38.18518746791636, 43.98251678431012, 148, 53, 9),
    "Bu": LabColor(23.92144819784853, 5.28400492805528, -30.63998357385018, 22, 57, 103),
    "Rd": LabColor(20.18063311070288, 40.48184409611946, 29.94038922869042, 104, 4, 2),
}


def open_mode(filename):        
    return "w"


class WwwMixin:
    def www_header(self):
        """
        Write the <head> including css
        """
        side_margin = 10
        square_size = 40
        size = self.width

        print("")

    def write_color_corners(self, desc, corners):
        print("")

    def write_color_edge_pairs(self, desc, square_pairs):
        print("")

    def write_colors(self, desc, squares):
        print("")

    def www_footer(self):
        print("")

    def html_cube(self, desc, use_html_colors, div_class):
        cube = ["dummy"]

        for side in (
            self.sideU,
            self.sideL,
            self.sideF,
            self.sideR,
            self.sideB,
            self.sideD,
        ):
            for position in range(side.min_pos, side.max_pos + 1):
                square = side.squares[position]

                if use_html_colors:
                    red = html_color[square.color_name]["red"]
                    green = html_color[square.color_name]["green"]
                    blue = html_color[square.color_name]["blue"]
                else:
                    red = square.lab.red
                    green = square.lab.green
                    blue = square.lab.blue

                cube.append((red, green, blue, square.color_name, square.lab))

        col = 1
        squares_per_side = self.width * self.width
        max_square = squares_per_side * 6

        sides = ("upper", "left", "front", "right", "back", "down")
        side_index = -1
        (first_squares, last_squares, last_UBD_squares) = get_important_square_indexes(self.width)

        html = []
        html.append("<div class='cube {}'>".format(div_class))
        html.append("<h1>%s</h1>\n" % desc)
        for index in range(1, max_square + 1):
            if index in first_squares:
                side_index += 1
                html.append("<div class='side' id='%s'>\n" % sides[side_index])

            (red, green, blue, color_name, lab) = cube[index]

            html.append(
                "    <div class='square col%d' title='RGB (%d, %d, %d), Lab (%s, %s, %s), "
                "color %s' style='background-color: #%02x%02x%02x;'><span>%02d</span></div>\n"
                % (
                    col,
                    red,
                    green,
                    blue,
                    int(lab.L),
                    int(lab.a),
                    int(lab.b),
                    color_name,
                    red,
                    green,
                    blue,
                    index,
                )
            )

            if index in last_squares:
                html.append("</div>\n")

                if index in last_UBD_squares:
                    html.append("<div class='clear'></div>\n")

            col += 1

            if col == self.width + 1:
                col = 1

        html.append("</div>")
        return "".join(html)

    # def write_html(self, html):
    #     with open(HTML_FILENAME, open_mode(HTML_FILENAME)) as fh:
    #         fh.write(html)

    def _write_colors(self, desc, box):
        print("")

    def write_crayola_colors(self):
        self._write_colors("crayola box", crayola_colors)

    def write_color_box(self):
        self._write_colors("color_box", self.color_box)