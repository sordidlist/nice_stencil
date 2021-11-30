import os

a = 0x000000
b = 0xffffff

try:
    os.system('rm ./colors.py')
except Exception:
    print()
colors_py = open('colors.py', 'w')

colors_py.write("from fabulous import color\n\n\n")
test_counter = 0
tests = ""

for x in range(a, b + 1):
    h = format(x, '06x')
    if test_counter % 5000 == 0:
        colors_py.write("def bg_{}(text):\n\treturn color.bg256('{}', text)\n\n\ndef fg_{}(text):\n\treturn "
                        "color.fg256('{}', text)\n\n\n".format(h, h, h, h))
    if test_counter % 25000 == 0:
        tests += "print(test_output_format.format(fg_{}('{}'), bg_{}('{}')))\n\t".format(h, h, h, h)
    test_counter += 1

tof = "\\t{}\\t\\t{}"
colors_py.write("if __name__ == '__main__':\n\ttest_output_format = '{}'\n\t{}".format(tof, tests))

colors_py.close()
